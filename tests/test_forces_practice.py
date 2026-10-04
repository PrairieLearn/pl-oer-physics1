"""Exhaustive Forces checks using the installed PrairieLearn MC element.

Run in the local PL container:
  python3 tests/test_forces_practice.py --pl-root /PrairieLearn/apps/prairielearn
No database or live assessment is modified.
"""
import argparse
import copy
import importlib.util
import json
import os
from pathlib import Path
import random
import re
import sys
import unittest

parser = argparse.ArgumentParser()
parser.add_argument("--pl-root", type=Path, required=True)
parser.add_argument("--course-root", type=Path, default=Path(__file__).resolve().parents[1])
args, remaining = parser.parse_known_args()
ROOT = args.course_root.resolve()
PL = args.pl_root.resolve()
sys.path[:0] = [str(ROOT / "serverFilesCourse"), str(PL / "python")]

import chevron
import jsonschema
import lxml.html

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

ELEMENT_DIR = PL / "elements/pl-multiple-choice"
mc = load_module(ELEMENT_DIR / "pl-multiple-choice.py", "forces_mc")
G = 9.8

def new_data():
    return dict(params={}, correct_answers={}, submitted_answers={}, format_errors={},
                partial_scores={}, feedback={}, raw_submitted_answers={},
                options={"question_path": "."}, panel="question", editable=True)

def plain(value):
    return " ".join(lxml.html.fragment_fromstring(value, create_parent=True).text_content().split())

def numbers(value):
    # All answer calculations use exactly two decimal places. Ignore unit exponents.
    return [float(x) for x in re.findall(r"(?<![\w.])-?\d+\.\d{2}(?!\d)", value)]

def rounded(values):
    return [float(f"{x:.2f}") for x in values]

def expected(qid, x):
    """Independent solutions from the supplied observations, not hidden case answers."""
    if qid == "brakingShuttle":
        t, v, a = x["time"], x["speed"], -x["deceleration"]
        floor_distance = v*t
        shuttle_distance = v*t + a*t*t/2
        return {"motion": [v, floor_distance-shuttle_distance]}
    if qid == "robotTraction":
        return {"traction": [x["force"]/x["mass"]]}
    if qid == "lunarCalibration":
        support = x["reading"]*G
        return {"mass_weight": [support/x["local_g"], support], "hover": [support]}
    if qid == "liftAssist":
        return {"first_trial": [x["weight"]-x["first"]],
                "second_trial": [(x["second"]-x["weight"])/(x["weight"]/G)]}
    if qid == "descentScale":
        a = (0-(-x["initial_down_speed"]))/x["time"]
        return {"display": [x["mass"]*(G+a)/G]}
    if qid == "stackedInstruments":
        a = (-x["v2"]-(-x["v1"]))/x["time"]
        contact = x["upper_mass"]*(G+a)
        support = x["lower_mass"]*a + x["lower_mass"]*G + contact
        return {"force_inventory": [support, x["lower_mass"]*G, contact]}
    if qid == "cameraLauncher":
        a = (x["force"]-x["mass"]*G)/x["mass"]
        v = a*x["contact_time"]
        return {"rise": [v*v/(2*G)], "apex": [G, x["mass"]*G]}
    if qid == "netCatcher":
        mass = x["mass_grams"]/1000
        a = (0-x["entry_speed"]**2)/(2*(-x["stopping_distance"]))
        return {"net_force": [mass*a+mass*G]}
    if qid == "springSeparation":
        return {"accelerations": [x["force"]/x["light_mass"], x["force"]/x["heavy_mass"]]}
    if qid == "counterweightHoist":
        mass = x["weight"]/G
        a = (x["tension"]-x["weight"])/mass
        return {"stop": [mass, -x["initial_up_speed"]/a]}
    if qid == "sensorCalibration":
        a = x["moving_reading"]*G/x["rest_reading"]-G
        return {"velocity_mass": [abs(a*x["time"]), x["rest_reading"]]}
    if qid == "coupledModules":
        # Solve the two bodies' equations together, then reapply the rear-body equation.
        a1 = x["first_tension"]/x["rear_mass"]
        drive = x["front_mass"]*a1 + x["first_tension"]
        a2 = drive/(x["front_mass"]+x["payload_mass"]+x["rear_mass"])
        return {"drive_and_link": [drive, x["rear_mass"]*a2]}
    if qid == "liftStackSensor":
        # Eliminate g+a by subtracting the measured contact forces first.
        effective_g = (x["beneath_force"]-x["between_force"])/x["lower_mass"]
        return {"hidden_mass": [x["between_force"]/effective_g, abs(effective_g-G)]}
    if qid == "opposedDrives":
        a = -x["initial_speed"]/x["stopping_time"]
        return {"mass": [(x["drive"]-x["brake"])/a]}
    if qid == "launcherDesign":
        release_v2 = 2*G*x["free_height"]
        a = release_v2/(2*x["stroke"])
        return {"actuator_force": [x["mass"]*a + x["mass"]*G]}
    if qid in {"corneringCarrier", "motionEvidence", "collisionEvidence", "gravityLabels", "forceSwitch"}:
        return {}
    raise AssertionError("Missing independent oracle: "+qid)

# Numeric options in these parts represent exactly the same quantities and directions.
# Hence any distractor with the same tuple would also be a correct answer.
NUMERIC_ONLY = {
    "mass_weight", "display", "force_inventory", "rise", "net_force",
    "accelerations", "stop", "drive_and_link", "mass", "actuator_force",
}
class ForcesPracticeTests(unittest.TestCase):
    def test_every_case_render_physics_and_grade(self):
        counts = dict(variants=0, parts=0, graded_options=0)
        for folder in sorted((ROOT/"questions/forcesPractice").iterdir()):
            if not folder.is_dir():
                continue
            qid = folder.name
            server = load_module(folder/"server.py", qid)
            template = (folder/"question.html").read_text()
            rendered_variants = set()
            for case in server.CASES:
                with self.subTest(qid=qid, case=case):
                    data = new_data()
                    server.build(data, case)
                    json.dumps(data, allow_nan=False)
                    p = data["params"]
                    reference = expected(qid, p["givens"])
                    self.assertEqual(len({part["name"] for part in p["parts"]}), len(p["parts"]))
                    for part in p["parts"]:
                        correct = [a["text"] for a in part["choices"] if a["correct"] == "true"]
                        self.assertEqual(len(correct), 1)
                        self.assertEqual(len(part["choices"]), 4)
                        self.assertEqual(len({plain(a["text"]).casefold() for a in part["choices"]}), 4)
                        self.assertTrue(part["solution"].strip())
                        if part["name"] in reference:
                            want = rounded(reference[part["name"]])
                            self.assertEqual(numbers(correct[0]), want)
                            if part["name"] in NUMERIC_ONLY:
                                matching = [a for a in part["choices"] if numbers(a["text"]) == want]
                                self.assertEqual(len(matching), 1, "Physically equivalent numeric options")
                    self.check_directions(qid, p)
                    self.check_conceptual_models(qid, p)
                    rendered = chevron.render(template, data)
                    self.assertNotIn("{{", rendered)
                    rendered_variants.add(rendered)
                    doc = lxml.html.fragment_fromstring(rendered, create_parent=True)
                    elements = doc.findall(".//pl-multiple-choice")
                    self.assertEqual(len(elements), len(p["parts"]))
                    self.assertFalse(doc.findall(".//pl-number-input"))
                    self.assertEqual(len(doc.findall(".//pl-answer-panel")), 1)
                    for element in elements:
                        name = element.get("answers-name")
                        elem_html = lxml.html.tostring(element, encoding="unicode")
                        mc.prepare(elem_html, data)
                        choices = data["params"][name]
                        self.assertEqual(len(choices), 4)
                        self.assertEqual(len({plain(a["html"]) for a in choices}), 4)
                        correct_key = data["correct_answers"][name]["key"]
                        # All four options go through the actual native parse/grade code.
                        for choice in choices:
                            trial = copy.deepcopy(data)
                            trial["submitted_answers"][name] = choice["key"]
                            mc.parse(elem_html, trial)
                            self.assertEqual(trial["format_errors"], {})
                            mc.grade(elem_html, trial)
                            self.assertEqual(trial["partial_scores"][name]["score"],
                                             1 if choice["key"] == correct_key else 0)
                            counts["graded_options"] += 1
                        previous = Path.cwd()
                        try:
                            os.chdir(ELEMENT_DIR)
                            for panel in ("question", "answer", "submission"):
                                data["panel"] = panel
                                self.assertTrue(mc.render(elem_html, data))
                        finally:
                            os.chdir(previous)
                        counts["parts"] += 1
                    counts["variants"] += 1
            self.assertGreater(len(rendered_variants), 1, qid+" has no visible variation")
            # Test the production generate entry point and seeded repeatability too.
            random.seed(173)
            one = new_data()
            server.generate(one)
            random.seed(173)
            two = new_data()
            server.generate(two)
            self.assertEqual(one, two)
        print("Exhaustive coverage:", counts)

    def check_directions(self, qid, p):
        answer = {x["name"]: next(a["text"] for a in x["choices"] if a["correct"]=="true")
                  for x in p["parts"]}
        if qid == "brakingShuttle":
            self.assertIn("east", answer["motion"])
            self.assertIn("ahead", answer["motion"])
            self.assertGreater(p["givens"]["speed"]-p["givens"]["deceleration"]*p["givens"]["time"], 0)
        if qid == "robotTraction":
            self.assertIn("floor pushes the wheels east", answer["traction"])
        if qid == "liftAssist":
            self.assertLess(p["givens"]["first"], p["givens"]["weight"])
            self.assertGreater(p["givens"]["second"], p["givens"]["weight"])
            self.assertIn("bench contact force 0 N", answer["second_trial"])
        if qid == "sensorCalibration":
            self.assertLess(p["givens"]["moving_reading"], p["givens"]["rest_reading"])
            self.assertIn("downward", answer["velocity_mass"])
        if qid == "liftStackSensor":
            x = p["givens"]
            signed = (x["beneath_force"]-x["between_force"])/x["lower_mass"]-G
            direction = "upward" if signed > 0 else "downward"
            self.assertIn(direction, answer["hidden_mass"])
            # The opposite-direction distractor is not an equivalent answer.
            matching = [a for a in p["parts"][0]["choices"]
                        if numbers(a["text"]) == numbers(answer["hidden_mass"]) and direction in a["text"]]
            self.assertEqual(len(matching), 1)
        if qid == "netCatcher":
            self.assertLess(p["givens"]["weak_force"], p["givens"]["mass_grams"]/1000*G)
            self.assertIn("downward and its downward speed increases", answer["weak_catch"])
        if qid == "springSeparation":
            self.assertIn("left", answer["accelerations"].split(";")[0])
            self.assertIn("right", answer["accelerations"].split(";")[1])
        if qid == "corneringCarrier":
            self.assertIn("straight path toward "+p["givens"]["original"], answer["trajectory"])


    def check_conceptual_models(self, qid, p):
        if qid not in {"motionEvidence", "collisionEvidence", "gravityLabels", "forceSwitch"}:
            return
        self.assertEqual(len(p["parts"]), 1)
        x = p["givens"]
        if qid == "motionEvidence":
            # Construct representative motion measurements, then apply F = m dv/dt.
            sign = 1 if x["direction"] == "right" else -1
            speed_change = {"steady": 0, "speeding": 1, "slowing": -1}[x["motion"]]
            masses = {"A": 3 if x["heavier"] == "A" else 1,
                      "B": 3 if x["heavier"] == "B" else 1}
            v_before = {"A": 4*sign, "B": 2*sign}
            v_after = {key: value+speed_change*sign for key, value in v_before.items()}
            forces = {key: masses[key]*(v_after[key]-v_before[key]) for key in masses}
            if forces["A"] == forces["B"] == 0:
                correct_model = "zero"
            else:
                self.assertGreater(abs(forces[x["heavier"]]), abs(forces["B" if x["heavier"]=="A" else "A"]))
                correct_model = "heavier_along" if forces["A"]*sign > 0 else "heavier_opposite"
        elif qid == "collisionEvidence":
            correct_model = "pair_and_mass"
            lighter = "B" if x["heavier"] == "A" else "A"
            choice = next(c for c in p["parts"][0]["choices"] if c["model"]==correct_model)
            self.assertIn("case "+lighter+" has the greater acceleration magnitude", choice["text"])
        elif qid == "gravityLabels":
            g = {"A": 1 if x["weak_site"]=="A" else 2,
                 "B": 1 if x["weak_site"]=="B" else 2}
            masses = {key: 1/value if x["matching"]=="weight" else 1 for key, value in g.items()}
            # Under unit force, time to reach unit speed is m; compare without using hidden answers.
            correct_model = "same" if masses["A"]==masses["B"] else ("A_first" if masses["A"]<masses["B"] else "B_first")
        else:
            initial_v = 1 if x["direction"]=="right" else -1
            forces = {"right": 1, "left": -1}
            del forces[x["switched_off"]]
            acceleration = sum(forces.values())
            v_later = initial_v + acceleration*3
            if initial_v*v_later < 0:
                correct_model = "reverse"
            else:
                self.assertGreater(abs(v_later), abs(initial_v))
                correct_model = "speed_up"
        choices = p["parts"][0]["choices"]
        self.assertEqual(len({c["model"] for c in choices}), 4)
        for choice in choices:
            self.assertEqual(choice["correct"]=="true", choice["model"]==correct_model)

    def test_schemas_assessment_membership_and_identity(self):
        question_schema = json.loads((PL/"src/schemas/schemas/infoQuestion.json").read_text())
        assessment_schema = json.loads((PL/"src/schemas/schemas/infoAssessment.json").read_text())
        all_ids, uuids = [], []
        for number in (1, 2):
            path = ROOT/f"courseInstances/HighSchoolPhysics/assessments/forces-practice-{number}/infoAssessment.json"
            assessment = json.loads(path.read_text())
            jsonschema.validate(assessment, assessment_schema)
            uuids.append(assessment["uuid"])
            self.assertEqual(assessment["number"], str(4+number))
            self.assertTrue(assessment["multipleInstance"])
            self.assertTrue(assessment["allowRealTimeGrading"])
            questions = [q for z in assessment["zones"] for q in z["questions"]]
            self.assertEqual(len(questions), 10)
            for question in questions:
                self.assertEqual(set(question), {"id", "autoPoints"})  # No pools/alternatives.
                self.assertEqual(question["autoPoints"], [5, 4, 3])
                all_ids.append(question["id"])
                metadata = json.loads((ROOT/"questions"/question["id"]/"info.json").read_text())
                jsonschema.validate(metadata, question_schema)
                self.assertEqual(metadata["topic"], "Forces")
                uuids.append(metadata["uuid"])
        self.assertEqual(len(all_ids), 20)
        conceptual = {"forcesPractice/motionEvidence", "forcesPractice/collisionEvidence",
                      "forcesPractice/gravityLabels", "forcesPractice/forceSwitch"}
        self.assertTrue(conceptual.issubset(set(all_ids)))
        source_map = json.loads((ROOT/"tests/forces_source_map.json").read_text())
        self.assertEqual({q["qid"] for q in source_map["questions"]}, set(all_ids))
        self.assertEqual(len(all_ids), len(set(all_ids)))
        self.assertEqual(len(uuids), len(set(uuids)))
        # Also check against existing course content when run after installation.
        old_uuids = []
        for path in (ROOT/"questions").rglob("info.json"):
            if "forcesPractice" not in path.parts:
                old_uuids.append(json.loads(path.read_text()).get("uuid"))
        for path in (ROOT/"courseInstances").rglob("infoAssessment.json"):
            if not path.parent.name.startswith("forces-practice-"):
                old_uuids.append(json.loads(path.read_text()).get("uuid"))
        self.assertFalse(set(uuids)&set(old_uuids))

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0], *remaining], verbosity=2)

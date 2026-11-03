"""Enumerate the complete finite domain; independently solve and native-grade each part.
Run: python tests/test_forces_unit2.py --pl-root /path/to/PrairieLearn/apps/prairielearn
"""
import argparse, copy, importlib.util, json, math, os, random, re, sys
from pathlib import Path
parser=argparse.ArgumentParser(); parser.add_argument('--pl-root',type=Path,required=True)
args=parser.parse_args(); ROOT=Path(__file__).resolve().parents[1]; PL=args.pl_root.resolve()
sys.path[:0]=[str(ROOT/'serverFilesCourse'),str(PL/'python')]
import chevron, jsonschema, lxml.html

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def data():
    return dict(params={},correct_answers={},submitted_answers={},format_errors={},partial_scores={},feedback={},raw_submitted_answers={},options={'question_path':'.'},panel='question',editable=True)

def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def numeric(text): return [float(v) for v in re.findall(r'(?<![\w.])-?\d+\.\d{2}(?!\d)',text)]
def oracle(q,x):
    g=9.8
    if q=='liftRatio':
        effective=x['lower']/x['m']; return {'mass':[x['upper']/effective-x['m']], 'motion':[effective-g]}
    if q=='rampRelease': return {'angle':[x['angle']], 'turn':[g*sin(x['angle'])], 'drive':[x['m']*(2+g*sin(x['angle']))]}
    if q=='rampClamp': return {'normal':[x['m']*g*cos(x['angle'])+x['P']]}
    if q=='ropeGauge': return {}
    if q=='turningCord': return {'force':[x['m']*x['a']]}
    if q=='pulleyMount': return {'support':[x['m']*g*math.sqrt(2)],'second':[2*x['m']*g]}
    if q=='atwoodInverse':
        a=x['r']*g; T=x['m']*(g+a); return {'hidden':[T/(g-a)],'tension':[T]}
    if q=='angledRating':
        T=x['ratio']*x['W']; a=math.asin(x['W']/T); return {'minimum':[math.degrees(a)],'tie':[T*math.cos(a)]}
    if q=='twoCableInference':
        U=x['T']*cos(x['A'])/cos(x['B']); return {'right':[U],'weight':[x['T']*sin(x['A'])+U*sin(x['B'])]}
    if q=='wallAngle': return {'newforce':[x['m']*g/sin(x['B'])]}
    if q=='vectorCorrection':
        east=x['F']*cos(x['A'])-x['H']; north=x['F']*sin(x['A']); assert east>0
        return {'east':[east/x['m']],'equilibrium':[math.hypot(east,north),math.degrees(math.atan2(north,east))]}
    if q=='contactLimit':
        N=x['fraction']*x['m']*g; T=(x['m']*g-N)/sin(x['A']); assert 0<N<x['m']*g
        return {'acceleration':[T*cos(x['A'])/x['m']],'threshold':[g*cos(x['A'])/sin(x['A'])]}
    if q=='hangingAccelerometer':
        T=x['m']*g/cos(x['A']); return {'values':[T*sin(x['A'])/x['m'],T]}
    raise AssertionError(q)

mc=module(PL/'elements/pl-multiple-choice/pl-multiple-choice.py','mc')
assessment=json.loads((ROOT/'courseInstances/HighSchoolPhysics/assessments/forces-unit-2/infoAssessment.json').read_text())
jsonschema.validate(assessment,json.loads((PL/'src/schemas/schemas/infoAssessment.json').read_text()))
entries=[q for z in assessment['zones'] for q in z['questions']]
assert len(entries)==13 and len({q['id'] for q in entries})==13
assert assessment['multipleInstance'] and assessment['number']=='7'
assert all(set(q)=={'id','autoPoints'} and q['autoPoints']==[5,4,3] for q in entries)
old=set()
for p in (ROOT/'courseInstances/HighSchoolPhysics/assessments').glob('*/infoAssessment.json'):
    if p.parent.name!='forces-unit-2':
        a=json.loads(p.read_text()); assert a['number']!='7'
        old.update(q.get('id') for z in a.get('zones',[]) for q in z.get('questions',[]))
assert not old.intersection(q['id'] for q in entries)
uuids=[]
for p in list((ROOT/'questions').rglob('info.json'))+list((ROOT/'courseInstances').rglob('infoAssessment.json')):
    u=json.loads(p.read_text()).get('uuid'); assert u not in uuids,(p,u); uuids.append(u)
source=json.loads((ROOT/'tests/forces_unit2_source_map.json').read_text())
assert {q['qid'] for q in source['questions']}=={q['id'] for q in entries}
counts=dict(variants=0,parts=0,graded_options=0)
for entry in entries:
    folder=ROOT/'questions'/entry['id']; q=folder.name
    jsonschema.validate(json.loads((folder/'info.json').read_text()),json.loads((PL/'src/schemas/schemas/infoQuestion.json').read_text()))
    server=module(folder/'server.py',q); template=(folder/'question.html').read_text(); variants=set()
    for case in server.CASES:
        d=data(); server.build(d,case); json.dumps(d,allow_nan=False)
        expected=oracle(q,d['params']['givens']); parts=d['params']['parts']; assert len(parts)==(3 if q=='rampRelease' else 2)
        assert len({p['name'] for p in parts})==len(parts)
        for p in parts:
            options=p['choices']; right=[o for o in options if o['correct']=='true']; assert len(right)==1
            assert len(options)==4 and len({o['text'] for o in options})==4
            if p['name'] in expected:
                want=[float(f'{v:.2f}') for v in expected[p['name']]]
                assert numeric(right[0]['text'])==want,(q,case,p['name'],right,want)
                # Directional/textual differences can intentionally retain the same numbers.
                if p['name'] in {'mass','angle','normal','second','hidden','tension','minimum','tie','right','weight','newforce','east','acceleration','drive'}:
                    assert sum(numeric(o['text'])==want for o in options)==1,(q,case,'equivalent options')
            assert p['solution']
        rendered=chevron.render(template,d); assert '{{' not in rendered; variants.add(rendered)
        elements=lxml.html.fragment_fromstring(rendered,create_parent=True).findall('.//pl-multiple-choice'); assert len(elements)==len(parts)
        for e in elements:
            text=lxml.html.tostring(e,encoding='unicode'); name=e.get('answers-name'); mc.prepare(text,d)
            choices=d['params'][name]; key=d['correct_answers'][name]['key']; assert len(choices)==4
            for choice in choices:
                trial=copy.deepcopy(d); trial['submitted_answers'][name]=choice['key']; mc.parse(text,trial); mc.grade(text,trial)
                assert not trial['format_errors']; assert trial['partial_scores'][name]['score']==int(choice['key']==key)
                counts['graded_options']+=1
            oldcwd=Path.cwd()
            try:
                os.chdir(PL/'elements/pl-multiple-choice')
                for panel in ('question','answer','submission'):
                    d['panel']=panel; assert mc.render(text,d)
            finally: os.chdir(oldcwd)
            counts['parts']+=1
        counts['variants']+=1
    assert len(variants)>1
    random.seed(73); a=data(); server.generate(a); random.seed(73); b=data(); server.generate(b); assert a==b
print('PASS:',counts,'; schemas, identities, source map, variation and repeatability verified')

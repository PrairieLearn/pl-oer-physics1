"""Presentation helpers for the high-school Forces practice questions."""
import html
import re

G = 9.8


def fmt(value):
    return f"{value:.2f}"


def part(name, prompt, correct, wrong, solution):
    """Keep every distractor tied to its original model; never perturb values."""
    texts = [correct, *wrong]
    normalized = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip() for s in texts]
    if len(texts) != 4 or len(set(normalized)) != 4:
        raise ValueError(f"{name}: answer choices must be four distinct statements")
    return {
        "name": name,
        "prompt": prompt,
        "choices": [{"text": text, "correct": "true" if i == 0 else "false"} for i, text in enumerate(texts)],
        "solution": solution,
    }


def deliver(data, context, parts, givens):
    if len({p["name"] for p in parts}) != len(parts):
        raise ValueError("Answer names must be unique within a question")
    for i, p in enumerate(parts, 1):
        p["number"] = i
    data["params"].update(context=context, parts=parts, givens=givens)

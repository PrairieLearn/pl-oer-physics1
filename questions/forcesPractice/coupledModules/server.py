import itertools
import random
from forces_practice import G, fmt, part, deliver

CASES = list(itertools.product([3, 5], [6, 8], [12, 18], [2, 4]))


def build(data, case):
    front, rear, tension, payload = case
    force = tension*(front+rear)/rear
    new_tension = force*rear/(front+rear+payload)
    context = (
        f"<p>A powered {front} kg cart pulls a passive {rear} kg trailer along a level track through a horizontal, "
        f"massless link. The link's force sensor reads {fmt(tension)} N as they accelerate together. "
        "The only external horizontal driving force acts on the front cart; all rolling resistance is negligible.</p>"
        f"<p>In a second trial, a {payload} kg payload is fixed to the front cart. The driving force is kept at exactly its first-trial value.</p>"
    )
    parts = [part("drive_and_link", "What was the driving force in the first trial, and what does the link sensor read in the second?",
        f"Driving force {fmt(force)} N; new link reading {fmt(new_tension)} N.",
        [f"Driving force {fmt(tension)} N; new link reading {fmt(tension*rear/(front+rear+payload))} N.",
         f"Driving force {fmt(force)} N; new link reading {fmt(tension)} N.",
         f"Driving force {fmt(force)} N; new link reading {fmt(force*(rear+payload)/(front+rear+payload))} N."],
        f"Use the trailer alone first: a = T/m = {fmt(tension/rear)} m/s². The drive must accelerate both carts, so "
        f"F = (M + m)a = {fmt(force)} N. With the added front payload the total mass increases and a becomes "
        f"{fmt(force/(front+rear+payload))} m/s². The link still accelerates only the rear trailer, giving "
        f"T_new = {rear}a = {fmt(new_tension)} N. Putting the payload on the wrong side of the link gives a different tension.")]
    deliver(data, context, parts, dict(front_mass=front, rear_mass=rear, first_tension=tension, payload_mass=payload))


def generate(data):
    build(data, random.choice(CASES))

"""Builds content.js and index.html from tools/content. Run: py tools/build.py"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, "content")]
from dsl import short
from units1 import UNITS as U1
from units2 import UNITS as U2
from exams import EXAMS
from formulas import FORMULAS

SITE = os.path.dirname(HERE)

CONCEPTS = [
    ("foundations", "Superposition, interferometers & entanglement", "Linearity, relative phases, beam splitters, bomb testing and product vs. entangled states."),
    ("matterwaves", "Photons & matter waves", "Photoelectric effect, Compton scattering, de Broglie wavelengths and group velocity."),
    ("schrodinger", "Wavefunctions & probability current", "The Schrödinger equation, normalization, and how probability flows."),
    ("wavepackets", "Wavepackets & momentum space", "Fourier transforms, Gaussians, spreading and expectation values in momentum space."),
    ("operators", "Operators, observables & uncertainty", "Commutators, Hermiticity, measurement, Ehrenfest and uncertainty relations."),
    ("stationary", "Stationary states & time evolution", "Expanding in eigenstates, Bohr frequencies, circles and boxes."),
    ("wells", "Wells, deltas & sketching", "Infinite and finite wells, delta potentials, node theorem and qualitative wavefunctions."),
    ("oscillator", "Harmonic oscillator", "Ladder operators, expectation values and time dependence."),
    ("scattering", "Steps, barriers & transmission", "Reflection and transmission, tunneling and resonant transmission."),
    ("phaseshift", "Phase shifts & resonances", "Half-line scattering, time delay, Levinson's theorem and resonances."),
    ("angular", "Angular momentum & central potentials", "L operators, spherical harmonics and the radial equation."),
    ("hydrogen", "Hydrogen atom", "Spectrum, wavefunctions, degeneracy and superpositions."),
]


def build_data():
    pages, exams = {}, []
    ids = {c[0] for c in CONCEPTS}
    for ex in EXAMS:
        pids = []
        for k, prob in enumerate(ex["problems"], 1):
            pid = f"{ex['id']}/p{k}"
            pids.append(pid)
            parts, order, md = {}, [], [prob["md"]]
            for j, part in enumerate(prob["parts"]):
                concept, q = part if isinstance(part, tuple) else (prob["concept"], part)
                assert concept in ids, concept
                name = chr(ord("A") + j)
                parts[name] = dict(q, name=name, concept=concept, short=short(q["prompt"]))
                order.append(name)
                md.append(f'<div class="q" data-q="{name}"></div>')
            pages[pid] = {"title": prob["title"], "exam": ex["id"], "label": ex["label"],
                          "md": "\n\n".join(md), "order": order, "questions": parts}
        exams.append({"id": ex["id"], "label": ex["label"], "kind": ex["kind"], "blurb": ex["blurb"], "pages": pids})
    return {"concepts": [{"id": a, "name": b, "description": c} for a, b, c in CONCEPTS], "exams": exams, "pages": pages}


def menu(label, entries, key):
    links = "".join(f'<a class="cs_top_menu_item menu-submenu" href="#e-{e["id"]}" role="menuitem">{e["label"]}</a>' for e in entries)
    return (f'<div class="dropdown" onmouseleave="clearMenu(this);"><label class="dropbtn cs_top_menu_item" for="cs_menu_{key}">{label}'
            f'<span aria-hidden="true" class="downarrow">▼</span></label><input checked="false" class="dropdown-checkbox screenreader-only-clip menu-toplevel" '
            f'id="cs_menu_{key}" onblur="catsoop.topMenuFocus(event);" role="menuitemcheckbox" type="checkbox"/><div class="dropdown-content">{links}</div></div>')


def build_index(data):
    t = open(os.path.join(HERE, "index.template.html"), encoding="utf8").read()
    menus = menu("Mock exams", data["exams"], "exams")
    return t.replace("<!--MENUS-->", menus)


def to_js(name, obj):
    return f"window.{name}=" + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + ";\n"


data = build_data()
# A script rather than JSON files, so index.html also works when opened directly from disk.
with open(os.path.join(SITE, "content.js"), "w", encoding="utf8", newline="\n") as f:
    f.write(to_js("XQ_DATA", data) + to_js("XQ_LEARN", {"course": U1 + U2, "formulas": FORMULAS.strip()}))
with open(os.path.join(SITE, "index.html"), "w", encoding="utf8", newline="\n") as f:
    f.write(build_index(data))
nq = sum(len(p["order"]) for p in data["pages"].values())
nl = sum(1 for c in U1 + U2 for s in c["unit"]["steps"] if s["type"] == "check")
print(f"{len(U1 + U2)} units, {nl} lesson checks, {len(data['pages'])} problems, {nq} exam parts")

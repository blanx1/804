"""Small authoring language for 8.04 lessons and exam problems (see build.py)."""
import re


def _num_check(val, unit=None, tol=0.02):
    answers = [repr(float(val))]
    if unit:
        answers.append(f"{float(val)!r} {unit}")
    return {"type": "num", "answers": answers, "tol": tol, "atol": 0 if val else 1e-9,
            "vars": [], "ranges": {}, "none": False, "words": []}


def _sig(val):
    return f"{val:.3g}" if isinstance(val, float) else str(val)


def N(prompt, val, unit=None, why="", tol=0.02, soln=None, qtype=None):
    """Numeric answer. `unit` is the unit the prompt asks for (a plain number is accepted too)."""
    return {"kind": "smallbox", "prompt": prompt, "check": _num_check(val, unit, tol),
            "soln": soln or f"${_sig(val)}$" + (f" {unit}" if unit else ""), "why": why,
            "qtype": qtype or "computational"}


def S(prompt, expr, vars, soln, why="", ranges=None, qtype=None):
    """Symbolic answer: `expr` is graded by evaluation at random values of `vars`."""
    if isinstance(vars, str):
        vars = vars.split()
    check = {"type": "num", "answers": expr if isinstance(expr, list) else [expr], "tol": 0.001, "atol": 1e-9,
             "vars": vars, "ranges": ranges or {}, "none": False, "words": []}
    return {"kind": "smallbox", "prompt": prompt, "check": check, "soln": soln, "why": why,
            "qtype": qtype or "computational"}


def M(prompt, options, answer, why="", qtype=None):
    """Multiple choice; `answer` is the index of the correct option."""
    return {"kind": "multiplechoice", "renderer": "radio", "prompt": prompt, "options": options,
            "soln": options[answer], "why": why, "qtype": qtype or "conceptual"}


def C(prompt, options, correct, why="", qtype=None):
    """Select-all; `correct` is the list of indices of the correct options."""
    return {"kind": "multiplechoice", "renderer": "checkbox", "prompt": prompt, "options": options,
            "soln": [k in correct for k in range(len(options))], "why": why, "qtype": qtype or "conceptual"}


def B(prompt, soln, why="", qtype="conceptual", rows=4):
    """Written answer: the student submits, views the reference answer, and self-reviews."""
    return {"kind": "bigbox", "prompt": prompt, "soln": soln, "why": why, "qtype": qtype, "rows": rows}


def R(title, md):
    return {"type": "read", "title": title, "md": md.strip()}


def U(id, part, lectures, title, practice, intro, steps, quiz=()):
    """A Learn unit: `steps` mixes R(...) and questions; `quiz` questions close the unit."""
    out, n = [], 0
    for s, is_quiz in [(s, False) for s in steps] + [(s, True) for s in quiz]:
        if s.get("type") == "read":
            out.append(s)
            continue
        n += 1
        q = dict(s, name=f"{id.replace('-', '_')}_Q{n}", quiz=is_quiz)
        out.append({"type": "check", "q": q})
    unit = {"id": id, "title": title, "week": part, "date": lectures, "lecture": lectures,
            "practice": practice, "intro": intro, "steps": out}
    return {"week": part, "date": lectures, "title": title, "unit": unit}


def short(prompt, limit=110):
    """A one-line preview of a prompt for the practice lists, never cut inside math."""
    t = re.sub(r"\$\$.*?\$\$", " … ", prompt, flags=re.S).replace("\n", " ").strip()
    if len(t) <= limit:
        return t
    cut, inmath = 0, False
    for k, ch in enumerate(t[:limit]):
        if ch == "$":
            inmath = not inmath
        if not inmath and ch == " ":
            cut = k
    return t[:cut].rstrip(" ,;:") + " …"


def P(title, concept, md, parts):
    """An exam problem: shared text `md`, then parts. Part entries are questions, or (concept, question)."""
    return {"title": title, "concept": concept, "md": md.strip(), "parts": parts}


def E(id, label, kind, blurb, problems):
    return {"id": id, "label": label, "kind": kind, "blurb": blurb, "problems": problems}

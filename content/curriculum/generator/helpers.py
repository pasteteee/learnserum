# -*- coding: utf-8 -*-
def S(instruction, highlight=None, param=None, op=None, value=None):
    check = None
    if param is not None:
        check = {"param": param, "op": op, "value": value}
    return {"instruction": instruction, "highlight": highlight, "check": check}


def EX(type_, title, description, target=None):
    return {"type": type_, "title": title, "description": description, "targetPatch": target}


def L(id_, title, summary, goals, concepts, synth, minutes, difficulty, steps=None, exercises=None,
      prereq=None, theory=None, unverified=False, note=None):
    d = {"id": id_, "title": title, "summary": summary, "theory": theory or [], "goals": goals, "concepts": concepts,
         "prerequisites": prereq, "estimatedMinutes": minutes, "difficulty": difficulty,
         "synthModules": synth, "steps": steps or [], "exercises": exercises or [], "unverified": unverified}
    if note:
        d["unverifiedNote"] = note
    return d


def M(id_, title, description, lessons, prereq=None):
    return {"id": id_, "title": title, "description": description, "prerequisites": prereq, "lessons": lessons}


def LV(id_, title, description, hours, modules):
    return {"id": id_, "title": title, "description": description, "estimatedHours": hours, "modules": modules}

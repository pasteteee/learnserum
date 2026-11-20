# -*- coding: utf-8 -*-
import json, re, sys
from glossary import build_glossary, MOD_SOURCES
from level0 import level0
from level1 import level1
from level2 import level2
from level3 import level3
from level45 import level4, level5
from recipes import recipes

def G(id_, name, bpm, keys, structure, key_elements, mix_tips, loudness, sources_note, unverified=False):
    return {"id": id_, "name": name, "bpm": bpm, "keys": keys, "structure": [{"section": s, "bars": b} for s, b in structure],
            "keyElements": key_elements, "mixTips": mix_tips, "loudnessNote": loudness, "sourceNote": sources_note,
            "unverified": unverified}

genres = [
    G("hardstyle-euphoric", "Хардстайл (эйфорик)", [150, 160],
      "Чаще минор с «приподнятыми» мажорными мелодиями; гармонический минор для эйфории. Тональность бочки — тоника трека.",
      [("Интро (DJ-friendly, бочка)", 32), ("Мид-интро / тизер", 16), ("Брейк: мелодическая секция без бочки", 32), ("Билд-ап", 16),
       ("Климакс (дроп)", 32), ("Мид-аутро", 16), ("Аутро (DJ-friendly)", 32)],
      ["Настроенная бочка, которая играет роль баса", "Реверс-бас на оффбитах", "Эйфорик-лид из 2–3 слоёв суперсо", "Мелодия из немногих нот, аккордовые звуки на сильных долях", "Билд: открывающийся фильтр, снейр-ролл, свипы, реверс-бочка, автоматизация посылов"],
      ["Почти всё сайдчейнится к бочке", "Посылы реверба/дилея лида — 100 % wet и сайдчейн к лиду", "Нет отдельного длинного саба в дропе: низ — хвост бочки", "Моно ниже ~150 Гц"],
      "Клубные мастера очень громкие; бочку часто клиппируют как часть звука. Ориентир −6…−4 LUFS в дропе — практический консенсус, не подтверждён замерами.",
      "BPM: источники расходятся (EDMProd 140–150, eMastered 145–150, NI 150–160); современная норма ~150. Структура в тактах — ориентировочная (у eMastered — таймкоды референса).", True),
    G("rawstyle", "Роустайл", [150, 160],
      "Минор, часто фригийский оттенок; тёмное настроение.",
      [("Интро", 32), ("Брейк / сюжетная часть", 32), ("Билд-ап", 16), ("Климакс", 32), ("Брейк 2", 16), ("Анти-климакс (роу-бочки и скричи)", 32), ("Аутро", 32)],
      ["Длинные агрессивные искажённые бочки с тональным движением", "Скричи", "Питч-лиды", "Тёмная минорная гармония"],
      ["Скрич: HPF ~500 Гц, вырез резкости около 2 кГц", "Резонансы кранча бочки чистить EQ", "Сайдчейн всего к бочке"],
      "Очень громко; клиппинг бочки — часть эстетики. Конкретные LUFS-цифры источниками не подтверждены.",
      "Темп и структура — практический консенсус; анти-климакс не подтверждён источниками.", True),
    G("uptempo", "Аптемпо / хардкор", [180, 210],
      "Минор, мрачное звучание.",
      [("Интро", 16), ("Брейк", 16), ("Билд-ап", 8), ("Дроп", 32), ("Брейк", 16), ("Дроп 2", 32), ("Аутро", 16)],
      ["Очень короткие спады бочек", "Жёсткие многослойные искажения", "Бочка доминирует в треке"],
      ["Короткие хвосты — меньше конфликта между ударами", "Контроль резкости верхней середины"],
      "Максимально громкие мастера; цифр в источниках нет.",
      "Аптемпо-специфика не подтверждена источниками.", True),
    G("hyperpop", "Хайперпоп / дигикор", [130, 210],
      "Часто яркий мажор и поп-прогрессии; пример NI: C minor – D# major – D minor – C minor.",
      [("Интро: арп, аккорды, вокал под закрытым фильтром", 16), ("Дроп / припев: фильтр открыт, полные барабаны и бас", 16), ("Глитч-лид секция", 16), ("Куплет / брейк", 16), ("Финальный дроп", 16), ("Аутро", 8)],
      ["Перегруженные, клиппированные 808 с глайдами", "Суперсо октавой-двумя выше", "Короткие квадратные плаки", "Вокал с автотюном 0 мс и сдвигом формант", "Битовое дробление и глитч", "Половинный темп в барабанах, роллы хэтов"],
      ["Аккорды ограничены по полосе (~300–850 Гц) и расширены", "Арп срезан ниже ~300 Гц", "Контраст сухого близкого вокала и перегруженного фона", "Бас нередко громче «правильного» баланса — осознанное решение"],
      "Мастера обычно очень громкие (в примере NI — максимайзер с порогом −7 дБ). Для стриминга помни про нормализацию ~−14 LUFS.",
      "Пример NI идёт на 205 BPM; на практике темп широко варьируется. Специфика дигикора не подтверждена.", True),
    G("dubstep-riddim", "Дабстеп / рыдим", [140, 145],
      "Минор (пример EDMProd — D# minor).",
      [("Затакт", 2), ("Интро-атмосфера", 8), ("Билд (синты)", 8), ("Билд (барабаны)", 8), ("Ложный дроп", 4), ("Дроп 1A", 8), ("Дроп 1B", 8),
       ("Билд (барабаны)", 8), ("Ложный дроп", 4), ("Дроп 2A", 8), ("Дроп 2B", 8), ("Аутро", 8)],
      ["Половинный темп: бочки на 1 и 3, клэпы/снейр на 2 и 4, тихие гоуст-бочки", "Простые барабаны — разнообразный бас", "Нарезанные и перепитченные басовые лупы", "Цепочка: фильтр с огибающей → дисторшн → OTT"],
      ["Саб играет одну ноту, LFO на уровень 1/4 под ритм баса", "Мид-бас и саб разделены", "Оставлять воздух между фразами баса"],
      "Громкие клубные мастера; конкретных LUFS в источниках нет.",
      "Шаблон аранжировки — EDMProd (подтверждён).", False),
    G("dnb", "Драм-н-бейс", [170, 175],
      "Чаще минор; конкретных данных о тональностях нет.",
      [("DJ-интро", 32), ("Брейкдаун", 16), ("Дроп (новые элементы каждые 16 тактов)", 48), ("Лид-аут", 16), ("Аутро без баса", 16)],
      ["Брейкбит + программные ван-шоты", "Снейр на 2 и 4 плюс лишний снейр на последней восьмой 4-тактовой фразы", "Мид-бас + отдельный саб на тех же нотах", "Нейро-рис и ресэмплинг (нейрофанк)"],
      ["Мид-бас срезан ниже ~250 Гц, саб отдельно", "Барабаны около −6 дБ каждый для запаса"],
      "DnB мастерят предельно громко, иногда около −3 LUFS (по NI); клиппер (1–2 дБ) перед лимитером, без тяжёлой компрессии.",
      "Темп: NI 160–170, туториал на 174 (современный клубный стандарт). Структура — по туториалу NI.", False),
    G("future-bass", "Фьюче-бас", [130, 160],
      "Расширенные аккорды (maj7/m7, 9, 11, 13); пример NI: Fm9 – Dbmaj9 – Ebmaj9 – C(aug5).",
      [("Интро", 8), ("Куплет", 16), ("Билд-ап", 8), ("Дроп", 16), ("Брейк", 8), ("Дроп 2", 16), ("Аутро", 8)],
      ["Аккорды суперсо с пульсацией громкости 1/16", "Трэп-барабаны в половинном темпе, хэты 1/8 с роллами 1/32", "Вибрато и питч-бенды на длинных аккордах", "Мелодия: 4 такта утверждение + 4 такта контраст"],
      ["Убрать корень из аккордов — его играет бас", "OTT на аккордах", "Сайдчейн или волюм-шейпер к бочке"],
      "Обычный поп/EDM-ориентир; для стриминга −14 LUFS-нормализация.",
      "Структура в тактах — ориентировочная; гармония, барабаны и пульсация — по NI.", True),
    G("trance", "Транс", [130, 150],
      "Чаще минор (пример NI — F# minor).",
      [("Интро", 32), ("Билд 1", 16), ("Брейкдаун без перкуссии", 32), ("Билд 2", 16), ("Главная секция", 32), ("Аутро", 32)],
      ["Бочка четыре на пол", "Оффбит-бас короткими нотами", "Слоистые синты, пэды, райзеры", "Длинные билды, разрешающиеся в брейкдауны (без «дропа» в EDM-смысле)"],
      ["Плаки и арпы — сайдчейн к бочке", "Задержки с срезом низов"],
      "Клубные мастера громче −14 LUFS; конкретных цифр в источниках нет.",
      "По NI: 125–150 BPM в целом, 130–150 в туториале. Структура в тактах — ориентировочная.", True),
]

ALLOWED_UI = {"keyboard", "meter", "init-button", "save-button", "undo-button", "preset-browser", "tabs", "tab-osc", "tab-mix",
              "tab-fx", "tab-matrix", "tab-global", "tab-arp", "tab-clip", "osc-a.edit", "osc-b.edit", "osc-c.edit", "matrix-row",
              "env1", "env2", "env3", "env4", "fx.distortion", "fx.reverb", "macro1", "macro2"}
SYNTH_MODULES = ["osc-a", "osc-b", "osc-c", "sub", "noise", "wavetable-editor", "warp", "filter", "env", "lfo", "mod-matrix",
                 "macros", "voicing", "fx", "arp", "mixer", "spectrum", "scope"]

gl = build_glossary()
errors = []


def param_ok(pid):
    if pid in gl:
        return True
    m = re.fullmatch(r"(mod|modaux):([a-z0-9-]+)->(.+)", pid)
    if m:
        return m.group(2) in MOD_SOURCES and m.group(3) in gl and not gl[m.group(3)].get("readonly")
    if re.fullmatch(r"wte\.h([1-9]|[1-5][0-9]|6[0-4])", pid):
        return True
    m = re.fullmatch(r"fx\.orderIndex\.([a-z]+)", pid)
    if m:
        return f"fx.{m.group(1)}.enabled" in gl
    return False


def value_ok(pid, op, v):
    base = pid
    if pid.startswith("mod:"):
        lo, hi = -100, 100
    elif pid.startswith("modaux:"):
        lo, hi = 0, 6
    elif pid.startswith("wte.h"):
        lo, hi = 0, 100
    elif pid.startswith("fx.orderIndex."):
        lo, hi = -1, 20
    else:
        d = gl[base]; lo, hi = d.get("min"), d.get("max")
    vals = v if isinstance(v, list) else [v]
    if op == "between" and (not isinstance(v, list) or len(v) != 2 or v[0] > v[1]):
        return False
    if op != "between" and isinstance(v, list):
        return False
    if lo is None:
        return True
    return all(lo <= x <= hi for x in vals)


levels = [level0, level1, level2, level3, level4, level5]
all_lessons, all_modules = {}, {}
prev_lesson, prev_module = None, None
for li, lv in enumerate(levels):
    lv_out = {"id": lv["id"], "order": li, "title": lv["title"], "description": lv["description"], "estimatedHours": lv["estimatedHours"], "modules": []}
    for mi, mod in enumerate(lv["modules"]):
        if mod["id"] in all_modules:
            errors.append(f"dup module {mod['id']}")
        if mod["prerequisites"] is None or (mod["prerequisites"] == [] and prev_module and mi == 0 and li > 0):
            mod["prerequisites"] = [prev_module] if prev_module else []
        mod["order"] = mi
        for le_i, les in enumerate(mod["lessons"]):
            lid = les["id"]
            if lid in all_lessons:
                errors.append(f"dup lesson {lid}")
            les["order"] = le_i
            if les["prerequisites"] is None:
                les["prerequisites"] = [prev_lesson] if prev_lesson else []
            for sm in les["synthModules"]:
                if sm not in SYNTH_MODULES:
                    errors.append(f"{lid}: bad synthModule {sm}")
            for si, st in enumerate(les["steps"]):
                st_out = {"id": f"{lid}-s{si+1}", **st}
                les["steps"][si] = st_out
                hl = st["highlight"]
                if hl is not None and not (hl in ALLOWED_UI or param_ok(hl) or hl in SYNTH_MODULES):
                    errors.append(f"{lid}: bad highlight {hl}")
                c = st["check"]
                if c:
                    if not param_ok(c["param"]):
                        errors.append(f"{lid}: bad check param {c['param']}")
                    elif c["op"] not in ("gte", "lte", "eq", "between"):
                        errors.append(f"{lid}: bad op {c['op']}")
                    elif not value_ok(c["param"], c["op"], c["value"]):
                        errors.append(f"{lid}: bad value {c}")
            for ei, ex in enumerate(les["exercises"]):
                les["exercises"][ei] = {"id": f"{lid}-ex{ei+1}", **ex}
                if ex["type"] not in ("guided", "sound-match", "ab-test", "quiz", "project"):
                    errors.append(f"{lid}: bad ex type")
                for k, v in (ex["targetPatch"] or {}).items():
                    if not param_ok(k):
                        errors.append(f"{lid}: bad target param {k}")
                    elif not value_ok(k, "eq", v):
                        errors.append(f"{lid}: target out of range {k}={v}")
            ordered = {k: les[k] for k in ["id", "order", "title", "summary", "theory", "goals", "concepts", "prerequisites",
                                            "estimatedMinutes", "difficulty", "synthModules", "steps", "exercises", "unverified"]}
            for extra in ("unverifiedNote", "recipeIds"):
                if extra in les:
                    ordered[extra] = les[extra]
            all_lessons[lid] = (lv["id"], mod["id"])
            mod["lessons"][le_i] = ordered
            prev_lesson = lid
        all_modules[mod["id"]] = lv["id"]
        prev_module = mod["id"]
        lv_out["modules"].append({k: mod[k] for k in ["id", "order", "title", "description", "prerequisites", "lessons"]})
    levels[li] = lv_out

# prereq existence & order
order_index = {lid: i for i, lid in enumerate(all_lessons)}
for lv in levels:
    for mod in lv["modules"]:
        for p in mod["prerequisites"]:
            if p not in all_modules:
                errors.append(f"module {mod['id']} bad prereq {p}")
        for les in mod["lessons"]:
            for p in les["prerequisites"]:
                if p not in all_lessons:
                    errors.append(f"lesson {les['id']} bad prereq {p}")
                elif order_index[p] >= order_index[les["id"]]:
                    errors.append(f"lesson {les['id']} prereq after it {p}")
            if les["id"] in ("what-is-sound",) or True:
                pass

# recipes
rec_ids = set()
for r in recipes:
    if r["id"] in rec_ids:
        errors.append(f"dup recipe {r['id']}")
    rec_ids.add(r["id"])
    if r["lessonId"] not in all_lessons:
        errors.append(f"recipe {r['id']} bad lesson {r['lessonId']}")
    if r["category"] not in ("lead", "pluck", "pad", "bass", "kick", "fx", "keys"):
        errors.append(f"recipe {r['id']} bad category")
    for k, v in r["patch"].items():
        if not param_ok(k):
            errors.append(f"recipe {r['id']} bad param {k}")
        elif not value_ok(k, "eq", v):
            errors.append(f"recipe {r['id']} out of range {k}={v}")
genre_ids = {g["id"] for g in genres} | {"universal"}
for r in recipes:
    for g in r["genre"]:
        if g not in genre_ids:
            errors.append(f"recipe {r['id']} bad genre {g}")
for lv in levels:
    for mod in lv["modules"]:
        for les in mod["lessons"]:
            for rid in les.get("recipeIds", []):
                if rid not in rec_ids:
                    errors.append(f"lesson {les['id']} bad recipe {rid}")

# check that L0-2 lessons all have steps
for lv in levels[:3]:
    for mod in lv["modules"]:
        for les in mod["lessons"]:
            if not les["steps"]:
                errors.append(f"no steps: {les['id']}")

if errors:
    print("\n".join(errors)); sys.exit(1)

out = {
    "version": "1.0",
    "title": "LearnSerum — курс саунд-дизайна в Serum: от теории звука до хардстайла и хайперпопа",
    "language": "ru",
    "conventions": {
        "valuesAreStartingPoints": "Все значения в рецептах и targetPatch — стартовые точки, доводятся на слух.",
        "basicShapesFrames": {"sine": 0.0, "triangle": 0.33, "saw": 0.67, "square": 1.0},
        "modAmount": "mod:<source>-><dest> — глубина в % (−100…100) от полного диапазона цели; 0 = маршрута нет.",
        "pitchModNote": "Для osc-*.coarse (±64 st) 1 % ≈ 1.28 st: +24 st ≈ 18.8 %, +48 st ≈ 37.5 %.",
        "checkOps": {"eq": "равно (для float — допуск ±1 % диапазона)", "gte": "≥", "lte": "≤", "between": "в отрезке [min, max] включительно"},
        "uiHighlightIds": sorted(ALLOWED_UI),
        "synthModules": SYNTH_MODULES,
        "modSources": MOD_SOURCES,
    },
    "paramGlossary": gl,
    "levels": levels,
    "recipes": recipes,
    "genres": genres,
}
path = sys.argv[1]
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
n_les = sum(len(m["lessons"]) for lv in levels for m in lv["modules"])
n_mod = sum(len(lv["modules"]) for lv in levels)
n_steps = sum(len(l["steps"]) for lv in levels for m in lv["modules"] for l in m["lessons"])
n_unv = [l["id"] for lv in levels for m in lv["modules"] for l in m["lessons"] if l["unverified"]]
print(f"levels={len(levels)} modules={n_mod} lessons={n_les} steps={n_steps} recipes={len(recipes)} genres={len(genres)} params={len(gl)} unverifiedLessons={len(n_unv)}")
for lv in levels:
    print(lv["id"], sum(len(m["lessons"]) for m in lv["modules"]), "lessons", sum(l["estimatedMinutes"] for m in lv["modules"] for l in m["lessons"]), "min")
print("UNVERIFIED:", ", ".join(n_unv))

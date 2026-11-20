# -*- coding: utf-8 -*-
"""Param glossary for the LearnSerum trainer. id -> {label, min, max, unit, default, enum?, kind, unverified?}"""

RATE_SYNC = ["8 тактов", "4 такта", "2 такта", "1 такт", "1/2", "1/4", "1/4D", "1/4T",
             "1/8", "1/8D", "1/8T", "1/16", "1/16D", "1/16T", "1/32"]
# index helpers
RS = {name: i for i, name in enumerate(["8bar", "4bar", "2bar", "1bar", "1/2", "1/4", "1/4D", "1/4T",
                                         "1/8", "1/8D", "1/8T", "1/16", "1/16D", "1/16T", "1/32"])}

TABLES = ["Basic Shapes (синус → треугольник → пила → квадрат)", "Analog (аналоговые формы)",
          "Digital (цифровые/резкие кадры)", "Formant / Vowel (гласные)", "Growl (рычащие кадры)",
          "Pulse Width (меандр → узкий импульс)", "User (нарисованная/импортированная)"]

WARPS = ["Off", "Sync", "Bend+", "Bend-", "Bend+/-", "PWM", "Asym+", "Asym-", "Asym+/-", "Flip",
         "Mirror", "Quantize", "FM (от источника)", "AM (от источника)", "RM (от источника)",
         "PD — фазовое искажение (Serum 2)", "Wavefold / Distortion warp (Serum 2)"]
W = {n: i for i, n in enumerate(["off", "sync", "bend+", "bend-", "bend+-", "pwm", "asym+", "asym-", "asym+-",
                                  "flip", "mirror", "quantize", "fm", "am", "rm", "pd", "fold"])}

WARP_SRC = ["нет", "OSC A", "OSC B", "OSC C", "SUB", "NOISE"]
WS = {"none": 0, "osc-a": 1, "osc-b": 2, "osc-c": 3, "sub": 4, "noise": 5}

ENGINES = ["Wavetable", "Multisample (SFZ)", "Sample", "Granular", "Spectral"]

SHAPES = ["синус", "треугольник", "пила", "квадрат", "другая форма"]
SH = {"sine": 0, "tri": 1, "saw": 2, "square": 3, "other": 4}

SUB_SHAPES = ["синус", "скруглённый прямоугольник", "треугольник", "пила", "квадрат", "импульс"]

NOISE_TYPES = ["белый шум", "розовый шум", "винил / треск", "ударный one-shot (клик)", "текстура / атмосфера"]

FILTER_TYPES = ["Low 12", "Low 24", "MG Low 12", "MG Low 24", "High 12", "High 24", "Band 12", "Band 24",
                "Peak 12", "Notch 12", "Comb+", "Comb-", "Flanger", "Phaser", "Formant", "Low 6",
                "Ladder / Acid", "SampHold", "Ring Mod", "Scream", "DJ Mixer", "Add Bass"]
F = {n: i for i, n in enumerate(["low12", "low24", "mglow12", "mglow24", "high12", "high24", "band12", "band24",
                                  "peak12", "notch12", "comb+", "comb-", "flanger", "phaser", "formant", "low6",
                                  "ladder", "samphold", "ringmod", "scream", "djmixer", "addbass"])}

LFO_SHAPES = ["синус", "треугольник", "пила вниз", "пила вверх (рамп)", "квадрат", "S&H / случайный",
              "нарисованная (custom)", "Chaos: Lorenz (Serum 2)", "Chaos: Rössler (Serum 2)", "Path X/Y (Serum 2)"]
LS = {n: i for i, n in enumerate(["sine", "tri", "sawdown", "rampup", "square", "sh", "custom", "lorenz", "rossler", "path"])}

LFO_MODES = ["Free (Off — без перезапуска)", "Trig (перезапуск на каждую ноту)", "Env (однократно, как огибающая)"]
LM = {"free": 0, "trig": 1, "env": 2}

DIST_MODES = ["Tube", "SoftClip", "HardClip", "Diode 1", "Diode 2", "Linear Fold", "Sine Fold", "Zero-Square",
              "Downsample", "Asym", "Rectify", "X-Shaper", "X-Shaper (Asym)", "Overdrive (Serum 2)"]
D = {n: i for i, n in enumerate(["tube", "softclip", "hardclip", "diode1", "diode2", "linfold", "sinfold", "zerosquare",
                                  "downsample", "asym", "rectify", "xshaper", "xshaperasym", "overdrive"])}

REVERB_TYPES = ["Plate", "Hall", "Vintage (Serum 2)", "Nitrous (Serum 2)", "Basin (Serum 2)"]
DELAY_MODES = ["Normal", "Ping-Pong", "Tap → Delay"]
TABS = ["OSC", "MIX", "FX", "MATRIX", "GLOBAL", "ARP", "CLIP"]
TAB = {n: i for i, n in enumerate(["osc", "mix", "fx", "matrix", "global", "arp", "clip"])}
ROUTE = ["мимо фильтров", "Filter 1", "Filter 2", "Filter 1 + Filter 2"]
BUS = ["Main", "FX Bus 1", "FX Bus 2"]
ARP_MODES = ["Up", "Down", "Up/Down", "Random", "As Played", "Pattern"]
UNISON_MODES = ["Linear", "Super", "Exp", "Inv", "Random"]
SPLITTERS = ["нет", "Splitter L/H", "Splitter L/M/H", "Splitter M/S"]


def p(label, mn=None, mx=None, unit="", default=None, enum=None, kind="continuous", unverified=False, note=None, readonly=False):
    d = {"label": label}
    if enum is not None:
        d["kind"] = "enum"
        d["enum"] = enum
        d["min"] = 0
        d["max"] = len(enum) - 1
    else:
        d["kind"] = kind
        if mn is not None:
            d["min"] = mn
        if mx is not None:
            d["max"] = mx
    if unit:
        d["unit"] = unit
    if default is not None:
        d["default"] = default
    if readonly:
        d["readonly"] = True
    if unverified:
        d["unverified"] = True
    if note:
        d["note"] = note
    return d


def build_glossary():
    g = {}
    # ---------- main oscillators
    for osc, name, dflt_on in (("osc-a", "OSC A", 1), ("osc-b", "OSC B", 0), ("osc-c", "OSC C", 0)):
        uv = osc == "osc-c"
        g[f"{osc}.enabled"] = p(f"{name}: включён", 0, 1, default=dflt_on, kind="toggle", unverified=uv)
        g[f"{osc}.mode"] = p(f"{name}: тип движка", enum=ENGINES, default=0, unverified=True,
                             note="Пять движков подтверждены Xfer; в тренажёре полноценно реализован только Wavetable.")
        g[f"{osc}.table"] = p(f"{name}: выбранная волновая таблица", enum=TABLES, default=0)
        g[f"{osc}.wtPos"] = p(f"{name}: позиция в таблице (WT POS)", 0, 1, default=0.67,
                              note="В таблице Basic Shapes кадры стоят так: 0 = синус, 0.33 = треугольник, 0.67 = пила, 1 = квадрат.")
        g[f"{osc}.shape"] = p(f"{name}: распознанная форма волны (вычисляется)", enum=SHAPES, readonly=True,
                              note="Производный параметр: приложение считает его из table=0 и ближайшего кадра wtPos (допуск ±0.05). Иначе 4.")
        g[f"{osc}.interp"] = p(f"{name}: плавная интерполяция кадров (Smooth)", 0, 1, default=0, kind="toggle", unverified=True)
        g[f"{osc}.octave"] = p(f"{name}: октава (OCT)", -4, 4, "oct", 0, kind="int")
        g[f"{osc}.semi"] = p(f"{name}: полутоны (SEM)", -12, 12, "st", 0, kind="int")
        g[f"{osc}.fine"] = p(f"{name}: точная подстройка (FIN)", -100, 100, "cent", 0)
        g[f"{osc}.coarse"] = p(f"{name}: грубая высота (CRS), непрерывная", -64, 64, "st", 0, unverified=True,
                               note="Цель для модуляции высоты (питч-огибающие). Диапазон взят из Serum 1.")
        g[f"{osc}.unison"] = p(f"{name}: число голосов унисона", 1, 16, "voices", 1, kind="int")
        g[f"{osc}.detune"] = p(f"{name}: расстройка унисона (DETUNE)", 0, 1, default=0.25)
        g[f"{osc}.blend"] = p(f"{name}: баланс центр/боковые голоса (BLEND)", 0, 100, "%", 75)
        g[f"{osc}.width"] = p(f"{name}: стерео-ширина унисона", 0, 100, "%", 100, unverified=True)
        g[f"{osc}.phase"] = p(f"{name}: начальная фаза (PHASE)", 0, 360, "deg", 0)
        g[f"{osc}.rand"] = p(f"{name}: случайность фазы (RAND)", 0, 100, "%", 100)
        g[f"{osc}.pan"] = p(f"{name}: панорама", -100, 100, "%", 0)
        g[f"{osc}.level"] = p(f"{name}: громкость (LEVEL)", 0, 100, "%", 75)
        g[f"{osc}.warp"] = p(f"{name}: режим варпа (слот 1)", enum=WARPS, default=0)
        g[f"{osc}.warpAmt"] = p(f"{name}: глубина варпа (слот 1)", 0, 100, "%", 0)
        g[f"{osc}.warpSource"] = p(f"{name}: источник для FM/AM/RM варпа", enum=WARP_SRC, default=0)
        g[f"{osc}.warp2"] = p(f"{name}: режим варпа (слот 2, Dual Warp)", enum=WARPS, default=0, unverified=True)
        g[f"{osc}.warp2Amt"] = p(f"{name}: глубина варпа (слот 2)", 0, 100, "%", 0, unverified=True)
        g[f"{osc}.sampleStart"] = p(f"{name}: старт сэмпла (Sample)", 0, 100, "%", 0, unverified=True)
        g[f"{osc}.loop"] = p(f"{name}: петля сэмпла (Sample)", 0, 1, default=0, kind="toggle", unverified=True)
        g[f"{osc}.grainLength"] = p(f"{name}: длина зерна (Granular)", 1, 1000, "ms", 80, unverified=True)
        g[f"{osc}.grainDensity"] = p(f"{name}: плотность / число зёрен (Granular)", 1, 256, "grains", 16, kind="int", unverified=True,
                                     note="Подтверждено: до 256 зёрен. Точная шкала регулятора не подтверждена.")
        g[f"{osc}.scanRate"] = p(f"{name}: скорость сканирования (Granular/Spectral)", -200, 200, "%", 100, unverified=True)
        g[f"{osc}.grainRandom"] = p(f"{name}: случайное смещение зёрен", 0, 100, "%", 0, unverified=True)
        g[f"{osc}.timbreShift"] = p(f"{name}: сдвиг тембра (Spectral)", -100, 100, "%", 0, unverified=True)
    # ---------- sub / noise
    g["sub.enabled"] = p("SUB: включён", 0, 1, default=0, kind="toggle")
    g["sub.shape"] = p("SUB: форма", enum=SUB_SHAPES, default=0)
    g["sub.octave"] = p("SUB: октава", -4, 4, "oct", 0, kind="int")
    g["sub.directOut"] = p("SUB: Direct Out (мимо фильтра и FX)", 0, 1, default=0, kind="toggle", unverified=True,
                           note="Поведение взято из Serum 1; в Serum 2 маршрут задаётся также на странице MIX.")
    g["sub.pan"] = p("SUB: панорама", -100, 100, "%", 0)
    g["sub.level"] = p("SUB: громкость", 0, 100, "%", 75)
    g["noise.enabled"] = p("NOISE: включён", 0, 1, default=0, kind="toggle")
    g["noise.type"] = p("NOISE: тип шума/сэмпла", enum=NOISE_TYPES, default=0)
    g["noise.oneShot"] = p("NOISE: однократное проигрывание (One-shot)", 0, 1, default=0, kind="toggle")
    g["noise.keyTrack"] = p("NOISE: следование высоте ноты", 0, 1, default=0, kind="toggle")
    g["noise.pitch"] = p("NOISE: высота/скорость", 0, 100, "%", 50)
    g["noise.pan"] = p("NOISE: панорама", -100, 100, "%", 0)
    g["noise.level"] = p("NOISE: громкость", 0, 100, "%", 25)
    # ---------- filters
    for fid, name, uv in (("filter", "Filter 1", False), ("filter2", "Filter 2 (Serum 2)", True)):
        g[f"{fid}.enabled"] = p(f"{name}: включён", 0, 1, default=0, kind="toggle", unverified=uv)
        g[f"{fid}.type"] = p(f"{name}: тип", enum=FILTER_TYPES, default=0, unverified=True,
                             note="Полный список типов Serum 2 не подтверждён руководством; набор — проверенное ядро + типы из обзоров.")
        g[f"{fid}.cutoff"] = p(f"{name}: частота среза (CUTOFF)", 8, 22000, "Hz", 22000, kind="log")
        g[f"{fid}.res"] = p(f"{name}: резонанс (RES)", 0, 100, "%", 10)
        g[f"{fid}.drive"] = p(f"{name}: перегруз (DRIVE)", 0, 100, "%", 0)
        g[f"{fid}.mix"] = p(f"{name}: dry/wet (MIX)", 0, 100, "%", 100)
        g[f"{fid}.keytrack"] = p(f"{name}: кей-трекинг среза", 0, 100, "%", 0)
        g[f"{fid}.pan"] = p(f"{name}: панорама", -100, 100, "%", 0)
    # ---------- envelopes
    for n in range(1, 5):
        uv = False  # 4 огибающие подтверждены Xfer
        role = " (жёстко на громкость)" if n == 1 else ""
        g[f"env{n}.attack"] = p(f"ENV {n}{role}: атака", 0, 32000, "ms", 0.5 if n == 1 else 0, kind="log", unverified=uv)
        g[f"env{n}.hold"] = p(f"ENV {n}: удержание (HOLD)", 0, 32000, "ms", 0, kind="log", unverified=uv)
        g[f"env{n}.decay"] = p(f"ENV {n}: спад (DECAY)", 0, 32000, "ms", 1000, kind="log", unverified=uv)
        g[f"env{n}.sustain"] = p(f"ENV {n}: уровень сустейна (SUSTAIN)", 0, 100, "%", 100 if n == 1 else 0, unverified=uv,
                                 note="100 % = 0 dB, 0 % = −∞ dB. Serum показывает сустейн ENV 1 в децибелах.")
        g[f"env{n}.release"] = p(f"ENV {n}: затухание (RELEASE)", 0, 32000, "ms", 15, kind="log", unverified=uv)
        g[f"env{n}.attackCurve"] = p(f"ENV {n}: кривизна атаки", -100, 100, "%", 0, unverified=True)
        g[f"env{n}.decayCurve"] = p(f"ENV {n}: кривизна спада", -100, 100, "%", 0, unverified=True)
    # ---------- LFOs
    for n in range(1, 11):
        uv = False  # до 10 LFO подтверждено Xfer (7–10 появляются после назначения LFO 6)
        g[f"lfo{n}.shape"] = p(f"LFO {n}: форма", enum=LFO_SHAPES, default=0, unverified=uv)
        g[f"lfo{n}.mode"] = p(f"LFO {n}: режим запуска", enum=LFO_MODES, default=1, unverified=uv)
        g[f"lfo{n}.sync"] = p(f"LFO {n}: синхронизация с темпом (BPM)", 0, 1, default=1, kind="toggle", unverified=uv)
        g[f"lfo{n}.rateSync"] = p(f"LFO {n}: скорость в долях такта", enum=RATE_SYNC, default=5, unverified=uv)
        g[f"lfo{n}.rate"] = p(f"LFO {n}: скорость в Гц (без синхронизации)", 0.01, 1000, "Hz", 2, kind="log", unverified=uv,
                              note="Serum 2 допускает до 1000 Гц через множитель ×10 (подтверждено Xfer).")
        g[f"lfo{n}.delay"] = p(f"LFO {n}: задержка старта (DELAY)", 0, 8000, "ms", 0, unverified=uv)
        g[f"lfo{n}.rise"] = p(f"LFO {n}: плавное нарастание (RISE)", 0, 8000, "ms", 0, unverified=uv)
        g[f"lfo{n}.smooth"] = p(f"LFO {n}: сглаживание (SMOOTH)", 0, 100, "%", 0, unverified=uv)
        g[f"lfo{n}.phase"] = p(f"LFO {n}: начальная фаза", 0, 360, "deg", 0, unverified=uv)
    # ---------- macros
    for n in range(1, 9):
        g[f"macro{n}"] = p(f"Макрос {n}: положение", 0, 100, "%", 0)
    # ---------- voicing / global
    g["voicing.mono"] = p("Моно-режим", 0, 1, default=0, kind="toggle")
    g["voicing.legato"] = p("Легато (без перезапуска огибающих)", 0, 1, default=0, kind="toggle")
    g["voicing.polyphony"] = p("Полифония (макс. голосов)", 1, 32, "voices", 8, kind="int", unverified=True)
    g["voicing.porta"] = p("Портаменто / глайд (PORTA)", 0, 2000, "ms", 0, kind="log")
    g["voicing.portaAlways"] = p("Портаменто всегда (не только в легато)", 0, 1, default=0, kind="toggle")
    g["voicing.portaScaled"] = p("Портаменто масштабируется по интервалу", 0, 1, default=0, kind="toggle", unverified=True)
    g["voicing.bendUp"] = p("Диапазон pitch bend вверх", 0, 48, "st", 2, kind="int", unverified=True)
    g["voicing.bendDown"] = p("Диапазон pitch bend вниз", 0, 48, "st", 2, kind="int", unverified=True)
    g["voicing.unisonMode"] = p("Режим распределения расстройки унисона", enum=UNISON_MODES, default=0, unverified=True)
    g["voicing.quality"] = p("Качество / оверсэмплинг", enum=["Normal", "High", "High (offline)"], default=0, unverified=True)
    g["master.volume"] = p("Мастер-громкость", 0, 100, "%", 70)
    # ---------- mixer (Serum 2 MIX page)
    for ch, name in (("osc-a", "OSC A"), ("osc-b", "OSC B"), ("osc-c", "OSC C"), ("sub", "SUB"), ("noise", "NOISE")):
        g[f"mixer.{ch}.route"] = p(f"MIX: {name} → фильтр", enum=ROUTE, default=1 if ch == "osc-a" else 0, unverified=True)
        g[f"mixer.{ch}.bus"] = p(f"MIX: {name} → шина", enum=BUS, default=0, unverified=True)
    for ch, name in (("filter", "Filter 1"), ("filter2", "Filter 2")):
        g[f"mixer.{ch}.bus"] = p(f"MIX: выход {name} → шина", enum=BUS, default=0, unverified=True)
    g["mixer.filterRouting"] = p("MIX: соединение фильтров", enum=["последовательно", "параллельно"], default=0)
    g["mixer.bus1.level"] = p("MIX: уровень FX Bus 1", 0, 100, "%", 75, unverified=True)
    g["mixer.bus2.level"] = p("MIX: уровень FX Bus 2", 0, 100, "%", 75, unverified=True)
    # ---------- FX
    def fxp(unit, name, params, uv=False):
        g[f"fx.{unit}.enabled"] = p(f"FX {name}: включён", 0, 1, default=0, kind="toggle", unverified=uv)
        for key, args in params.items():
            lab, rest = args[0], args[1:]
            if isinstance(rest[0], list):
                g[f"fx.{unit}.{key}"] = p(f"FX {name}: {lab}", enum=rest[0], unverified=uv)
            elif rest[0] == 0 and rest[1] == 1 and rest[2] == "":
                g[f"fx.{unit}.{key}"] = p(f"FX {name}: {lab}", 0, 1, default=rest[3], kind="toggle", unverified=uv)
            else:
                g[f"fx.{unit}.{key}"] = p(f"FX {name}: {lab}", *rest, unverified=uv)

    fxp("hyper", "Hyper/Dimension", {"rate": ("скорость", 0, 100, "%", 40), "detune": ("расстройка", 0, 100, "%", 25),
                                     "unison": ("голоса", 1, 7, "voices", 4), "mix": ("dry/wet Hyper", 0, 100, "%", 50),
                                     "dimSize": ("размер Dimension", 0, 100, "%", 50), "dimMix": ("dry/wet Dimension", 0, 100, "%", 0)})
    fxp("distortion", "Distortion", {"mode": ("режим", DIST_MODES), "drive": ("драйв", 0, 100, "%", 25),
                                     "mix": ("dry/wet", 0, 100, "%", 100),
                                     "prePost": ("фильтр до/после", ["выкл", "Pre", "Post"]),
                                     "filterFreq": ("частота встроенного фильтра", 20, 20000, "Hz", 1000),
                                     "bias": ("DC bias (Serum 2)", -100, 100, "%", 0)})
    fxp("flanger", "Flanger", {"rate": ("скорость", 0, 20, "Hz", 0.5), "depth": ("глубина", 0, 100, "%", 50),
                               "feedback": ("обратная связь", 0, 100, "%", 50), "mix": ("dry/wet", 0, 100, "%", 50)})
    fxp("phaser", "Phaser", {"rate": ("скорость", 0, 20, "Hz", 0.5), "depth": ("глубина", 0, 100, "%", 50),
                             "freq": ("частота", 20, 20000, "Hz", 800), "feedback": ("обратная связь", 0, 100, "%", 30),
                             "mix": ("dry/wet", 0, 100, "%", 50)})
    fxp("chorus", "Chorus", {"rate": ("скорость", 0, 20, "Hz", 0.8), "depth": ("глубина", 0, 100, "%", 30),
                             "feedback": ("обратная связь", 0, 100, "%", 0), "mix": ("dry/wet", 0, 100, "%", 50)})
    fxp("delay", "Delay", {"mode": ("режим", DELAY_MODES), "sync": ("синхронизация", 0, 1, "", 1),
                           "timeSync": ("время в долях", RATE_SYNC), "time": ("время в мс", 1, 2000, "ms", 375),
                           "feedback": ("обратная связь", 0, 100, "%", 40), "mix": ("dry/wet", 0, 100, "%", 25),
                           "hpf": ("срез низов в повторах", 20, 20000, "Hz", 200), "lpf": ("срез верхов в повторах", 20, 20000, "Hz", 8000)})
    fxp("compressor", "Compressor", {"threshold": ("порог", -60, 0, "dB", -12), "ratio": ("соотношение", 1, 20, ":1", 4),
                                     "attack": ("атака", 0.1, 200, "ms", 5), "release": ("восстановление", 5, 1000, "ms", 100),
                                     "gain": ("компенсация усиления", -12, 30, "dB", 0), "mix": ("dry/wet", 0, 100, "%", 100),
                                     "multiband": ("многополосный режим (OTT-стиль)", 0, 1, "", 0)})
    fxp("reverb", "Reverb", {"type": ("тип", REVERB_TYPES), "size": ("размер", 0, 100, "%", 50),
                             "decay": ("время затухания", 0.1, 30, "s", 2), "predelay": ("предзадержка", 0, 500, "ms", 0),
                             "damp": ("демпфирование верхов", 0, 100, "%", 50), "width": ("ширина", 0, 100, "%", 100),
                             "lowcut": ("срез низов", 20, 2000, "Hz", 100), "highcut": ("срез верхов", 1000, 20000, "Hz", 12000),
                             "mix": ("dry/wet", 0, 100, "%", 20)})
    fxp("eq", "EQ", {"lowType": ("тип нижней полосы", ["Shelf", "Peak", "High-pass"]),
                     "lowFreq": ("частота нижней полосы", 20, 20000, "Hz", 200), "lowGain": ("усиление нижней полосы", -24, 24, "dB", 0),
                     "lowQ": ("добротность нижней полосы", 0.1, 10, "Q", 0.7),
                     "highType": ("тип верхней полосы", ["Shelf", "Peak", "Low-pass"]),
                     "highFreq": ("частота верхней полосы", 20, 20000, "Hz", 5000), "highGain": ("усиление верхней полосы", -24, 24, "dB", 0),
                     "highQ": ("добротность верхней полосы", 0.1, 10, "Q", 0.7)})
    fxp("filter", "Filter (эффект)", {"type": ("тип", FILTER_TYPES), "cutoff": ("срез", 8, 22000, "Hz", 22000),
                                      "res": ("резонанс", 0, 100, "%", 0), "drive": ("драйв", 0, 100, "%", 0),
                                      "mix": ("dry/wet", 0, 100, "%", 100)})
    fxp("bode", "Bode (частотный сдвиг, Serum 2)", {"shift": ("сдвиг частоты", -2000, 2000, "Hz", 0),
                                                     "mix": ("dry/wet", 0, 100, "%", 50)}, uv=True)
    fxp("convolve", "Convolve (свёртка, Serum 2)", {"ir": ("импульс", ["комната", "зал", "кабинет гитары", "винил", "пружина"]),
                                                    "mix": ("dry/wet", 0, 100, "%", 30)}, uv=True)
    fxp("utility", "Utility (Serum 2)", {"monoBass": ("моно ниже частоты", 0, 1, "", 0),
                                         "monoFreq": ("частота моно-баса", 40, 500, "Hz", 120),
                                         "width": ("ширина", 0, 200, "%", 100), "pan": ("панорама", -100, 100, "%", 0),
                                         "hpf": ("high-pass", 20, 2000, "Hz", 20), "lpf": ("low-pass", 1000, 22000, "Hz", 22000),
                                         "gain": ("усиление", -24, 24, "dB", 0)}, uv=True)
    fxp("splitter", "Splitter (Serum 2)", {"type": ("тип", SPLITTERS), "crossover": ("частота раздела", 40, 8000, "Hz", 150)}, uv=True)
    # ---------- arp / clip
    g["arp.enabled"] = p("ARP: включён", 0, 1, default=0, kind="toggle")
    g["arp.mode"] = p("ARP: порядок нот", enum=ARP_MODES, default=0, unverified=True)
    g["arp.rateSync"] = p("ARP: длительность шага", enum=RATE_SYNC, default=11, unverified=True)
    g["arp.octaves"] = p("ARP: диапазон октав", 1, 4, "oct", 1, kind="int", unverified=True)
    g["arp.gate"] = p("ARP: длина ноты (GATE)", 1, 100, "%", 50)
    g["arp.chance"] = p("ARP: вероятность шага (CHANCE)", 0, 100, "%", 100)
    g["arp.swing"] = p("ARP/клавиатура: свинг", 0, 100, "%", 0)
    g["arp.slot"] = p("ARP: выбранный слот паттерна", 1, 12, "", 1, kind="int")
    g["clip.enabled"] = p("CLIP: воспроизведение клипа", 0, 1, default=0, kind="toggle")
    g["clip.slot"] = p("CLIP: выбранный слот клипа", 1, 12, "", 1, kind="int")
    g["kbd.scaleLock"] = p("Клавиатура: привязка к ладу (Key/Scale)", 0, 1, default=0, kind="toggle")
    g["kbd.transpose"] = p("Клавиатура: транспонирование", -12, 12, "st", 0, kind="int")
    # ---------- wavetable editor
    g["wte.open"] = p("Редактор таблиц открыт", 0, 1, default=0, kind="toggle")
    g["wte.view"] = p("Редактор: режим", enum=["волна (рисование)", "FFT / гармоники", "формула"], default=0)
    g["wte.frames"] = p("Редактор: число кадров", 1, 256, "frames", 1, kind="int")
    g["wte.h{n}"] = p("Редактор (FFT): амплитуда гармоники n (n = 1…64)", 0, 100, "%", 0, kind="pattern",
                      note="Шаблон: wte.h1 … wte.h64. h1 — основной тон.")
    g["wte.harmonicCount"] = p("Редактор: число ненулевых гармоник (вычисляется)", 0, 64, "", 1, kind="int", readonly=True)
    # ---------- views / meters / ui (read-only state)
    g["view.tab"] = p("Открытая вкладка синта", enum=TABS, default=0)
    g["view.analyzer"] = p("Анализатор", enum=["выкл", "осциллограф", "спектр", "оба"], default=0)
    g["view.mono"] = p("Кнопка проверки в моно", 0, 1, default=0, kind="toggle")
    g["view.phoneSim"] = p("Симуляция динамика телефона (HPF ~150 Гц)", 0, 1, default=0, kind="toggle")
    g["kbd.lastNote"] = p("Последняя сыгранная нота (MIDI-номер)", 0, 127, "midi", 60, kind="int", readonly=True,
                          note="A4 = 69, C4 = 60, A1 = 33, E1 = 28.")
    g["kbd.notesHeld"] = p("Сколько нот зажато сейчас", 0, 16, "", 0, kind="int", readonly=True)
    g["meter.peakDb"] = p("Пиковый уровень на выходе", -96, 12, "dBFS", -96, readonly=True)
    g["meter.lufsShort"] = p("Краткосрочная громкость (3 с)", -70, 0, "LUFS", -70, readonly=True)
    g["meter.clipCount"] = p("Сколько раз выход перегрузился (>0 dBFS)", 0, 99999, "", 0, kind="int", readonly=True)
    g["mod.count"] = p("Число активных модуляций в матрице", 0, 64, "", 0, kind="int", readonly=True)
    g["ui.initCount"] = p("Сколько раз нажат Init", 0, 999, "", 0, kind="int", readonly=True)
    g["ui.presetSaves"] = p("Сколько раз сохранён пресет", 0, 999, "", 0, kind="int", readonly=True)
    g["ui.undoCount"] = p("Сколько раз использован Undo", 0, 999, "", 0, kind="int", readonly=True)
    g["ui.presetLoads"] = p("Сколько пресетов загружено из браузера", 0, 999, "", 0, kind="int", readonly=True)
    g["fx.orderIndex.{unit}"] = p("Позиция эффекта в цепочке (0 = первый); −1 если не в цепочке", -1, 20, "", -1,
                                  kind="pattern", readonly=True, note="Шаблон: fx.orderIndex.distortion и т. п.")
    g["mod:{source}->{dest}"] = p("Глубина модуляции источника на параметр", -100, 100, "%", 0, kind="pattern",
                                  note="Шаблон маршрута матрицы. Глубина в % от полного диапазона цели; 0 = маршрута нет. "
                                       "Источники: env2–env4, lfo1–lfo10, macro1–macro8, velocity, note, modwheel, pitchbend, "
                                       "aftertouch, noteon-rand1, noteon-rand2. Для osc-*.coarse (±64 st, размах 128 st) 1 % ≈ 1.28 st.")
    g["modaux:{source}->{dest}"] = p("Aux-источник маршрута (масштабирует глубину)", enum=["нет", "velocity", "modwheel", "macro1", "macro2", "lfo1", "env2"],
                                     kind="pattern", note="Шаблон: modaux:lfo1->osc-a.wtPos")
    g["modaux:{source}->{dest}"]["kind"] = "pattern"
    return g


MOD_SOURCES = (["env2", "env3", "env4"] + [f"lfo{i}" for i in range(1, 11)] + [f"macro{i}" for i in range(1, 9)]
               + ["velocity", "note", "modwheel", "pitchbend", "aftertouch", "noteon-rand1", "noteon-rand2"])

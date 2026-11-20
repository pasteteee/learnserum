# LearnSerum: учебная программа (curriculum.json)

Данные курса для веб-приложения `pasteteee/learnserum`. Слева тренажёр в стиле Serum 2, справа уроки. Весь текст для пользователя на русском языке. Идентификаторы написаны на английском в kebab-case.

- `curriculum.json` — сам датасет, сгенерирован автоматически, вручную не редактируется.
- `generator/` — Python-скрипты, из которых он собирается. Сборка запускается так: `cd generator && python3 build.py ../curriculum.json`. Скрипт проверяет ссылки, параметры и диапазоны и при ошибке ничего не записывает.

Объём: **6 уровней, 29 модулей, 90 уроков, 278 проверяемых шагов, 32 рецепта, 8 жанров, 394 параметра в глоссарии.**

| Уровень | Уроков | Содержание |
|---|---|---|
| 0. Теория звука | 12 | волна, частота, дБ, гармоники, фаза, полосы, психоакустика, стерео/Хаас, алиасинг, ноты↔Гц, центы |
| 1. Основы синтеза | 20 | осцилляторы, фильтр, ADSR, огибающие фильтра и высоты, LFO, velocity, моно/глайд, унисон, базовые FX, проект «4 звука» |
| 2. Интерфейс Serum один-в-один | 15 | шапка/INIT/браузер, OSC A/B/C, унисон, SUB/NOISE, 2 фильтра и маршрутизация, drag-and-drop модуляция, ENV/LFO/MATRIX/макросы, FX-рэк, GLOBAL/MIX |
| 3. Продвинутый Serum 2 | 15 | варпы, FM/AM/RM, Dual Warp, редактор таблиц, ресэмплинг, aux/кривые, хаос/path LFO, Sample/Granular/Spectral, FX-шины, сплиттеры, Utility/Bode/Convolve, гейн-стейджинг, ARP/CLIP |
| 4. Саунд-дизайн | 18 | лиды → плаки/пэды/FX → басы (саб, 808, рис, вобл, гроул, рыдим) → хайперпоп → хардстайл (бочка, реверс-бас, эйфорик, скрич, роу) |
| 5. Продакшн | 10 | ритм, гармония, аранжировка, сайдчейн, сведение, мастеринг/LUFS, 4 финальных проекта по жанрам |

## Схема

```
{ version, title, language, conventions, paramGlossary,
  levels[]  { id, order, title, description, estimatedHours,
    modules[] { id, order, title, description, prerequisites[moduleId],
      lessons[] { id, order, title, summary, theory[], goals[], concepts[],
                  prerequisites[lessonId], estimatedMinutes, difficulty(1–5),
                  synthModules[], steps[], exercises[], unverified,
                  unverifiedNote?, recipeIds? } } },
  recipes[] { id, name, category, genre[], difficulty, lessonId, summary,
              patch{param:value}, fxChain[], commonMistakes[], basis },
  genres[]  { id, name, bpm[min,max], keys, structure[{section,bars}],
              keyElements[], mixTips[], loudnessNote, sourceNote, unverified } }
```

Поля сверх заданной схемы. Все они необязательные, приложение может их не читать.

- `lesson.theory[]` — 1–3 абзаца теории для правой панели.
- `lesson.unverifiedNote` — что именно в уроке не подтверждено.
- `lesson.recipeIds` — какие рецепты разбираются в уроке (только уровень 4).
- `recipe.basis` — `cited` (опирается на найденный источник) или `practice` (обычная стартовая точка практиков).
- `genre.sourceNote` и `genre.unverified` — откуда взяты цифры по жанру и насколько они надёжны.
- `conventions` — договорённости для движка: кадры Basic Shapes, единицы модуляции, допуски проверок, разрешённые id подсветки, список источников модуляции.

Пререквизиты по умолчанию идут по порядку: урок зависит от предыдущего урока, модуль — от предыдущего модуля. Первые уроки и модули каждого уровня ссылаются на последний урок или модуль предыдущего уровня. Ссылки вперёд генератор не пропускает.

## Схема именования параметров

Формат: `<модуль>.<параметр>`, параметр в camelCase. Все id с диапазонами, единицами, значениями по умолчанию и enum-списками собраны в `paramGlossary`. Значения enum — это индексы в массиве `enum`.

| Префикс | Что это |
|---|---|
| `osc-a.*`, `osc-b.*`, `osc-c.*` | `enabled, mode, table, wtPos, shape*, interp, octave, semi, fine, coarse, unison, detune, blend, width, phase, rand, pan, level, warp, warpAmt, warpSource, warp2, warp2Amt`, а также параметры Sample/Granular/Spectral |
| `sub.*`, `noise.*` | саб и шумовой генератор |
| `filter.*`, `filter2.*` | Filter 1 и Filter 2: `type, cutoff (Гц, log), res, drive, mix, keytrack, pan` |
| `env1…env4.*` | `attack, hold, decay, release` (мс), `sustain` (%: 100 = 0 дБ), `attackCurve, decayCurve` |
| `lfo1…lfo10.*` | `shape, mode (Free/Trig/Env), sync, rateSync (enum долей), rate (Гц), delay, rise, smooth, phase` |
| `macro1…macro8` | положение макроса, 0–100 % |
| `voicing.*`, `master.volume` | моно, легато, портаменто, pitch bend, режим унисона, качество |
| `mixer.*` | страница MIX: `mixer.<источник>.route` (фильтр), `mixer.<источник>.bus`, `mixer.filterRouting` |
| `fx.<unit>.*` | `hyper, distortion, flanger, phaser, chorus, delay, compressor, reverb, eq, filter, bode, convolve, utility, splitter`; у каждого есть `.enabled` |
| `arp.*`, `clip.*`, `kbd.*` | арпеджиатор, клипы, клавиатура (`kbd.scaleLock`, `kbd.transpose`) |
| `wte.*` | редактор таблиц: `open, view, frames`, гармоники `wte.h1…wte.h64` |
| `view.*` | состояние интерфейса: `tab, analyzer, mono, phoneSim` |

Шаблонные и вычисляемые параметры. В глоссарии они помечены `kind: "pattern"` или `readonly: true`.

- `mod:<source>-><dest>` — глубина маршрута в матрице, −100…100 % от полного диапазона цели; 0 значит, что маршрута нет. Список допустимых источников лежит в `conventions.modSources`. Для `osc-*.coarse` (±64 полутона) 1 % ≈ 1.28 полутона: +24 st ≈ 18.8 %, +48 st ≈ 37.5 %.
- `modaux:<source>-><dest>` — индекс aux-источника маршрута.
- `osc-*.shape` — производное значение. Приложение вычисляет его из `table = 0` (Basic Shapes) и ближайшего кадра `wtPos` (0 / 0.33 / 0.67 / 1 → синус / треугольник / пила / квадрат, допуск ±0.05); в остальных случаях значение 4.
- `fx.orderIndex.<unit>` — позиция эффекта в цепочке: 0 — первый, −1 — эффект не в цепочке.
- `kbd.lastNote`, `kbd.notesHeld` — последняя сыгранная нота (MIDI) и число зажатых нот.
- `meter.peakDb`, `meter.lufsShort`, `meter.clipCount` — показания измерителей на выходе.
- `mod.count` — число активных маршрутов в матрице.
- `ui.initCount`, `ui.presetSaves`, `ui.presetLoads`, `ui.undoCount` — счётчики действий пользователя за урок.

`step.highlight` содержит id параметра, id панели из `synthModules` или id элемента интерфейса из `conventions.uiHighlightIds` (`keyboard`, `meter`, `init-button`, `save-button`, `undo-button`, `preset-browser`, `tab-*`, `osc-a.edit`, `matrix-row`, `env1…4` и т. д.).

## Как приложение должно проверять шаги

1. При открытии урока приложение сбрасывает счётчики `ui.*` и `meter.clipCount`. Панели, которых нет в `synthModules`, затемняются или блокируются, как в Syntorial.
2. Шаги идут строго по порядку. Активный шаг подсвечивает `highlight` пульсацией.
3. После каждого изменения состояния синта (debounce ~150 мс) и на каждый note-on/off приложение вычисляет `check` активного шага:
   - `eq`: для enum, int и toggle — точное равенство; для непрерывных значений — допуск ±1 % диапазона параметра (у log-параметров, например `cutoff`, ±1 % считается в логарифмической шкале).
   - `gte` / `lte`: больше или равно / меньше или равно.
   - `between`: значение лежит в отрезке `[min, max]` включительно.
   - Для `mod:*` приложение берёт сумму глубин всех маршрутов с этой парой «источник → цель»; маршрут в режиме bypass считается как 0.
   - Измерители (`meter.*`) засчитываются, только пока звучит нота; условие должно держаться не меньше ~300 мс.
4. Шаг засчитывается автоматически, как только условие выполнено; кнопка «Далее» не нужна. Если `check` равен `null`, шаг информационный и закрывается кнопкой «Понятно».
5. Для `sound-match` приложение сравнивает каждый параметр из `targetPatch` по отдельности и подсказывает по каждому, в какую сторону его крутить («ярче/темнее», «длиннее/короче»). Рекомендуемые допуски: ±10 % диапазона для непрерывных параметров, ±1 шаг для int, точное совпадение для enum. Параметры, которых нет в `targetPatch`, сравниваются с INIT. Чтобы ответ нельзя было списать, target можно случайно сдвигать в пределах допуска.
6. Каждое значение рецепта и `targetPatch` — стартовая точка. Советуй ученику доводить звук на слух и не ставь балл за точное совпадение с рецептом.

## Неподтверждённые пункты (`unverified: true`)

Источник по Serum 2 — документ Xfer «What's New in Serum 2» и обзоры (MusicRadar, ModeAudio, Splice, KVR). Полное руководство Serum 2 получить не удалось. Всё, что взято из Serum 1 или из практики, помечено флагом. Это касается 27 уроков:

- `ui-overview-init` — точное расположение вкладок и элементов интерфейса.
- `wavetable-osc-panel` — набор ручек панели (CRS) и диапазоны Serum 2.
- `unison-panel` — где находятся ширина и режим унисона.
- `phase-sub-noise-panels` — Direct Out у SUB (подтверждён для Serum 1).
- `filter-panel-routing` — внешний вид панели и кнопок маршрута.
- `filter-types-tour` — полный список типов фильтров Serum 2.
- `env-panel` — жёсткая привязка ENV 1 к громкости и значения по умолчанию.
- `lfo-editor` — названия кнопок и режимов.
- `distortion-ott-panels` — полный список режимов дисторшна и параметры компрессора.
- `space-fx-panels` — параметры панелей Reverb, Delay и Hyper.
- `global-mix-page` — полифония, режимы портаменто и качества.
- `dual-warp-new-warps` — полный список и названия новых варпов.
- `wt-editor-draw-fft`, `wt-formula-morph`, `resampling-import` — функции редактора таблиц и режимы импорта (по Serum 1).
- `chaos-path-lfos` — параметры хаос- и path-LFO.
- `sample-multisample`, `granular-spectral` — ручки и шкалы движков (в тренажёре упрощены).
- `busses-splitters`, `riddim-midbass` — устройство сплиттеров внутри цепочки.
- `utility-bode-convolve` — параметры Bode и Convolve.
- `gain-staging-cpu` — данных о нагрузке на CPU в Serum 2 нет.
- `arp-and-clip` — режимы и скорости арпеджиатора.
- `hardstyle-kick` — числа анатомии бочки из второстепенного источника (BeatKey).
- `raw-kick-pitched-leads`, `capstone-rawstyle` — специфика роу и аптемпо держится на консенсусе практиков.
- `capstone-euphoric-hardstyle` — потактовый шаблон хардстайла и анти-климакс.

Ещё 92 параметра в `paramGlossary` помечены `unverified: true`. В основном это OSC C, движки осцилляторов, Dual Warp, `coarse`, ширина унисона, Filter 2 и полный список типов фильтров, кривизна огибающих, маршрутизация MIX, Bode/Convolve/Utility/Splitter, режимы арпа, полифония и качество. Когда найдётся руководство Serum 2, по нему нужно сверить названия режимов (варпы, фильтры, дисторшн), диапазоны и раскладку панелей.

Жанры с `unverified: true`: `hardstyle-euphoric`, `rawstyle`, `uptempo`, `hyperpop`, `future-bass`, `trance`. У них число тактов в структуре ориентировочное, а в `sourceNote` описано, что подтверждено. Подтверждены по источникам шаблон рыдима (EDMProd) и структура DnB (NI). Темп хардстайла в источниках расходится: 140–150 у EDMProd, 145–150 у eMastered, 150–160 у NI; современная норма около 150. Данных замеров LUFS для хардстайла, рыдима, фьюче-баса и транса нет.

## Авторские права

Рецепты, теория и формулировки написаны своими словами на основе исследовательских заметок. Тексты из курсов и статей не копировались. Из источников взяты только факты и общепринятые стартовые значения.

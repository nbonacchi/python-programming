# Lisbon and Portugal Notebook Example Localization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace standalone Scottish teaching examples in tracked Jupyter notebooks with Lisbon or Portugal equivalents without translating the notebooks or changing their underlying data files.

**Architecture:** Apply targeted patches to existing notebook JSON so cell order, metadata, code structure, and unrelated outputs remain intact. Keep source-specific Scottish provenance accurate, update only outputs made stale by edited literals, and verify the complete notebook inventory with structural and semantic assertions.

**Tech Stack:** Jupyter Notebook JSON, Python 3.13, standard-library `json` and `ast`, existing repository `.venv`, PowerShell, Git.

## Global Constraints

- Inspect all 18 tracked `.ipynb` files under `python-intro/` and `python-data-science/`.
- Edit Markdown prose and textual values in code cells when they form part of a Scottish teaching example.
- Update directly affected saved outputs when they would otherwise contradict an edited source cell; clear only a stale affected output if reliable execution is unavailable.
- Leave CSV, pickle, spreadsheet, audio, image, and other data files unchanged.
- Do not edit checkpoint notebooks or generated copies.
- Do not translate English prose, identifiers, explanations, or instructions into Portuguese.
- Do not relabel unchanged Scottish datasets as Portuguese datasets.
- Keep author credits, dataset filenames, and source attribution factually accurate.
- Preserve notebook metadata, cell types, cell ordering, and execution structure.
- Avoid unrelated cleanup, refactoring, or formatting changes.

---

### Task 1: Localize introductory Lisbon examples

**Files:**
- Modify: `python-intro/python-intro-1.ipynb` cells 0-3 and 42

**Interfaces:**
- Consumes: Existing notebook JSON and the unchanged miles-to-kilometres lesson.
- Produces: A Lisbon-to-Porto conversion example and a Lisbon string-method example with consistent code and output.

- [ ] **Step 1: Run the semantic check before editing**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import json,pathlib; p=pathlib.Path('python-intro/python-intro-1.ipynb'); n=json.loads(p.read_text(encoding='utf-8')); s=''.join(''.join(c.get('source', [])) for c in n['cells']); assert 'Edinburgh' not in s and 'distanceToLondon' not in s"
```

Expected: FAIL because the Scottish/London example is still present.

- [ ] **Step 2: Patch the Markdown, code, and saved result**

Apply these exact changes without reserializing the full notebook:

```text
"distance between Edinburgh and London is 403 miles" -> "distance between Lisbon and Porto is 195 miles"
403 * 1.60934 -> 195 * 1.60934
saved text/plain result 648.56402 -> 313.8213
"distance between Edinburgh and London in km" -> "distance between Lisbon and Porto in km"
distanceToLondonMiles = 403 -> distanceToPortoMiles = 195
distanceToLondonKm -> distanceToPortoKm
x = "Edinburgh" -> x = "Lisbon"
```

- [ ] **Step 3: Verify structure and semantics**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import json,pathlib; p=pathlib.Path('python-intro/python-intro-1.ipynb'); n=json.loads(p.read_text(encoding='utf-8')); s=''.join(''.join(c.get('source', [])) for c in n['cells']); assert n['nbformat']==4; assert 'Edinburgh' not in s and 'distanceToLondon' not in s; assert 'Lisbon' in s and 'distanceToPortoMiles = 195' in s; assert n['cells'][1]['outputs'][0]['data']['text/plain']==['313.8213']"
```

Expected: PASS with no output.

- [ ] **Step 4: Commit the introductory localization**

```powershell
git add python-intro/python-intro-1.ipynb
git commit -m "content: localize introductory examples to Lisbon"
```

---

### Task 2: Localize currency and tabular labels

**Files:**
- Modify: `python-data-science/python-data-0-recap.ipynb` cell 32
- Modify: `python-data-science/python-data-4-pandas.ipynb` cells 12, 15, 28, 30, 34, and 101
- Modify: `python-data-science/python-data-exercises.ipynb` cell 61

**Interfaces:**
- Consumes: Existing calculation, Series, DataFrame, column-drop, and filtering exercises.
- Produces: Euro-denominated messages and Portugal-based illustrative city labels without changing exercise logic or underlying files.

- [ ] **Step 1: Run the targeted localization check before editing**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import json,pathlib; ps=[pathlib.Path('python-data-science/python-data-0-recap.ipynb'),pathlib.Path('python-data-science/python-data-4-pandas.ipynb'),pathlib.Path('python-data-science/python-data-exercises.ipynb')]; s=''.join(''.join(''.join(c.get('source', [])) for c in json.loads(p.read_text(encoding='utf-8'))['cells']) for p in ps); assert 'Ł' not in s and not any(x in s for x in ['Glasgow','Edinburgh','Aberdeen','Dundee'])"
```

Expected: FAIL because pound symbols and Scottish city labels are present.

- [ ] **Step 2: Patch currencies and city labels**

Apply these exact replacements in the specified cells:

```text
Ł -> € in bitcoin profit/loss messages and both home-price exercises
Glasgow -> Lisbon
Edinburgh -> Porto
Aberdeen -> Braga
Dundee -> Coimbra
df.drop(["Aberdeen", "Edinburgh"], axis="columns") -> df.drop(["Braga", "Porto"], axis="columns")
```

Keep all existing numeric values and years unchanged because this task changes notebook text only. Add `# Illustrative values for data-structure examples` immediately above the two city/population mappings so they are not presented as sourced Portuguese statistics.

- [ ] **Step 3: Verify the edited code and notebook JSON**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import ast,json,pathlib; ps=[pathlib.Path('python-data-science/python-data-0-recap.ipynb'),pathlib.Path('python-data-science/python-data-4-pandas.ipynb'),pathlib.Path('python-data-science/python-data-exercises.ipynb')]; ns=[json.loads(p.read_text(encoding='utf-8')) for p in ps]; s=''.join(''.join(''.join(c.get('source', [])) for c in n['cells']) for n in ns); assert 'Ł' not in s and not any(x in s for x in ['Glasgow','Edinburgh','Aberdeen','Dundee']); assert all(x in s for x in ['Lisbon','Porto','Braga','Coimbra','€150']); [ast.parse(''.join(n['cells'][i].get('source', []))) for n,i in [(ns[0],32),(ns[1],12),(ns[1],15),(ns[1],28),(ns[1],30),(ns[1],34)]]"
```

Expected: PASS with no output.

- [ ] **Step 4: Commit currency and tabular localization**

```powershell
git add python-data-science/python-data-0-recap.ipynb python-data-science/python-data-4-pandas.ipynb python-data-science/python-data-exercises.ipynb
git commit -m "content: localize currency and city examples"
```

---

### Task 3: Localize rental and string-processing examples

**Files:**
- Modify: `python-data-science/python-data-extra-machine-learning.ipynb` cells 1, 9, and 41
- Modify: `python-data-science/python-data-extra-regex.ipynb` cells 4, 5, 7, and 11

**Interfaces:**
- Consumes: Existing regression arrays, string-splitting flow, loop behavior, and capitalization lesson.
- Produces: A Praça do Comércio rental scenario, euro-denominated prose, generic institutional resource wording, and consistent Lisbon string outputs.

- [ ] **Step 1: Run the focused check before editing**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import json,pathlib; ps=[pathlib.Path('python-data-science/python-data-extra-machine-learning.ipynb'),pathlib.Path('python-data-science/python-data-extra-regex.ipynb')]; blobs=[p.read_text(encoding='utf-8') for p in ps]; assert not any(x in ''.join(blobs) for x in ['George Square','Edinburgh','EDINBURGH','Ł'])"
```

Expected: FAIL because the rental and string examples still use Edinburgh and pounds.

- [ ] **Step 2: Patch the rental example and access statement**

Apply these exact changes in the machine-learning notebook:

```text
George Square in Edinburgh -> Praça do Comércio in Lisbon
Every Ł currency symbol -> €
"Lynda is free for students and staff of Edinburgh University." -> "Access to LinkedIn Learning courses may depend on your institution."
```

Keep the regression arrays `560`, `1200`, and `540` unchanged so the derivation and model remain consistent.

- [ ] **Step 3: Patch regex sources and their dependent outputs**

Apply these exact changes in the regex notebook:

```text
val = "Edinburgh is great" -> val = "Lisbon is great"
['Edinburgh', 'is', 'great'] -> ['Lisbon', 'is', 'great']
'Edinburgh::is::great' -> 'Lisbon::is::great'
val = "Edinburgh" -> val = "Lisbon"
printed letters E,d,i,n,b,u,r,g,h -> L,i,s,b,o,n
'EDINBURGH' -> 'LISBON'
```

- [ ] **Step 4: Verify sources, outputs, and code syntax**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import ast,json,pathlib; ml=json.loads(pathlib.Path('python-data-science/python-data-extra-machine-learning.ipynb').read_text(encoding='utf-8')); rx=json.loads(pathlib.Path('python-data-science/python-data-extra-regex.ipynb').read_text(encoding='utf-8')); b=json.dumps([ml,rx],ensure_ascii=False); assert not any(x in b for x in ['George Square','EDINBURGH','Ł']); assert 'Praça do Comércio in Lisbon' in b and 'LISBON' in b and '€2000' in b; [ast.parse(''.join(rx['cells'][i]['source'])) for i in [4,5,7,11]]"
```

Expected: PASS with no output.

- [ ] **Step 5: Commit rental and string localization**

```powershell
git add python-data-science/python-data-extra-machine-learning.ipynb python-data-science/python-data-extra-regex.ipynb
git commit -m "content: localize rental and string examples"
```

---

### Task 4: Neutralize dataset framing while preserving provenance

**Files:**
- Modify: `python-data-science/python-data-3-plotting.ipynb` cell 17
- Modify: `python-data-science/python-data-exercises.ipynb` cell 35
- Modify: `python-data-science/python-data-extra-text-analysis.ipynb` cells 9 and 38
- Verify unchanged provenance: `python-data-science/python-data-extra-life.ipynb` cell 0

**Interfaces:**
- Consumes: Unchanged NRS marriage data, unchanged University of Edinburgh tweet data, and the existing Game of Life author credit.
- Produces: Geographically neutral exercise framing, a Lisbon capitalization example, and institution-neutral resource availability wording while retaining truthful source attribution.

- [ ] **Step 1: Run the provenance-aware check before editing**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import json,pathlib; p=pathlib.Path('python-data-science/python-data-extra-text-analysis.ipynb'); n=json.loads(p.read_text(encoding='utf-8')); s=''.join(n['cells'][9]['source'])+''.join(n['cells'][38]['source']); assert '`Lisbon` and `lisbon`' in s and 'Main Lirbrary at Edinburgh University' not in s"
```

Expected: FAIL because the standalone capitalization example and resource wording still use Edinburgh.

- [ ] **Step 2: Make NRS exercise framing provenance-first**

In both the plotting and exercises notebooks, replace the sentence with:

```markdown
The following code reads quarterly data on marriages and civil partnerships between 2008 and 2018. The unchanged local dataset was obtained from [National Records of Scotland (NRS)](https://www.nrscotland.gov.uk/statistics-and-data).
```

This deliberately retains Scotland only in the source name; do not change `data/marriage_data.csv` or its code comments.

- [ ] **Step 3: Localize the independent text-analysis wording**

Apply these exact changes:

```text
`Edinburgh` and `edinburgh` -> `Lisbon` and `lisbon` in the lowercase explanation
"The book is available at the Main Lirbrary at Edinburgh University." -> "Check your institutional library for availability."
```

Do not change the University of Edinburgh dataset description, `@EdinburghUni`, the `uoe_tweets_07022019.csv` path, dataset-derived outputs, or the University of Edinburgh Game of Life author credit.

- [ ] **Step 4: Verify provenance and localization boundaries**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import json,pathlib; plot=json.loads(pathlib.Path('python-data-science/python-data-3-plotting.ipynb').read_text(encoding='utf-8')); ex=json.loads(pathlib.Path('python-data-science/python-data-exercises.ipynb').read_text(encoding='utf-8')); ta=json.loads(pathlib.Path('python-data-science/python-data-extra-text-analysis.ipynb').read_text(encoding='utf-8')); life=json.loads(pathlib.Path('python-data-science/python-data-extra-life.ipynb').read_text(encoding='utf-8')); assert 'National Records of Scotland (NRS)' in ''.join(plot['cells'][17]['source']) and 'National Records of Scotland (NRS)' in ''.join(ex['cells'][35]['source']); assert '`Lisbon` and `lisbon`' in ''.join(ta['cells'][9]['source']); assert 'University of Edinburgh twitter account' in ''.join(ta['cells'][2]['source']); assert '@EdinburghUni' in ''.join(ta['cells'][5]['source']); assert 'University of Edinburgh' in ''.join(life['cells'][0]['source'])"
```

Expected: PASS with no output.

- [ ] **Step 5: Commit provenance-safe wording changes**

```powershell
git add python-data-science/python-data-3-plotting.ipynb python-data-science/python-data-exercises.ipynb python-data-science/python-data-extra-text-analysis.ipynb
git commit -m "content: localize prose while preserving dataset provenance"
```

---

### Task 5: Validate every notebook and final scope

**Files:**
- Verify: all 18 tracked `.ipynb` files
- Verify: repository diff and unchanged data files
- Include: `docs/superpowers/plans/2026-07-15-localize-notebook-examples.md`

**Interfaces:**
- Consumes: All localized notebooks from Tasks 1-4.
- Produces: Evidence that notebooks remain structurally valid, edited code is syntactically valid, stale localized outputs are resolved, and no data file changed.

- [ ] **Step 1: Parse the complete tracked notebook inventory**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import json,pathlib,subprocess; fs=[pathlib.Path(x) for x in subprocess.check_output(['git','ls-files','*.ipynb'],text=True).splitlines()]; assert len(fs)==18, len(fs); ns=[json.loads(p.read_text(encoding='utf-8')) for p in fs]; assert all(n.get('nbformat')==4 and isinstance(n.get('cells'),list) for n in ns); print('validated 18 notebooks')"
```

Expected: `validated 18 notebooks`.

- [ ] **Step 2: Audit remaining Scottish terms with an explicit provenance allowlist**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import json,pathlib,re,subprocess; pat=re.compile(r'(?i)scotland|scottish|edinburgh|glasgow|aberdeen|dundee|george square|[Ł£]'); allowed={'python-data-science/python-data-3-plotting.ipynb','python-data-science/python-data-exercises.ipynb','python-data-science/python-data-extra-life.ipynb','python-data-science/python-data-extra-text-analysis.ipynb','python-data-science/python-data-extra-regex.ipynb'}; hits=[]; fs=[pathlib.Path(x) for x in subprocess.check_output(['git','ls-files','*.ipynb'],text=True).splitlines()]; [(hits.append((p.as_posix(),i,sorted(set(m.group(0) for m in pat.finditer(blob))))) for p in fs for i,c in enumerate(json.loads(p.read_text(encoding='utf-8'))['cells']) for blob in [''.join(c.get('source',[]))+json.dumps(c.get('outputs',[]),ensure_ascii=False)] if pat.search(blob))]; assert all(path in allowed for path,cell,terms in hits), hits; print('\n'.join(map(str,hits)))"
```

Expected: Matches only for NRS provenance, University of Edinburgh provenance/credit and tweet-derived outputs, plus the `Aberdeen` baby-name output in the regex notebook. No standalone Scottish teaching example may remain.

- [ ] **Step 3: Execute focused edited code paths**

Run:

```powershell
& '.venv\Scripts\python.exe' -c "import json,pathlib; intro=json.loads(pathlib.Path('python-intro/python-intro-1.ipynb').read_text(encoding='utf-8')); ns={}; exec(''.join(intro['cells'][3]['source']),ns); assert abs(ns['distanceToPortoKm']-313.8213)<1e-9; rx=json.loads(pathlib.Path('python-data-science/python-data-extra-regex.ipynb').read_text(encoding='utf-8')); ns={}; exec(''.join(rx['cells'][4]['source']),ns); assert ns['val']=='Lisbon is great'; exec(''.join(rx['cells'][5]['source']),ns); exec(''.join(rx['cells'][7]['source']),ns); assert ns['val']=='Lisbon'; print('focused execution passed')"
```

Expected: The Lisbon letters followed by `focused execution passed`.

- [ ] **Step 4: Confirm the diff contains no changed data or checkpoint files**

Run:

```powershell
git status --short
git diff --name-only HEAD~4..HEAD
```

Expected: Only the implementation plan may remain uncommitted; committed implementation paths are the eight intended notebooks, with no files under `python-data-science/data/` or `.ipynb_checkpoints/`.

- [ ] **Step 5: Review notebook diffs and commit the plan**

Run:

```powershell
git diff --check HEAD~4..HEAD
git add docs/superpowers/plans/2026-07-15-localize-notebook-examples.md
git commit -m "docs: add notebook localization implementation plan"
git status --short
```

Expected: `git diff --check` reports no errors and the final `git status --short` is empty.

# Lisbon and Portugal Notebook Example Localization

## Objective

Localize Scottish teaching examples in every tracked Jupyter notebook to Lisbon or Portugal while preserving the notebooks' existing English language, teaching intent, cell order, and runnable behavior.

## Scope

- Inspect all 18 tracked `.ipynb` files under `python-intro/` and `python-data-science/`.
- Edit Markdown prose and textual values in code cells when they form part of a Scottish teaching example.
- Update directly affected saved outputs when they would otherwise contradict an edited source cell. If reliable execution is unavailable, clear only the stale affected output.
- Leave CSV, pickle, spreadsheet, audio, image, and other data files unchanged.
- Do not edit checkpoint notebooks or generated copies.

## Localization Rules

- Replace standalone Scottish place examples with appropriate Lisbon or Portugal equivalents.
- Replace pounds with euros and adjust surrounding example values or wording when needed for internal consistency.
- Preserve the purpose of each exercise. For example, a distance-conversion exercise remains a distance-conversion exercise, and a pandas label example remains a label example.
- Treat values used only to demonstrate data structures as illustrative unless the notebook explicitly presents them as sourced statistics.
- Do not translate English prose, identifiers, explanations, or instructions into Portuguese.

## Provenance and Accuracy

- Do not relabel unchanged Scottish datasets as Portuguese datasets.
- Keep author credits and source attribution factually accurate, including University of Edinburgh credits and NRS provenance.
- Geographically neutralize surrounding teaching prose when that reduces irrelevant Scottish framing without obscuring the real data source.
- Keep required dataset filenames and paths unchanged so existing code continues to run.
- Generalize institution-specific access statements when their original wording is relevant only to Edinburgh users and no verified Portuguese equivalent is available.

## Notebook Integrity

- Preserve notebook metadata, cell types, cell ordering, and execution structure.
- Make targeted source edits instead of rebuilding notebooks.
- Avoid unrelated cleanup, translation, refactoring, or formatting changes.

## Validation

- Parse every notebook as valid notebook JSON after editing.
- Confirm the tracked notebook inventory remains unchanged.
- Search notebook sources and outputs for Scottish terms, then classify any remaining matches as required provenance, dataset paths/content, or missed localization.
- Confirm Lisbon, Portugal, Portuguese place names, and euro examples appear where expected.
- Verify that edited code cells remain syntactically valid.
- Execute affected notebooks or focused cells when dependencies and local data permit; otherwise report the exact validation limitation.
- Review the final diff to ensure data files and non-notebook teaching content were not changed by the localization work.

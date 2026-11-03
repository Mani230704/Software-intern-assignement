# Software Intern Assignment Submission

This repository contains the completed submission for the software intern assignment.

## Contents

- Part 1: [Part 1_Programming fundamentals.py](Part%201_Programming%20fundamentals.py)
- Part 2: [Part 2_AIML mini project_predicting machine failures.ipynb](Part%202_AIML%20mini%20project_predicting%20machine%20failures.ipynb)
- Part 3: [Part3_answers.md](Part3_answers.md)
- Manager summary: [manager_summary.md](manager_summary.md)
- Tests: [test_part1.py](test_part1.py)
- SQL: [sql/machine_failure_queries.sql](sql/machine_failure_queries.sql) and [sql/machine_failure_queries_output.txt](sql/machine_failure_queries_output.txt)
- Bonus extension: [bonus_extension.py](bonus_extension.py)
- Dependencies: [requirements.txt](requirements.txt)

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate it:
   - Windows PowerShell:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the tests:
   ```bash
   pytest -q
   ```
5. Run the notebook:
   ```bash
   jupyter notebook "Part 2_AIML mini project_predicting machine failures.ipynb"
   ```
   or open it in VS Code/Jupyter and run all cells from top to bottom.

## How to run everything

### Part 1
```bash
python "Part 1_Programming fundamentals.py"
```
This file contains the smoothing function and can be validated with the included pytest file.

### Part 2
Open the notebook and run all cells in order. The notebook downloads the AI4I dataset automatically if it is not already present in the repository folder.

### SQL files
The SQL script is in [sql/machine_failure_queries.sql](sql/machine_failure_queries.sql) and a sample output is in [sql/machine_failure_queries_output.txt](sql/machine_failure_queries_output.txt).

## Main results for Part 2

We used the AI4I 2020 predictive maintenance dataset and trained a simple decision tree with a stratified 80/20 split.

Key evaluation results on the held-out test set:

- Accuracy: 0.94
- Failure precision: 0.33
- Failure recall: 0.85
- Macro-average F1: 0.72

Interpretation:

- The model is very good at identifying machines that are not failing.
- It catches most actual failures (high recall), which is valuable for safety and maintenance planning.
- It still produces some false alarms, which is expected with a rare-event classification task.
- Because machine failures are uncommon, class imbalance means accuracy alone is misleading.

## Assumptions made

- We used the AI4I 2020 synthetic predictive maintenance dataset.
- We did not include leakage columns such as `UDI`, `Product ID`, `TWF`, `HDF`, `PWF`, `OSF`, and `RNF` because they would reveal the target or encode the outcome too strongly.
- We used a simple, interpretable decision tree rather than a more complex black-box model to keep the solution understandable and explainable.
- The notebook is designed to run in a clean environment, downloading the dataset when needed.

## Bonus extension

The file [bonus_extension.py](bonus_extension.py) adds a lightweight predictive helper that can be used to score a new machine-reading record using the same logic and feature layout as the trained model.

## Honest limitations

The model is useful as a baseline, but it is not deployment-ready without more validation.

- It should be checked on real factory data.
- It should be evaluated for business cost, not just accuracy.
- It may need threshold tuning and retraining as operating conditions change.
- Rare failure events require careful monitoring of false positives and missed alerts.

## Summary

This project keeps the solution simple, interpretable, and honest: a clear baseline model, tested code, SQL evidence, and a realistic explanation of what the model does well and where it still falls short.

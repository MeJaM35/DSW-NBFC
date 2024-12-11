# NBFC Loan Repayment Prediction Project

## Problem Statement

A trusted Non-Banking Financial Company (NBFC) specializing in providing quick and accessible small loans tailored to the needs of individuals and small businesses aims to develop a classification model to predict loan repayment behavior. The goal is to identify potential defaulters and non-defaulters, enhancing risk assessment and improving the loan approval process.

## Task Summary

The project involves:

1. **EDA (Exploratory Data Analysis):**
   - Perform EDA on the provided data.
   - Submit the analysis in a notebook named `eda.ipynb`.
   - Include comments in markdown blocks for each analysis/chart code block.

2. **Modeling:**
   - Develop a training pipeline and submit it in a script named `model_.py`.
   - Create at least two different models.
   - Follow an object-oriented, class-based approach. Each model class must include the following functions:
     - `load`: To load data.
     - `preprocess`: To perform preprocessing steps.
     - `train`: To handle training steps.
     - `test`: To evaluate the model and generate an evaluation summary.
     - `predict`: For inference.

3. **Model Selection:**
   - Create a model selection pipeline and submit it in a notebook named `model_selection.ipynb`.
   - Test the different models created during the modeling phase.
   - Evaluate models using relevant metrics and perform hyperparameter tuning if required.
   - Choose the best model and provide a summary explaining the choice at the end of the notebook.

## Data Overview

Two datasets are provided:

- **Historic data:** Contains loan disbursement applications and their default/non-default status for the past 2+ years. (File name: `train_data.xlsx`)
- **Validation data:** Contains loan disbursement applications and their default/non-default status for the past 3 months. (File name: `test_data.xlsx`)

## Technical Requirements

- **Python Version:** Use Python 3.7+
- **Notebook Requirements:**
  - All notebooks must be pre-run with output cells included.
  - Use appropriate coding standards and provide in-line comments where required.
- **Submission Files:**
  - `eda.ipynb`: Notebook containing the exploratory data analysis.
  - `model_.py`: Script containing the training pipeline.
  - `model_selection.ipynb`: Notebook for model evaluation and selection.
  - Final submission should be a zip file named `<Your Full Name>.zip` containing all required files.

## Deliverables

1. **Exploratory Data Analysis (EDA):**
   - `eda.ipynb`: Perform exploratory analysis with appropriate visualizations and comments.

2. **Modeling:**
   - `model_.py`: Training pipeline with at least two models implemented using a class-based approach.

3. **Model Selection:**
   - `model_selection.ipynb`: Evaluate models, compare their performance, and finalize the best one.

4. **Submission:**
   - Submit all the required files as a zip archive named `<Your Full Name>.zip`.

## Summary Checklist

### Notebooks:
- [ ] `eda.ipynb` with EDA, visualizations, and markdown comments.
- [ ] `model_selection.ipynb` with model evaluation, metrics, and final model selection summary.

### Scripts:
- [ ] `model_.py` implementing at least two models with the required methods (`load`, `preprocess`, `train`, `test`, `predict`).

### Final Submission:
- [ ] A zip file containing all the required files.

---

Feel free to reach out for clarification or support as needed. Happy coding!

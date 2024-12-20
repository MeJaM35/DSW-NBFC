# -*- coding: utf-8 -*-
"""Model_

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_wNehllWRwCqjAFZALzf1gZLxTuhanwA
"""

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import numpy as np

test_df = pd.read_csv("eda_dataset_test.csv")
df = pd.read_csv("eda_dataset_train.csv")

X_train = df[['term', 'loan_age', 'emp_length', 'sub_grade_combined', 'int_rate', 'loan_amnt', 'account_bal', 'cibil_score', 'annual_inc']]
y_train = df['loan_status']

X_test = test_df[['term', 'loan_age', 'emp_length', 'sub_grade_combined', 'int_rate', 'loan_amnt', 'account_bal', 'cibil_score', 'annual_inc']]
y_test = test_df['loan_status']

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy_score(y_test, y_pred)

classification_report(y_test, y_pred)

log_reg_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')  # cv=5 for 5 folds
np.mean(log_reg_scores)

confusion_matrix(y_test, y_pred)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

accuracy_score(y_test, y_pred)

cross_val_score(rf_model, X_train, y_train, cv=5, scoring='accuracy')

classification_report(y_test, y_pred)

confusion_matrix(y_test, y_pred)

xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
xgb_model.fit(X_train, y_train)

cross_val_score(xgb_model, X_train, y_train, cv=5, scoring='accuracy')

y_pred = model.predict(X_test)

accuracy_score(y_test, y_pred)
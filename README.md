<!-- Its an END to END machine learning project to find the wheather a customer close the account in the bank -->
#### Bank Customers Crunch
## Project Overview
This project is an end-to-end machine learning pipeline that predicts customer churn for a bank. Churn prediction helps banks identify customers who are likely to leave, enabling targeted retention strategies to reduce losses and improve customer satisfaction.<br>

## Dataset
This dataset is for banks with following columns:

1.customer_id, unused variable.<br>
2.credit_score, used as input.<br>
3.country, used as input.<br>
4.gender, used as input.<br>
5.age, used as input.<br>
6.tenure, used as input.<br>
7.balance, used as input.<br>
8.products_number, used as input.<br>
9.credit_card, used as input.<br>
10.active_member, used as input.<br>
11.estimated_salary, used as input.<br>
12.churn, used as the target. 1 if the client has left the bank during some period or 0 if he/she has not.<br><br>

## Problem Statement
Predict whether a customer is likely to churn based on their demographic and account-related features. The goal is to proactively identify high-risk customers and implement retention strategies.

## Methodology

# Data Preprocessing:

1)Handle missing values

2)Encode categorical variables

3)Scale numerical features

# Exploratory Data Analysis (EDA):

1)Visualize feature distributions

2)Analyze correlations

3)Identify patterns leading to churn

# Feature Engineering:

1)Create new features to capture customer behavior

2)Select most important features for modeling

# Modeling:

1)Train various machine learning models (Logistic Regression, Random Forest, XGBoost, etc.)

2)Hyperparameter tuning using GridSearchCV/RandomizedSearchCV

3)Evaluate models based on metrics

## Modeling

Models used: Logistic Regression, Decision Trees, Random Forest, Gradient Boosting (XGBoost)

# Pipeline:

Preprocessing → Feature Scaling → Model Training → Evaluation → Deployment

## Evaluation Metrics

1)Accuracy

2)Precision

3)Recall

4)F1 Score

5)ROC-AUC Score

## Results

Best Model: **RANDOM FOREST CLASSIFIER** 

ROC-AUC: **0.87**

Accuracy: **82%**

Key Features Influencing Churn: **CreditScore, Balance, Tenure, IsActiveMember**


## Requirments

pandas
numpy
seaborn
scikit-learn
flask
gunicorn

## Approch



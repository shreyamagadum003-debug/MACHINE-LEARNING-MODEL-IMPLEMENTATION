# MACHINE-LEARNING-MODEL-IMPLEMENTATION

COMPANY: CODTECH IT SOLUTIONS

NAME: SHREYA TANAJI MAGADUM

INTERN ID: CTIS2453

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH KUMAR

# Spam Email Classification Using Machine Learning

This project implements a simple Machine Learning model in Python to classify emails as Spam or Not Spam using Scikit-learn. 
It demonstrates the complete workflow of text classification including vectorization, model training, evaluation, and prediction using a small sample dataset.

## Features

Converts email text into numerical features using CountVectorizer

Trains a Naive Bayes classifier for spam detection

Evaluates the model using accuracy score and classification report

Predicts whether a new email message is spam or not

Beginner-friendly and easy to understand implementation

## Installation

Clone the repository:

git clone <repository_link>


## Install required libraries:

pip install scikit-learn

## Usage

Run the Python script:

python spam_classifier.py


## The program will:

Train the model

Display accuracy and evaluation metrics

Predict whether a sample email is spam or not

## Technologies Used

Python

Scikit-learn

## How It Works

A small dataset of labeled email messages is used.

Text data is converted into numeric vectors using Bag-of-Words.

The dataset is split into training and testing sets.

A Naive Bayes classifier is trained and evaluated.

The model predicts spam or not spam for new input messages.

## Applications

This project can be extended for real-world email filtering systems, SMS spam detection, and content moderation tools.

## OUTPUT

Program started

Model training completed

Accuracy: 1.0

Classification Report:

              precision    recall  f1-score   support

           0       1.00      1.00      1.00         2
           
           1       1.00      1.00      1.00         1
           

    accuracy                           1.00         3
    
   macro avg       1.00      1.00      1.00         3
   
weighted avg       1.00      1.00      1.00         3



New Email: You have won a free lottery

Prediction: Spam

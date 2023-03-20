import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import acquire
import prepare
import numpy as np
import env
import scipy.stats as stats

from pydataset import data
from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from prepare import split_data

def get_metrics(y, y_pred, dataset):
    TP, FP, FN, TN = confusion_matrix(y, y_pred).ravel()
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    TPR = recall = TP / (TP + FN)
    FPR = FP / (FP + TN)
    TNR = TN / (FP + TN)
    FNR = FN / (FN + TP)
    precision =  TP / (TP + FP)
    f1 =  2 * ((precision * recall) / ( precision + recall))
    support_0 = dataset[dataset.churn == 0].shape[0]
    support_1 = dataset[dataset.churn == 1].shape[0]
    print(f'''
    Accuracy: {accuracy}
    True Positive Rate: {TPR}
    True Negative Rate: {TNR}
    False Positive Rate: {FPR}
    False Negative Rate: {FNR}
    Precision : {precision}
    f1 score: {f1}
    supports: 0: {support_0} 1: {support_1}
    ''')

def conf_matrix(y, y_preds):
    matrix = confusion_matrix(y, y_preds)
    rubric = pd.DataFrame(
        {'pred_0': ['True Positive', 'False Positive'],
        'pred_1': ['False Positive', 'True Negative']        
         }, index = ['actual_0', 'actual_1']
        )
    matrix = rubric + ': ' + matrix.astype(str)
    return matrix

def class_report(y, y_preds):
    report = pd.DataFrame(classification_report(y, y_preds, output_dict=True))
    return report
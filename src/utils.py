#all the common thing or functionalaties the entire project can use
import os
import sys

import numpy as np
import pandas as pd
import pickle

from sklearn.metrics import average_precision_score
from sklearn.model_selection import GridSearchCV

from src.exception import customException

def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        
    except Exception as e:
        raise customException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report={}
        
        for i in range(len(list(models))):
            model=list(models.values())[i]
            para = param[list(models.keys())[i]]
            
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)
            
            
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            if hasattr(model, "predict_proba"):
                y_train_pred_proba = model.predict_proba(X_train)[:,1]
                y_test_pred_proba = model.predict_proba(X_test)[:,1]
            elif hasattr(model, "decision_function"):
                y_train_pred_proba = model.decision_function(X_train)
                y_test_pred_proba = model.decision_function(X_test)
            else:
                continue
            
            
            
            train_model_score=average_precision_score(y_train, y_train_pred_proba)
            test_model_score=average_precision_score(y_test, y_test_pred_proba)
            
            report[list(models.keys())[i]]=test_model_score
            
        return report
    
    except Exception as e:
        raise customException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise customException(e, sys)
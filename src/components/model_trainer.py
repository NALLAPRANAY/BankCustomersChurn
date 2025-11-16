import os
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.ensemble import RandomForestClassifier
from src.logger import logging
from src.exception import CustomException
import sys
from sklearn.metrics import accuracy_score
from src.utils import save_obj
@dataclass
class ModelConfig:
    modelfilepath:str=os.path.join("artifacts","model.pkl")

class ModelTraining:
    def __init__(self):
        self.modelpath=ModelConfig()
    def intiate_modeltraining(self,train_arr,test_arr):
        try:
            # train_arr=pd.DataFrame(train_arr)
            # test_arr=pd.DataFrame(test_arr)
            X_train=train_arr[:,:-1]
            y_train=train_arr[:,-1]
            X_test=test_arr[:,:-1]
            y_test=test_arr[:,-1]
            logging.info("Passing parameters to model")
            RFC=RandomForestClassifier(max_depth=5,min_samples_leaf= 30,min_samples_split= 5,
                                       n_estimators= 150,class_weight='balanced',
                                       random_state=42)
            logging.info("intiating training")
            RFC.fit(X_train,y_train)
            logging.info("completed training")
            save_obj(self.modelpath.modelfilepath,RFC)
            logging.info("saved the model file")
            y_test_pred=RFC.predict(X_test)
            acs=accuracy_score(y_test,y_test_pred)
            return(
                acs
            )
            
        except Exception as e:
            raise CustomException(e,sys)
        

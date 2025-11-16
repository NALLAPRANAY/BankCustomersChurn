import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from src.logger import logging
from src.exception import CustomException
from sklearn.pipeline import Pipeline
import numpy as np
from src.utils import save_obj
@dataclass
class DataTransformationConfig:
    preprocessor_objfile=os.path.join("artificats","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_tramsformstion_obj(self):
        logging.info("Intaiating data transformation")
        columns=['CreditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']
        numerical=Pipeline(
            steps=[("scaler",StandardScaler())]
        )
        preprocessor=ColumnTransformer(
            [
                ("numerical",numerical,columns)
            ]
        )

        return preprocessor
    def intiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            train_df=train_df.drop(columns=['RowNumber','CustomerId','Surname','Geography','Gender'],axis=1)
            test_df=test_df.drop(columns=['RowNumber','CustomerId','Surname','Geography','Gender'],axis=1)
            logging.info("Removing unwanted columns in both test and train data frmaes")
            X_train=train_df.drop('Exited',axis=1)
            y_train=train_df['Exited']
            X_test=test_df.drop('Exited',axis=1)
            y_test=test_df['Exited']

            preprocessor_obj=self.get_tramsformstion_obj()
            X_train_scaled=preprocessor_obj.fit_transform(X_train)
            X_test_scaled=preprocessor_obj.transform(X_test)
            logging.info("Applying standard scaler using Column transformer, pipeline and Standard scaler")
            train_array=np.c_[X_train_scaled,np.array(y_train)]
            test_array=np.c_[X_test_scaled,np.array(y_test)]
            logging.info("Concating both independent and dependent values in test and  train array")
            save_obj(
                self.data_transformation_config.preprocessor_objfile,
                preprocessor_obj
            )
            logging.info("Saving prepocessor obj")
            return (
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_objfile
            )
            
        except Exception as e:
            raise CustomException(e,sys)
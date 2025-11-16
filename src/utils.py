import os
import sys
import pandas as pd
import numpy as np
import pickle
from src.logger import logging
from src.exception import CustomException
def save_obj(filepath,obj):
    try:
        dirname=os.path.dirname(filepath)
        os.makedirs(dirname,exist_ok=True)
        logging.info("Created a directory to save the object {obj}".format(obj=obj))
        with open(filepath,'wb') as file:
            pickle.dump(obj,file)
            logging.info("Saved the file at the given file path{filepath}".format(filepath=filepath))
    except Exception as e:
        raise CustomException(e,sys)
    
def load_obj(filepath):
    try:
        with open(filepath,'rb') as file:
            return pickle.load(file)

    except Exception as e:
        raise CustomException(e,sys)
    
def get_data_as_df(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    custom_input = {
        'CreditScore': [CreditScore],
        'Age': [Age],
        'Tenure': [Tenure],
        'Balance': [Balance],
        'NumOfProducts': [NumOfProducts],
        'HasCrCard': [HasCrCard],
        'IsActiveMember': [IsActiveMember],
        'EstimatedSalary': [EstimatedSalary]
    }

    df = pd.DataFrame(custom_input)
    return df
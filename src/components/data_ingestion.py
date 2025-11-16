import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artificats','train.csv')
    test_data_path=os.path.join('artificats','test.csv')
    raw_data_path=os.path.join('artificats','raw.csv')

class DataIngestion:
    def __init__(self):
        self.dataingestion_config=DataIngestionConfig
    
    def initiate_data_ingestion(self):
        logging.info('Intiating Data ingestion')
        try:
            df=pd.read_csv('churn.csv')
            logging.info("loaded the data into df dataframe")
            os.makedirs(os.path.dirname(self.dataingestion_config.train_data_path),exist_ok=True)
            logging.info("Created artifcat directory")
            df.to_csv(self.dataingestion_config.raw_data_path,index=False,header=True)
            logging.info("Raw data saved in the artifact folder")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
            train_set.to_csv(self.dataingestion_config.train_data_path) 
            test_set.to_csv(self.dataingestion_config.test_data_path)
            logging.info("Using train tets split extracted both test and train split and stored it in the artificts")
            return (
                self.dataingestion_config.train_data_path,
                self.dataingestion_config.test_data_path
            )       
        except:
            pass
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

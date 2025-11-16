import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_obj
class predictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join("artificats","preprocessor.pkl")
            logging.info("loaded both model and preprocessor to predict")
            model=load_obj(model_path)
            logging.info(model_path)
            logging.info(preprocessor_path)
            preprocessor=load_obj(preprocessor_path)
            processed_data=preprocessor.transform(features)
            pred=model.predict(processed_data)
            logging.info("processed_data:")
            logging.info(processed_data)
            logging.info("Prediction")
            logging.info(pred)
            if int(pred)==1:
                output="Yes"
            else:
                output="NO"
            return output
        except Exception as e:
            raise CustomException(e,sys)
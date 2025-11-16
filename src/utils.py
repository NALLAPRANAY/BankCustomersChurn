import os
import sys
import pandas 
import numpy
import pickle
from logger import logging
from exception import CustomException
def save_obj(filepath,obj):
    try:
        dirname=os.path.dirname(filepath)
        os.makedirs(dirname,exist_ok=True)
        logging.info("Created a directory to save the object {obj}".format(obj=obj))
        with open(filepath,'wb') as file:
            pickle.dump(obj,filepath)
            logging.info("Saved the file at the given file path{filepath}".format(filepath=filepath))
    except Exception as e:
        raise CustomException(e,sys)
    
def load_obj(filepath):
    try:
        with open(filepath,'rb') as file:
            return pickle.load(file)

    except Exception as e:
        raise CustomException(e,sys)

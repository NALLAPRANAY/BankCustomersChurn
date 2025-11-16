from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import predictPipeline
from src.utils import get_data_as_df

application=Flask(__name__)
app=application

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('/home.html')
    else:
        CreditScore=request.form.get('CreditScore')
        Age=request.form.get('CreditScore')
        Tenure=request.form.get('Tenure')
        Balance=request.form.get('Balance')
        NumOfProducts=request.form.get('NumOfProducts')
        HasCrCard=request.form.get('HasCrCard')
        IsActiveMember=request.form.get('IsActiveMember')
        EstimatedSalary=request.form.get('EstimatedSalary')
        input_df=get_data_as_df(CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary)
        predict_pipe=predictPipeline()
        result=predict_pipe.predict(input_df)
        return render_template('home.html',results=result)
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True) 
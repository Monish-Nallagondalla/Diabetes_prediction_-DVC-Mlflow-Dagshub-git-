import pandas as pd 
import pickle
from sklearn.metrics import accuracy_score
import yaml
import os
import mlflow
from urllib import urlparse

os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/Monish-Nallagondalla/Diabetes_prediction.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME'] = 'Monish-Nallagondalla'
os.environ['MLFLOW_TRACKING_PASSWORD'] ='417ac0bdaf269365b06f763d36db323b2964ab54'

   # 

params = yaml.safe_load(open('params.yaml'))['train']

def evaluate(data_path, model_path):
    data = pd.read_csv(data_path)

    X= data.drop(columns=['Outcome'])
    y= data['Outcome']

    mlflow.set_tracking_uri("https://dagshub.com/Monish-Nallagondalla/Diabetes_prediction.mlflow")

    model=pickle.load(open(model_path,'rb'))

    predictions = model.predict(X)
    accuracy=accuracy_score(y,predictions)

    mlflow.log_metric('accuracy',accuracy)

    print ("Model accuracy:{accuracy}")
if __name__=="__main__":
    evaluate(params['data'],params['model'])
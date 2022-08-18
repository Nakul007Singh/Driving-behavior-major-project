Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
import pickle


app = Flask(__name__)

model0 = pickle.load(open('/content/drive/My Drive/Colab Notebooks/Logistic_MajorX.pkl','rb'))
model1 = pickle.load(open('/content/drive/My Drive/Colab Notebooks/KNN_MajorX.pkl','rb'))
model2 = pickle.load(open('/content/drive/My Drive/Colab Notebooks/Decision-Tree_MajorX.pkl','rb'))
model3 = pickle.load(open('/content/drive/My Drive/Colab Notebooks/Random-Forest_MajorX.pkl','rb'))
model4 = pickle.load(open('/content/drive/My Drive/Colab Notebooks/SVM_MajorX.pkl','rb'))
run_with_ngrok(app)

@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])

def predict():
    
     AccX = float(request.args.get('AccX'))
     AccY = float(request.args.get('AccY'))
     AccZ = float(request.args.get('AccZ'))
     GyroX = float(request.args.get('GyroX'))
     GyroY = float(request.args.get('GyroY'))
     GyroZ  = float(request.args.get('GyroZ'))
     Timestamp = float(request.args.get('Timestamp'))
    

# CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary
     Model = str(request.args.get('Model'))

     if Model=='Logistic Prediction':
      prediction = model0.predict([[ AccX   ,   AccY   ,   AccZ  ,   GyroX   ,  GyroY  ,   GyroZ , Timestamp]])
    
     elif Model=='KNN Prediction':
      prediction = model1.predict([[AccX   ,   AccY   ,   AccZ  ,   GyroX   ,  GyroY  ,   GyroZ , Timestamp]])
    
     elif Model=='Decision Tree Prediction':
      prediction = model2.predict([[AccX   ,   AccY   ,   AccZ  ,   GyroX   ,  GyroY  ,   GyroZ , Timestamp]])

     elif Model=='Random Forest Prediction':
      prediction = model3.predict([[AccX   ,   AccY   ,   AccZ  ,   GyroX   ,  GyroY  ,   GyroZ , Timestamp]])

     else:
      prediction = model4.predict([[AccX   ,   AccY   ,   AccZ  ,   GyroX   ,  GyroY  ,   GyroZ , Timestamp]])

    
     if prediction == [1]:
      text = "It is a Fraud"
     else:
      text = "It is not Fraud"

     return render_template('index.html', prediction_text= 'Prediction says: {}'.format(text))
  
if __name__=="__main__":
app.run()

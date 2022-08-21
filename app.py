

import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)

model0 = pickle.load(open('Logistic_MajorX.pkl','rb'))
model1 = pickle.load(open('KNN_MajorX.pkl','rb'))
model2 = pickle.load(open('Decision-Tree_MajorX.pkl','rb'))
model3 = pickle.load(open('Random-Forest_MajorX.pkl','rb'))
model4 = pickle.load(open('SVM_MajorX.pkl','rb'))


@app.route('/')
def home():
  
    return render_template("index.html")
  
#------------------------------About us-------------------------------------------
@app.route('/aboutusnew')
def aboutusnew():
    return render_template('aboutusnew.html')
#------------------------------minors-------------------------------------------
@app.route('/minors')
def minors():
    return render_template('minors.html')
  
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

    
      if prediction == [0]:
      text = "Driving Behavior is slow"
     elif prediction == [1]:
      text = "Driving Behavior is Normal"
     else:
      text = "Driving Behavior is Aggressive"

     return render_template('index.html', prediction_text= 'Prediction says: {}'.format(text))
if __name__=="__main__":

    app.run() 

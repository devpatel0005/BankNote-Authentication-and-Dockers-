from flask import Flask,request
import pandas as pd
import numpy as np
import pickle  #to load the classifier.pkl file
import flasgger 
from flasgger import Swagger  #to create the api documentation

app=Flask(__name__)  #it just says from here the app should be started
Swagger(app)
#first i will have to load the classifier.pkl file

pickle_in=open('classifier.pkl','rb')  #open the file in read binary mod
classifier=pickle.load(pickle_in)  #load the file
pickle_in.close()  #close the file

@app.route('/') #to return the welcome message in flask we need a decorator so we use @app.route('/')
def welcome():
    return "Welcome All"  #this function will return a welcome message

#here the predict is a api 
@app.route('/predict') #decorator and by default it will take the get method
#we need to get the variable before predicting it so we are using get method
def predict_note_authentication():

    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """

    variance= request.args.get('variance')
    skewness= request.args.get('skewness')
    curtosis= request.args.get('curtosis')
    entropy= request.args.get('entropy')
    prediction=classifier.predict([[variance, skewness, curtosis, entropy]])  #we will pass the values in the classifier
    return "The predicted value is" + str(prediction)
#when return 200 is executed the output will be return of the function above

#here predict_file is a api
@app.route('/predict_file',methods=['POST'])  #we will use post method to upload the file
def predict_note_file():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """

    df_test=pd.read_csv(request.files.get("file")) #read the file from the request. The file variable will have all data of Testfile.csv
    prediction=classifier.predict(df_test)  #we will pass the dataframe to the classifier
    return "The predicted values are" + str(list(prediction))  


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)



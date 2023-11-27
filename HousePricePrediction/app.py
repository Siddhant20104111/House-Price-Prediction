
import numpy as np
import pandas as pd 
from flask import Flask, request, render_template
import pickle
import json


app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open('LinearRegression123.pkl','rb'))


# with open('columns.json', 'r') as f:
#      columns = json.load(f)

@app.route('/predict-page')
def predict_page():
    locations = sorted(data['Location'].unique())
    return render_template('prediction.html',locations=locations)

@app.route('/')
def home():
    return render_template('abc.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/mlconnectivity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('ab.html')



@app.route('/predict',methods=['POST'])
def predict():
    Location = request.form.get('location')
    Area = request.form.get('area')
    bhk = request.form.get('BHK')
    Gymnasium = request.form.get('gymnasium')
    Lift = request.form.get('lift')

    

    print(Location,Area,bhk,Gymnasium,Lift)
    # ##input = pd.DataFrame([[Location,Area,bhk,Gymnasium,Lift]],columns=['location','area','BHK','gymnasium','lift'])
    # ##input = pd.DataFrame({'location': [Location], 'area': [Area], 'BHK': [bhk], 'gymnasium': [Gymnasium], 'lift': [Lift]})
    # ##input = pd.get_dummies(input, columns=['location'])
    input = pd.DataFrame([[Area,Location,bhk,Gymnasium,Lift]],columns=['Area','Location','bhk','Gymnasium','Lift'])
    
    prediction=pipe.predict(input)[0] 
        
   
    
    return str(np.round(prediction))
    
    
    
if __name__ == "__main__":
    app.run(debug=True,port=5001) 
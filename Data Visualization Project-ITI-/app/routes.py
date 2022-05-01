from flask import render_template, current_app as app, jsonify
import numpy
from app import rf_model

from sklearn.preprocessing import StandardScaler

from app.forms import DiagnoseForm


@app.route("/", methods=['GET'])
def home():

    return render_template("home.html", title='Home')


@app.route("/diagnose", methods=['GET'])
def diagnose():
    form = DiagnoseForm()
    return render_template("diagnose.html",
                           form=form,
                           title='Diagnose')


@app.route('/diagnosis', methods=['POST'])
def diagnosis():
        form = DiagnoseForm()
        print( form.validate_on_submit())
    
    
        form_dict = form.data
        
    
        form_dict.pop('csrf_token')
        form_dict.pop('submit')
        
        print(str(form_dict))
        # log the form data
    
        # make prediction
        features = list(form_dict.values())  # create list to pass as argument to prediction function
        features[1]=int(features[1])
        features[2]=int(features[2])
        features[3]=int(features[3])
        features[4]=int(features[4])
        print(features)
        
       # sc = StandardScaler()
        #features = sc.transform(features)
        print(rf_model.predict([features]))
        prediction = 'Positive' if rf_model.predict([features]) else 'Negative' # Convert boolean result to string
        accuracy = "{:.2f}".format(round((numpy.max(rf_model.predict_proba([features])) / 1), 2))
        results = {'prediction': prediction,
                   'accuracy': accuracy}
        return results

    


@app.route("/about")
def about():
    return render_template("about.html", title='About')

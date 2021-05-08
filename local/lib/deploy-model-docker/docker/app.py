import pickle
import numpy as np
import sys
import os
import json

from sklearn.neighbors import KNeighborsClassifier

# Import Flask for creating API

from flask import Flask, request

port = int(os.environ.get("PORT", 5000))

# Load the trained model from current directory

with open('./model.pkl', 'rb') as model_pkl:

    knn = pickle.load(model_pkl)

# Initialise a Flask app

app = Flask(__name__)

# Create an API endpoint

@app.route('/predict')
def predict_iris():

    # Read all necessary request parameters

    sl = request.args.get('sl')

    sw = request.args.get('sw')

    pl = request.args.get('pl')

    pw = request.args.get('pw')

    # Use the predict method of the model to 

    # get the prediction for unseen data

    new_record = np.array([[sl, sw, pl, pw]])

    predict_result = knn.predict(new_record)

    setosa_clases = ['Setosa', 'Versicolor', 'Virginica']
    # return the result back
    return json.dumps({"predicted_class": setosa_clases[int(predict_result)]})

if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0',port=port)
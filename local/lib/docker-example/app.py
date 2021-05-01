import os
import json

# Import Flask for creating API
from flask import Flask, request

port = int(os.environ.get("PORT", 5000))


# Initialise a Flask app
app = Flask(__name__)

# Create an API endpoint
@app.route('/hello-world')
def process_request():

    # Read all necessary request parameters

    hello = 'Hello ' + request.args.get('hello')

    # return the result back
    return json.dumps({"hello": hello})

if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0',port=port)
import pip
import urllib.parse
from flask import Flask, jsonify, request
pip.main(['install','flask-restful'])

# creating the flask app
app = Flask(__name__)

#Define a dictionary with different questions and their answers
data = {
    "How to Add" : "For adding two numbers you need to use + sign in calculator",
    "What holiday happens on December 25th?":"Christmas",
    "What holiday happens on November 25th?":"Thanksgiving"
       }
#Defining API endpoint and adding code to define a route for GET requests
@app.route('/instructions', methods=['GET'])
def get_query_string():

    #Decoding the 'question' parameter from the request URL to handle special characters properly
    question = urllib.parse.unquote(request.args.get('question'))
    response = data.get(question)

    #If statement that will return response based on whether question is recognized or not and returned in JSON format
    if (response == None):
        response = "No response available for the question"
        response = jsonify(instructions=response)

    else:
        response = jsonify(instructions=response)

    return response

# driver function
if __name__ == '__main__':
    app.run(debug=False)

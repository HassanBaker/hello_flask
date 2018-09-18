from flask import Flask     # Import Flask

app = Flask(__name__)       # Instantiate a flask instance and make it a variable called 'app' so it's easier to work with.

#Generic 'Hello World' with Flask taken from http://flask.pocoo.org/docs/0.12/

@app.route('/')             # This is a definition of the '/' (index) route
def hello_world():          # This is a definition of the endpoint
    return 'Hello, World!'


# Arguments Demo.

from flask import request                   # We import request
"""
    request is a flask object that contains all the data a request has. It's up to you're endpoint to handle that request.
    A request object contains various fields that store information. We will only worry about args (arguments).
    Other fields include form, cookies, files and a lot more.
    If you want to find out more; go here http://flask.pocoo.org/docs/0.12/api/#incoming-request-data
    """

@app.route('/whats_your_name', methods=["GET"])
def what_is_your_name():

    """
    We are expecting a route that resembles this:
        /whats_your_name?name=<some_name>
    The argument we are looking for is 'name'.
    We seek the value of this argument.
    """

    your_name = request.args.get("name")        # We get the value of the argument 'name'

    return "Your name is %s" % your_name


# Lets get our templating game on

from flask import render_template           # We import render_template
"""
Render template is a flask method that renders Jinja2 static_html. 
It takes the path to the template as the first parameter.
It then takes a series of optional parameters. All of which correspond to variables described in your template file.
"""


# A basic templating demo
@app.route('/sadboi', methods=["GET"])
def sadboi():
    """
        We are expecting a route that resembles this:
            /sadboi?name=<some_name>
        """

    name = request.args.get("name")         # Again, we get a name arguement

    return render_template("template.html", name=name)  # This time we feed the value if that argument into a template
                                                        # Jinja then injects it into prewritten html


@app.route('/form', methods=['GET', 'POST'])    # Allow both post and get methods
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        form_data = request.form                # forms are immutable dictionary objects
        return render_template('success.html',
                                FIRST_NAME=form_data['first_name'],
                                SURNAME=form_data['surname'])



# from flask import session, flash
# app.secret_key = 'ssssshhh its a secret'    # A session object allows you to cache user data
#                                             # This is especially handy for logins

# @app.route('/form', methods=['GET', 'POST'])    
# def form():

#     if request.method == 'GET':
#         if 'first_name' not in session:
#             return render_template('form.html')
#         else:
#             flash('This is fetched from the session')   # A flash message is a way of quickly outputting 
#                                                         # certain messages that you don't expect to ouput frequently
#             return render_template('success.html',  
#                                 FIRST_NAME=session['first_name'],
#                                 SURNAME=session['surname'])

#     elif request.method == 'POST':
#         form_data = request.form                
#         session['first_name'] = form_data['first_name']
#         session['surname'] = form_data['surname']
#         return render_template('success.html',  
#                                 FIRST_NAME=form_data['first_name'],
#                                 SURNAME=form_data['surname'])

import requests
from config import API_KEY
@app.route('/demo', methods=['GET'])
def demo():
    url = "http://www.hostedgraphite.com/api/v1/sink"
    response = requests.put(url, auth = (API_KEY, ""), data="hello_hg 1")
    print (response.status_code)
    return 'You have posted a metric'


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
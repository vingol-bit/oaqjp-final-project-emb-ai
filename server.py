# Import the Flask class from the flask module --->flask --app server --debug run
from flask import Flask, make_response, request, render_template

# Create an instance
#
# of the Flask class, passing in the name of the current module
app = Flask(__name__)

# root application
@app.route("/")
def render_index_page(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
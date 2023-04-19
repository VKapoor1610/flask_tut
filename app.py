# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#   return "HELLO Vihan"

# if __name__ == '__main__' : 
#   app.run(host='0.0.0.0' , debug=True)

from flask import Flask
# import the Flask class from flask module 

# then create an app object of type('Flask')
app = Flask(__name__)

# set the route of the app
@app.route("/") #@ is decorator function 
def func():
  return "Hello" #just below the route wrote the corresponding function 

# way to run a flask program 
if __name__ == "__main__" : 
  app.run(host= '0.0.0.0' , debug=True)





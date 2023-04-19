from flask import Flask, render_template, jsonify
# import the Flask class from flask module

# then create an app object of type('Flask')
app = Flask(__name__)

data = ['Vihan', 'Kapoor', 'Payal']

# data = [{} , {]


# set the route of the app
@app.route("/")  #@ is decorator function
def func():
  return render_template(
    'home.html',
    data=data)  #just below the route wrote the corresponding function

@app.route("/api/user_info")
def fun1():
  return jsonify(data)
# for sending data in form of data variable we use this format

# way to run a flask program
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

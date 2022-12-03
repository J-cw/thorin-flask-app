from flask import Flask

app = Flask(__name__)
#Creates instance of Flask class and storing in variable "app"

@app.route("/")
def index():
    return "Hello, World!"
#Decorator wraps functions, when we browse to root director fucntion is triggered.



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True)
#Gets IP if exists else set to default value, same with port. Debug true to allow easier debugging durin dev
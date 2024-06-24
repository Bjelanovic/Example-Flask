#using multiple routes in single method
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Hello World!"
  

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "Hello World"}

if __name__ == "__main__":
    app.run(debug=True)

#curl -X GET -i -w '\n' localhost:5000-  TO TEST HOST
  

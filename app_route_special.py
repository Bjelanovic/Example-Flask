@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for  "+userid

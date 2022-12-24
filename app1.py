from flask import Flask , jsonify,render_template,request,redirect,url_for
from utils1 import MagicHome
import config1

app = Flask(__name__)

@app.route("/")
def hello_flask():
        print("Welcome to MagicHome House price prediction")
        # return "hello" 
        return render_template("home.html")
    
@app.route("/MagicHome_price",methods = ["GET","POST"])

def predict():
    
    if request.method == "POST":
        print("We are in Post method")
        
        imp_data = request.form
        print("Input Data",imp_data)
        
        Area        = eval(request.form["Area"])
        BHK         = eval(request.form["BHK"])
        Bathroom    = eval(request.form["Bathroom"])
        Parking     = eval(request.form["Parking"])
        Per_Sqft    = eval(request.form["Per_Sqft"])
        Type        = request.form["Type"]
        Furnishing  = request.form["Furnishing"]
        Status      = request.form["Status"]
        Transaction = request.form["Transaction"]
        
        print("Area, BHK, Bathroom, Parking, Per_Sqft, Type, Furnishing, Status, Transaction",Area, BHK, Bathroom, Parking, Per_Sqft, Type, Furnishing, Status, Transaction)
        MagicHome_price = MagicHome(Area, BHK, Bathroom, Parking, Per_Sqft, Type, Furnishing, Status, Transaction)
        price = MagicHome_price.get_predicted_price()
        
        # return jsonify({"Price": price})
        return render_template("home.html",prediction = price)
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config1.PORT_NUMBER)
    
        
    
        
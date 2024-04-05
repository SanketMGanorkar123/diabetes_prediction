from flask import Flask,jsonify,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods= ["post"])
def diabetic_pred():
     
    with open("model.pkl","rb") as model:
        ml_model = pickle.load(model)
    
    data = request.form
    Glucose = eval(data["Glucose"])
    BloodPressure = eval(data["BloodPressure"])
    SkinThickness = eval(data["SkinThickness"])
    Insulin = eval(data["Insulin"])
    BMI = eval(data["BMI"])
    DiabetesPedigreeFunction = eval(data["DiabetesPedigreeFunction"])
    Age = eval(data["Age"])

    result = ml_model.predict([[Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]) 
    
    if result[0] == 0:
        Diabetic = render_template("index0.html")
    if result[0] == 1:
        Diabetic = render_template("index1.html")  

    return Diabetic

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
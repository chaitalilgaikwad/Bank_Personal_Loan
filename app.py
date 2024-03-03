from flask import Flask,render_template,url_for,request
from flask import jsonify
from utils import get_loan_approval
# import config

#initialise flask application
app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index1.html')

#define route
@app.route('/predicted_bank_loan',methods = ['POST'])
def predicted_bank_loan():
    #data = request.form
    
    Age = float(request.form['Age'])
    Experience = float(request.form['Experience'])
    Income = float(request.form['Income'])
    Family = float(request.form['Family'])
    CCAvg = float(request.form['CCAvg'])
    Education = float(request.form['Education'])
    Mortgage = float(request.form['Mortgage'])
    Securities_Account = float(request.form['Securities_Account'])
    CD_Account = float(request.form['CD_Account'])
    Online = float(request.form['Online'])
    CreditCard = float(request.form['CreditCard'])

    loan_result = get_loan_approval(Age,Experience,Income,Family,CCAvg,Education,Mortgage,Securities_Account,CD_Account,Online,CreditCard)
    print("Loan Approval Status:",loan_result)
    
    status_class =  "Will take a personal loan" if loan_result == 1 else "Will not take a personal loan"

    return render_template('index1.html', prediction_text = status_class)

    return jsonify({"Response":"Successful",
                    'Result':f"Predicted Class for Bank Loan Approval is : Class{loan_result}"})

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 5004,debug = False)
    #app.run(debug = False)

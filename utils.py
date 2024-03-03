import pickle
import config
import numpy as np
import json

def get_loan_approval(Age,Experience,Income,Family,CCAvg,Education,Mortgage,Securities_Account,CD_Account,Online,CreditCard):
    model_f_path = r"artifacts/Random_forest_Bank_Loan.pkl"
    with open(model_f_path,'rb') as ftr:
         rf_model= pickle.load(ftr)
    
    with open(config.COLUMN_DATA_JSON, 'r') as f:
          col_data = json.load(f)
     
#     col_names = rf_model.feature_names_in_
    
   
    test_array = np.zeros((1,rf_model.n_features_in_))
    test_array[0,0] = Age
    test_array[0,1] = Experience
    test_array[0,2] = Income
    test_array[0,3] = Family
    test_array[0,4] = CCAvg
    test_array[0,5] = Education
    test_array[0,6] = Mortgage
    test_array[0,7] = Securities_Account
    test_array[0,8] = CD_Account
    test_array[0,9] = Online
    test_array[0,10] = CreditCard
    
#     test_input = np.array([[Age,Experience,Income,Family,CCAvg,Education,Mortgage,Securities_Account,CD_Account,Online,CreditCard]])
    pecdicted_class = rf_model.predict(test_array)
    return pecdicted_class
    
from joblib import load
import pandas as pd
import os

# get the base address
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = load(os.path.join(BASE_DIR, 'artifacts/model.joblib'))
scaler_with_cols=load(os.path.join(BASE_DIR,'artifacts/scaler.joblib'))

def model_prediction(df):
    scaler=scaler_with_cols['scaler']
    x_scaled=scaler.transform(df)
    output=model.predict(df)
    return output

def predict(input_dict):
    df=pd.DataFrame([[0]*len(scaler_with_cols['feature_columns'])],columns=scaler_with_cols['feature_columns'])
    df.loc[0]['Age']=input_dict['Age']
    df.loc[0]['Tenure']=input_dict['Tenure']
    df.loc[0]['MonthlyCharges']=input_dict['MonthlyCharges']

    # for gender
    if input_dict['Gender']=='Male':
        df.loc[0]['Gender_Male']=1
    else:
        df.loc[0]['Gender_Male']=0
     
    # for contract
    if input_dict['ContractType']=='Month-to-month':
        df.loc[0]['ContractType_One-Year']=0
        df.loc[0]['ContractType_Two-Year']=0
    elif input_dict['ContractType']=='One year':
        df.loc[0]['ContractType_One-Year']=1
        df.loc[0]['ContractType_Two-Year']=0
    else:
        df.loc[0]['ContractType_One-Year']=0
        df.loc[0]['ContractType_Two-Year']=1

    # for InternetService
    if input_dict['InternetService']=='DSL':
        df.loc[0]['InternetService_Fiber Optic']=0
        df.loc[0]['InternetService_No']=0
    elif input_dict['InternetService']=='Fiber optic':
        df.loc[0]['InternetService_Fiber Optic']=1
        df.loc[0]['InternetService_No']=0
    else:
        df.loc[0]['InternetService_Fiber Optic']=0
        df.loc[0]['InternetService_No']=1

    # for TechSupport
    if input_dict['TechSupport']=='Yes':
        df.loc[0]['TechSupport_Yes']=1
    else:
        df.loc[0]['TechSupport_Yes']=0
    
    return model_prediction(df)

    




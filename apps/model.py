from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google.oauth2 import service_account
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pickle
import gdown

SCOPES = ['https://www.googleapis.com/auth/drive']

@st.cache_resource
def downloadModels():
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['DATA']}", 'data.csv', quiet=False)
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['LOGISTIC']}", 'logistic_regression.pkl', quiet=False)
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['DECISION_TREE']}", 'decision_tree.pkl', quiet=False)
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['RANDOM_FOREST']}", 'random_forest.pkl', quiet=False)
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['SVM']}", 'support_vector_machine.pkl', quiet=False)
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['KNN']}", 'k_nearest_neighbors.pkl', quiet=False)
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['NAIVE_BAYES']}", 'naive_bayes.pkl', quiet=False)
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['XGB']}", 'xgboost.pkl', quiet=False)
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['VOTING']}", 'voting_classifier.pkl', quiet=False)

def load_models():
    models = {
        'Logistic Regression': pickle.load(open('logistic_regression.pkl', 'rb')),
        'Decision Tree': pickle.load(open('decision_tree.pkl', 'rb')),
        'Random Forest': pickle.load(open('random_forest.pkl', 'rb')),
        'Support Vector Machine': pickle.load(open('support_vector_machine.pkl', 'rb')),
        'K-Nearest Neighbors': pickle.load(open('k_nearest_neighbors.pkl', 'rb')),
        'Naive Bayes': pickle.load(open('naive_bayes.pkl', 'rb')),
        'XGBoost': pickle.load(open('xgboost.pkl', 'rb')),
        'Voting Classifier': pickle.load(open('voting_classifier.pkl', 'rb'))
    }
    return models

def modelPredict():
    downloadModels()
    df = pd.read_csv('data.csv')

    min_date = datetime.datetime.today() + datetime.timedelta(days=1)
    date = st.date_input("Enter the date:", value=min_date, min_value=min_date)

    is_weekday = 1 if (date.weekday() in [5, 6]) else 0
    last_row_status = df.iloc[-1]['Status']
    last_row2_status = df.iloc[-2]['Status']
    last_row3_status = df.iloc[-3]['Status']
    rolling_3 = (last_row_status + last_row2_status + last_row3_status) / 3

    input_features = np.array([[date.weekday(), date.day, date.month, date.year, is_weekday, last_row_status, rolling_3]])
    models = load_models()
    if st.button("Predict"):
        for model_name, model in models.items():
            prob = model.predict_proba(input_features)[0][1]
            st.info(f"{model_name} predicts: {prob:.2f}")

@st.cache_resource
def get_drive_service():
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['SERVICE_ACCOUNT_FILE']}", 'credentials.json', quiet=False)
    creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)


def upload_to_drive(file_path, file_id):
    try:
        media = MediaFileUpload(file_path, mimetype='application/csv', resumable=True)
        service = get_drive_service()
        request = service.files().update(fileId=file_id, media_body=media, body=file_path)
        response = request.execute()
        st.success("File updated successfully!")
        return response
    except Exception as e:
        st.error(f"An error occurred while uploading: {e}", icon="🚫")
        return None

def saveData():
    data = pd.read_csv('data.csv')
    today = datetime.datetime.today().date()
    status = st.selectbox(f"What's the status of {today}? Present | Absent", ['Present', 'Absent'])

    if st.button('Save Data'):
        new_row = pd.DataFrame({
            'Date': [today],
            'Status': [1 if status == 'Present' else 0]
        })
        data = pd.concat([data, new_row], ignore_index=True)
        data.to_csv('data.csv', index=False)
        upload_to_drive('data.csv', st.secrets['DATA'])
        st.toast(f"Status for {today} has been saved successfully!", icon="✅")

def modelApp():
    choiceM = st.selectbox("Are you want to see model prediction or save today's data?", ['Model Prediction', 'Save Data'])
    if choiceM == 'Model Prediction':
        modelPredict()
    else:
        saveData()

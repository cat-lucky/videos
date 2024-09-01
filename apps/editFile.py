from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import streamlit as st
import gdown
import json

FILE = {"ANIMATED WORLD": "ACG", "LIVE ACTION MOVIES": "LAM"}
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_drive_service():
    gdown.download(f"https://drive.google.com/uc?id={st.secrets['SERVICE_ACCOUNT_FILE']}", 'credentials.json', quiet=False)
    creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)

service = get_drive_service()

def load_json(JSON_FILE_PATH):
    with open(JSON_FILE_PATH, 'r') as file:
        return json.load(file)

def save_json(JSON_FILE_PATH, data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def upload_to_drive(file_path, file_id):
    try:
        media = MediaFileUpload(file_path, mimetype='application/json', resumable=True)
        request = service.files().update(fileId=file_id, media_body=media, body=file_path)
        response = request.execute()
        st.success("File updated successfully!")
        return response
    except Exception as e:
        st.error(f"An error occurred while uploading: {e}", icon="🚫")
        return None

def load_data(file_id):
    try:
        gdown.download(f"https://drive.google.com/uc?id={file_id}", f'{file_id.lower()}.json', quiet=False)
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}", icon="🚫")
        return False

def editFile():
    choice = st.selectbox("Which file do you want to edit?", [None] + list(FILE.keys()))

    if choice:
        file_id = st.secrets[FILE[choice]]
        JSON_FILE_PATH = f'{FILE[choice].lower()}.json'
        
        if load_data(file_id):
            service = get_drive_service()
            data = load_json(JSON_FILE_PATH)
            action = st.radio("What would you like to do?", ["Add New Entry", "Edit Existing Entry"])

            if action == "Edit Existing Entry":
                updateEntry(data, JSON_FILE_PATH, file_id)
            elif action == "Add New Entry":
                addNewEntry(data, JSON_FILE_PATH, file_id)

def updateEntry(data, JSON_FILE_PATH, file_id):
    if len(data) > 0:
        entry_ids = [str(entry["ID"]) for entry in data]
        entry_id = st.selectbox("Select ID to edit:", entry_ids)
        
        entry_to_edit = next((entry for entry in data if str(entry["ID"]) == entry_id), None)

        if entry_to_edit:
            with st.form(key='edit_entry_form'):
                ID = st.text_input("ID", value=str(entry_to_edit["ID"]), disabled=True)
                category = st.text_input("Category", value=entry_to_edit["category"])
                name = st.text_input("Name", value=entry_to_edit["name"])

                col1, col2, col3 = st.columns(3)
                time = entry_to_edit["timeStamp"]
                with col1:
                    hour = st.number_input("Hour", value=time // 3600)
                with col2:
                    minute = st.number_input("Minute", value=(time % 3600) // 60)
                with col3:
                    second = st.number_input("Second", value=time % 60)
                    
                boyName = st.text_area("Boy Name (comma-separated)", value=", ".join(entry_to_edit["boyName"]))
                girlName = st.text_area("Girl Name (comma-separated)", value=", ".join(entry_to_edit["girlName"]))
                tags = st.text_area("Tags (comma-separated)", value=", ".join(entry_to_edit["tags"]))
                imageURL = st.text_input("Image URL", value=entry_to_edit["imageURL"])
                iFrameURL = st.text_input("iFrame URL", value=entry_to_edit["iFrameURL"])
                videoURL = st.text_input("Video URL", value=entry_to_edit["videoURL"])
                downloadURL = st.text_input("Download URL", value=entry_to_edit["downloadURL"])
                websiteURL = st.text_input("Website URL", value=entry_to_edit["websiteURL"])

                submit_button = st.form_submit_button(label='Save Changes')

                if submit_button:
                    updated_entry = {
                        "ID": int(ID) if ID.isdigit() else ID,
                        "category": category,
                        "name": name,
                        "timeStamp": int(hour) * 3600 + int(minute) * 60 + int(second),
                        "boyName": [name.strip() for name in boyName.split(",") if name.strip()],
                        "girlName": [name.strip() for name in girlName.split(",") if name.strip()],
                        "tags": [tag.strip() for tag in tags.split(",") if tag.strip()],
                        "imageURL": imageURL,
                        "iFrameURL": iFrameURL,
                        "videoURL": videoURL,
                        "downloadURL": downloadURL,
                        "websiteURL": websiteURL
                    }

                    for index, entry in enumerate(data):
                        if str(entry["ID"]) == entry_id:
                            data[index] = updated_entry
                            break
                    save_json(JSON_FILE_PATH, data)
                    upload_to_drive(JSON_FILE_PATH, file_id)

    else:
        st.warning("No data available to edit.")

def addNewEntry(data, JSON_FILE_PATH, file_id):
    with st.form(key='add_entry_form'):
        new_ID = len(data) + 1
        st.write(f"ID: {new_ID}")
        
        category = st.text_input("Category")
        name = st.text_input("Name")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            hour = st.number_input("Hour", min_value=0, value=0)
        with col2:
            minute = st.number_input("Minute", min_value=0, value=0)
        with col3:
            second = st.number_input("Second", min_value=0, value=0)

        timeStamp = int(hour) * 3600 + int(minute) * 60 + int(second)
        
        boyName = st.text_area("Boy Name (comma-separated)")
        girlName = st.text_area("Girl Name (comma-separated)")
        tags = st.text_area("Tags (comma-separated)")
        imageURL = st.text_input("Image URL")
        iFrameURL = st.text_input("iFrame URL")
        videoURL = st.text_input("Video URL")
        downloadURL = st.text_input("Download URL")
        websiteURL = st.text_input("Website URL")

        submit_button = st.form_submit_button(label='Add Entry')

        if submit_button:
            new_entry = {
                "ID": new_ID,
                "category": category,
                "name": name,
                "timeStamp": timeStamp,
                "boyName": [name.strip() for name in boyName.split(",") if name.strip()],
                "girlName": [name.strip() for name in girlName.split(",") if name.strip()],
                "tags": [tag.strip() for tag in tags.split(",") if tag.strip()],
                "imageURL": imageURL,
                "iFrameURL": iFrameURL,
                "videoURL": videoURL,
                "downloadURL": downloadURL,
                "websiteURL": websiteURL
            }

            data.append(new_entry)
            save_json(JSON_FILE_PATH, data)
            upload_to_drive(JSON_FILE_PATH, file_id)

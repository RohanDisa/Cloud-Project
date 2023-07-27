import streamlit as st
import os
import subprocess
import tp1
from tp1 import encryption,decryption
import enc
from enc import encrypt
import s3
from s3 import s3_upload

# Define function for homepage
def home():
    st.title("Homepage")
    st.write("Welcome to the Upload/Download Web App!")

# Define function for upload page
def upload():
    st.title("Upload Video")
    video_path = st.text_input("Enter the path of the video file:")
    if video_path:
        st.success("Video path uploaded successfully!")
        st.video(video_path)
       # filename=f"""\"{video_path}\"""".
        #encryption(video_path)
        #encrypt()
        #s3_upload()
    
        return video_path

# Define function for download page
def download():
    st.title("Download File")
    if os.path.exists("uploads"):
        file_list = os.listdir("uploads")
        if len(file_list) > 0:
            selected_file = st.selectbox("Select a file", file_list)
            if st.button("Download"):
                with open(os.path.join("uploads", selected_file), "rb") as f:
                    file_contents = f.read()
                st.download_button("Download", file_contents)
        else:
            st.warning("No files uploaded yet.")
    else:
        st.warning("No files uploaded yet.")

# Define function for about page
def about():
    st.title("About")
    st.write("This web app was created by me.")

# Set up the app layout
st.set_page_config(page_title="Upload/Download Web App")
pages = {
    "Homepage": home,
    "Upload": upload,
    "Download": download,
    "About": about
}
selection = st.sidebar.radio("Go to", list(pages.keys()))
page = pages[selection]
page()
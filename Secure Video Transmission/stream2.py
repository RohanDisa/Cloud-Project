import streamlit as st
import os
import subprocess
import tp1
from tp1 import vidtotext,texttovid
import enc
from enc import encrypt
import s3
from s3 import s3_upload,check_file_exists,downloadfile
import hash
from hash import hashing,hashVerification
import dec
from dec import decrypt

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
        vidtotext(video_path)
        encrypt()
        hashing()
        s3_upload()
        return video_path

# Define function for download page
def download():
    st.title("Download File")
    bucket_name = 'rohan1090'
    file_key = 'file.enc'
    filename="D:\\cloud\\Huffman-Coding\\decrypted_text_file.txt"
    if check_file_exists(bucket_name,file_key):
        def on_download_click():
           downloadfile()
           hashVerification()
           decrypt()
           texttovid(filename)
        if st.button("Download"):
           on_download_click()
        

# Create a button with the label "Download"


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
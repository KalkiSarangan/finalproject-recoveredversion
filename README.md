# final-flask

This application is intended to be used by an xray technician/medical professional to be able to login using their credentials, submit an image of an xray and the image would be used by an image classification model to determine whether the patient has osteoarthritis and the severity. An administrator of the website would be able to log in using their credentials to tell how many times each page was accessed.

# To use the app:

- mkdir final_project
- git clone https://github.com/KalkiSarangan/final-flask.git
- cd final-flask
- docker-compose up
- navigate to 127.0.0.1:5000/home
- docker-compose stop

##http://127.0.0.1:5000/ and http://127.0.0.1:5000/home

This is the landing page that currently just contains a title.

##http://127.0.0.1:5000/xray

This is the page where an authorized user can login to upload the image of the xray. For the sake of this project the username is 'technician' and the password is 'xray'. Upon login the user gets redirected to http://127.0.0.1:5000/upload

##http://127.0.0.1:5000/upload

This is the page that a technician uses to upload an image of a patient's xray to determine the result. They can choose the 'Choose File' button to choose the image of the xray and the 'Upload File' button to upload the image which gets saved in the 'files' folder.

The intention of this page is that when the image is uploaded, the user gets redirected to http://127.0.0.1:5000/predict which is currently not working due to an error with the PIL/pillow module.

##http://127.0.0.1:5000/predict

This is the page that would use the model to return the prediction of whether the patient has osteoarthritis and the severity of it. This page is currently not working due to an issue with the model and how it's incorporated into flask.

##http://127.0.0.1:5000/admin

This is the page where an admin of the website can log in to access information regarding the website. For the sake of this projectthe username is 'admin' and the password is 'secret'. Upon login the user is taken to a page containing statistics of how many times each page was visited.

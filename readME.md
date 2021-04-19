# **Residence Service System** 

## **About**

A web app for students and staff to submit, manage, and view complaints, maintenance requests, food orders, and packages.

## **Developers:**

- Firoz Lakhani
- Rohan Amjad
- Sajid Hafiz

## **How to run this program** 

### **Backend Django Server**

To run the Django backend ensure Python 3 is correctly installed on your system.

Start by navigating to the ***Residence_Service_System*** directory using: `cd /Residence_Service_System`

Then activate the Python 3 virtual environment using: `. env/bin/activate`

*You can use your own personal Python 3 virtual environment, however make sure to install all Python 3 dependencies from requirements.txt using: `pip install -r requirements.txt`*

Once the Python 3 environment is set up and all dependencies are installed, you can start the backend server using: `python manage.py runserver` 

### **Frontend Vue Client**

To run the Vue client ensure NodeJS and NPM are correctly installed on your system.

Start by navigating to the ***Residence_Service_System/frontend_vue*** directory using: `cd /Residence_Service_System/frontend_vue`

Install all Node dependencies using: `npm install`

Once all Node dependencies are installed, you can start the Vue client using: `npm run serve`

## **Testing the backend and frontend**
*Note: This app uses JWT authentication and all API andpoints except api/register are protected, ensure you are sending a valid JWT in your HTTP request header to perform any requests, otherwise all requests will be blocked*

*Note: This app is protected with CORS, ensure your frontend client is whitelisted in CORS_WHITELIST in settings.py in order to access the access the API from external clients*

*Note: Postman Desktop client is required to send requests through Postman*

*Note: Additonal accounts can be registered by visiting the web app and registering or making a post request to api/register/{accounttype}*

## Login Details

**Student**

Email: samplestudent@gmail.com
Password: fakepass123

**Admin**

Email: sampleadmin@gmail.com
Password: fakepass123

**Tech**

Email: sampletech@gmail.com
Password: fakepass123

**Staff**

Email: samplestaff@gmail.com
Password: fakepass123

**Chef**

Email: samplechef@gmail.com
Password: fakepass123





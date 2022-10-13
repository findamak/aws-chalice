# Setup

Create a new directory and change directories.
```sh
mkdir chalice && cd chalice
```
Setup your python virtual env and install the chalice and twilio modules.
```sh
python3.8 -m venv venv
source venv/bin/activate
pip install chalice
pip install twilio
```
Create a new chalice project. Enter the project name and use the arrows to select project type to be `Lambda functions only`. 
```sh
chalice new-project
```
This creates a new folder using your project name and also boilerplate files and directories as shown. Change directory into this new folder.
```
drwxr-xr-x .
drwxr-xr-x ..
drwxr-xr-x .chalice
-rw-r--r-- .gitignore
-rw-r--r-- app.py
drwxr-xr-x chalicelib
-rw-r--r-- requirements-dev.txt
-rw-r--r-- requirements.txt
drwxr-xr-x tests
```
Create a `.chalice/config.json` file to store environment variables. You will need your twilio details as shown below.
```json
{
  "version": "2.0",
  "app_name": "testapp",
  "stages": {
    "dev": {
      "api_gateway_stage": "api",
      "environment_variables": {
        "ACCOUNT_SID": "<Twilio account SID>",
        "AUTH_TOKEN": "<Twilio auth token>",
        "FROM_NUMBER": "<Twilio number assigned to you>",
        "TO_NUMBER": "<Destination number to send SMS>"
      }
    }
  }
}
```
Download the `app.py` and `chalicelib/sms.py` files from this repository into the respective locations in your project folder.

Tell AWS chalice what modules need to be installed to run your Python lambda function.
```sh
pip freeze > requirements.txt
```
Now start the application on your local machine.
```sh
chalice local
```
Test that the application running locally works.
```sh
curl -H "Content-Type: application/json" -X POST -d '{"msg": "How are you?"}' http://localhost:8000/service/sms/send
```
You should get a response similar to:
```
{"status":"success","data":"SM484ae8518dbd738f9230c49588bb1083","message":"SMS successfully sent"}
```
Now deploy to AWS.
```sh
chalice deploy
```
Once deployed you should see.
```
Creating deployment package.
Creating IAM role: testapp-dev
Creating lambda function: testapp-dev
Creating Rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:ap-southeast-2:<removed>:function:testapp-dev
  - Rest API URL: https://dbnur1ft85.execute-api.ap-southeast-2.amazonaws.com/api/
```
To test it is working, run the previous curl command but using the new URL.
```sh
curl -H "Content-Type: application/json" -X POST -d '{"msg": "How are you?"}' https://dbnur1ft85.execute-api.ap-southeast-2.amazonaws.com/api/service/sms/send
```
Now to delete your lambda function, run:
```sh
chalice delete
```
The resources will be deleted.
```
Deleting Rest API: dbnur1ft85
Deleting function: arn:aws:lambda:ap-southeast-2:<removed>:function:testapp-dev
Deleting IAM role: testapp-dev
```
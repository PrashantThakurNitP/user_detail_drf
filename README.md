# user_detail_drf
Api URl
http://details.pythonanywhere.com/api/create_detail

This API was developed using Django Restframework

It accept name,email,dateofbirth and mobile_no as Post request and save it in database

After that it will send email as confirmation on above email

It also verify age and phone no of user

After saving above data it show the above data in JSON format


Make sure python and pip is installed and is set to path
To start project run command

python -m venv uservenv  #create virtual environment

Go inside virtual environment and activate it

Scripts\activate.bat   #activate virtual environment

install dependency in virtual environment by below command

pip install -r requirements.txt  #install dependency

create .env file and store your email, email password ,security key in it and add .env file in .gitignore

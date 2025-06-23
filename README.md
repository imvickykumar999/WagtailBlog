# Wagtail Blog

    docker pull imvickykumar999/cleanblog-wagtail
    docker run -p 8000:8000 imvickykumar999/cleanblog-wagtail

![image](https://github.com/user-attachments/assets/2c914d09-886a-4bfe-8276-63c47cd0b267)
![image](https://github.com/user-attachments/assets/a6d34ead-c674-49d8-b33f-a853dba98364)

## Steps to run:

Terminal 1

- unzip supreme.zip
- python3 -m venv .venv
- source .venv/bin/activate # (ubuntu)
- .venv\Scripts\activate # (windows)
- pip install -r requirements.txt
- python manage.py runserver

Terminal 2

- docker pull ngrok/ngrok
- docker run --net=host -it -e NGROK_AUTHTOKEN=YOUR_NGROK_AUTHTOKEN ngrok/ngrok:latest http --url=free-camel-deadly.ngrok-free.app 8000

![image](https://github.com/user-attachments/assets/a050af43-7d7f-47f8-a872-1d1242d5adf5)
![image](https://github.com/user-attachments/assets/473eb9e9-6ac6-438f-b9cd-df1b13810f1d)
![image](https://github.com/user-attachments/assets/d03f8a71-3eae-4c4a-8508-fb839f1f62cb)

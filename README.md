# WagtailBlog
https://free-camel-deadly.ngrok-free.app/django-admin/

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

# Background Remove by using Python Django

To setup this project:\
virtualenv venv\
for Linux/Mac:   <br>
  source venv/bin/activate\
  pip3 install -r requirements.txt\
  python3 manage.py runserver
  <br>
for Windows: <br>
  source venv/Scripts/activate\
  pip install -r requirements.txt\
  python manage.py runserver
  
<br>
Upload image to this endpoint with background then it will return image after removing the bg\

  Endpoint: http://localhost:8000/remove-bg/
  <br>
  input name:
    image 'my-photo.png'
  <br>
  it will return 'media/my-photo.png' 
  <br>
Then you can get the file here   http://localhost:8000/media/my-photo.png

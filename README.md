# Background Remove by using Python Django

To setup this project:\
virtualenv venv\
for Linux/Mac: \
  source venv/bin/activate\
  pip3 install -r requirements.txt\
  python3 manage.py runserver
for Windows: \
  source venv/Scripts/activate\
  pip install -r requirements.txt\
  python manage.py runserver
  

Upload image to this endpoint with background then it will return image after removing the bg\

  Endpoint: http://localhost:8000/remove-bg/
  \
  \input name:\ 
    image 'my-photo.png'
\
  it will return 'media/my-photo.png' \ 

Then you can get the file here   http://localhost:8000/media/my-photo.png

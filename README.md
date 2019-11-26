### Dependencies

Python 3 
 * Django 
 * Gentelella template
 * 


### Usage
```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
 
python manage.py makemigrations
python manage.py migrate
# you need to start with a father menu with id 0
# you need to start with a father Departmet with id 0
python manage.py runserver
```

### Note
Make sure you call 'bower install' before 'collectatic'

FIRTS ->`` $ python manage.py bower install ``

THEN -> ``$ python manage.py collectstatic``
Tutorial:
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04-es

`Crear un entorno virtual:`
python -V
output: Python 3.8.10

python3 -m venv dulcesito_venv
source dulcesito_venv/bin/activate

Requirements:
pip install -r requirements.txt

Test local server:
python manage.py runserver 0:8000

15.188.81.240:8000

Crear carpetas para la galeria de fotos:
"comando para hacer el build"

test gunicorn:
gunicorn --bind 0.0.0.0:8000 Dulcesyto.wsgi

#### Comandos para docker y docker compose
docker compose up -d
docker compose down 
docker compose ps
docker exec -it dulcesyto-dulcesyto-1 bash
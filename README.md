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

Crear unix socket para gunicorn:
sudo nano /etc/systemd/system/gunicorn.socket
###########################
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

###########################

Crear service para gunicorn:
sudo nano /etc/systemd/system/gunicorn.service
###########################
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=marcelo
Group=www-data
WorkingDirectory=/home/marcelo/github_projects/Dulcesyto
ExecStart=/home/marcelo/github_projects/Dulcesyto/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          Dulcesyto.wsgi

[Install]
WantedBy=multi-user.target

###########################
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket



Tutorial:
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04-es

`Crear un entorno virtual:`
python -V
output: Python 3.8.6
python -m virtualenv venv

Requirements:
pip install django==3.1.3 gunicorn==20.0.4

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



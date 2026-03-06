# djangotutorial
<pre>
Debian 13 (Trixie)

apt update

apt install apache2
a2enmod proxy proxy_http proxy_reverse
systemctl restart apache2

nano /etc/apache2/sites-enabled/000-default.conf
&lt;VirtualHost *:80&gt;
        ProxyPreserveHost On
        ProxyPass / http://127.0.0.1:8000/
        ProxyPassReverse / http://127.0.0.1:8000/
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
&lt;/VirtualHost&gt;

apt install python3-pip
apt install python3.13-venv
cd /opt
python3 -m venv django
source django/bin/activate
python -m pip install Django
python -m django --version
cd django
django-admin startproject mysite djangotutorial
rm -fr djangotutorial
git clone https://github.com/usbport11/djangotutorial
cd djangotutorial
python manage.py runserver
</pre>
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

# Before start channels (/chat)
<pre>
apt install redis-server
cd /opt/django
rm -fr djangotutorial
git clone https://github.com/usbport11/djangotutorial
source bin/activate
pip install -U 'channels[daphne]'
pip install channels_redis
cd djangotutorial
python manage.py runserver
</pre>

# WS Apache
<pre>
a2enmod rewrite
systemctl restart apache2

&lt;VirtualHost *:80&gt;
        ProxyPreserveHost On
        &lt;Location /&gt;
                ProxyPass http://127.0.0.1:8000/
                ProxyPassReverse http://127.0.0.1:8000/
        &lt;/Location&gt;
        &lt;Location /chat/&gt;
                ProxyPass http://127.0.0.1:8000/chat/
                ProxyPassReverse http://127.0.0.1:8000/chat/
                RewriteEngine On
                RewriteCond %{HTTP:Connection} Upgrade [NC]
                RewriteCond %{HTTP:Upgrade} websocket [NC]
                RewriteRule /(.*) ws://127.0.0.1:8000/$1 [P,L]
        &lt;/Location&gt;

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
&lt;/VirtualHost>
</pre>

# WS Nginx
<pre>
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;
        location / {
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_pass http://127.0.0.1:8000;
        }
        location /chat/ {
                proxy_pass http://127.0.0.1:8000/chat/;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
        }
}
</pre>

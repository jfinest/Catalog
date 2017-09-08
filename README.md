# README

## Overview:
Ever read a book that you found interesting enough that you would like to recommend to others? Well, this web application lets you do just that. If you are someone whom just read a book and want to recommend it then simply log in and add the book to the list. Vice versa if you are someone whom is looking for a book to read that others recommend then this is a good place to do so.
This will let you take a linux sever to host Web Application.

## Instructions:
1. Clone the project to your local machine
2. Move the LinuxProject sshkey to the .ssh folder in your local machine
3. To log into server use ssh grader@54.236.241.116 -p 2200 -i ~/.ssh/LinuxProject
4. Password for RSA key is:  ASDFGH
5. Password for running sudo command(this is capitalized letters 'x'): XXXXXX
6. Run following commands to update all currently installed pakages:
    1. sudo apt-get update
    2. sudo apt-get upgrade
7. Changing SSH port from 22 to 2200:
    1. sudo nano /ect/ssh/sshd_config
    2. change "Port 22" to "Port 2200"
    3. save & quit
    4. reload SSH using command:  sudo service ssh restart
8. Finally configure the Uncomplicated Firewall (ufw)
    1. The below link can be helpful on how to setup ufw and enabling it.
        * https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-16-04
9. To visit project on web browser visit http://ec2-54-236-241-116.compute-1.amazonaws.com
10. Certain dependencies required to run are apache2 webserver, mod_wsgi, sqlalchemy, psycopg2, flask, postgres db. You can try running pip install requirements.txt or follow directions by googling the resepective to install.
11. Postgres db is setup as follows: db name=catalog, db username/role="catalog" with password="catalog123", Ubuntu username="catalog". The db console can be accessed by changing user to "catalog" $ su catalog and then $ psql into the console as the "catalog" user.
12. Setting up mod_wsgi: The wsgi file name is "catalog.wsgi" and found in /var/www/Catalog. The virutal host config must be changed to reflect the new file name. sudo nano /etc/apache2/sites-enabled/000-default.conf and add the following line at the end of the <VirtualHost *:80> block, right before the closing .... WSGIScriptAlias / /var/www/Catalog/catalog.wsgi . Run the command sudo apache2ctl restart to activate the config change.
13. To setup app do following: 
    1.Create the database by running: python database_setup.py
    2.To populate the db with a bulk list of books then run: python book_list.py
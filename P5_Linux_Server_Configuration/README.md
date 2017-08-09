# P5_Linux-Server-Configuration

## Project Overview
  * You will take a baseline installation of a Linux server and prepare it to host your web applications. 
  * You will secure your server from a number of attack vectors, install and configure a database server, 
  and deploy one of your existing web applications onto it.

## Why this Project?
  * A deep understanding of exactly what your web applications are doing, how they are hosted, and the 
  interactions between multiple systems are what define you as a Full Stack Web Developer. 
  * In this project, you’ll be responsible for turning a brand-new, bare bones, Linux server into the
  secure and efficient web application host your applications need.

## What will I Learn?
  * You will learn how to access, secure, and perform the initial configuration of a bare-bones Linux server. 
  * You will then learn how to install and configure a web and database server and actually host a web application.

## How does this Help my Career?
  * Deploying your web applications to a publicly accessible server is the first step in getting users.
  * Properly securing your application ensures your application remains stable and that your user’s data is safe
  
## Link to Project: P3 - Book Catalog
  * Public IP Address: http://35.165.104.19/
  * Accessible SSH port: 2200

## Tasks
  * Launch your Virtual Machine with your Udacity account
  * Follow the instructions provided to SSH into your server
  * Create a new user named grader
  * Give the grader the permission to sudo
  * Update all currently installed packages
  * Change the SSH port from 22 to 2200
  * Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123)
  * Configure the local timezone to UTC
  * Install and configure Apache to serve a Python mod_wsgi application
  * Install and configure PostgreSQL:
    * Do not allow remote connections
    * Create a new user named catalog that has limited permissions to your catalog application database
  * Install git, clone and setup your Catalog App project (from your GitHub repository from earlier
  in the Nanodegree program) so that it functions correctly when visiting your server’s IP address in a browser. Remember to set this up appropriately so that your .git directory is not publicly accessible via a browser!

  
  # Steps to Configure Linux server
  #### 1. Setup account on Amazon Lightsail and create a new instance.
  1. Download keys from the server.
  2. Move keys into .ssh directory.
  3. Change the key permission so that only owner can read and write.``` chmod 600 udacity_key.rsa ```
  4.  ssh into the instance using:```ssh -i ~/.ssh/udacity_key.rsa ubuntu@35.165.104.19 ```
    
    
  #### 2. Create a new user: grader
  1. ``` sudo adduser grader``` 
  2. ``` vim /etc/sudoers``` 
  3. ``` touch /etc/sudoers.d/grader``` 
  4. ``` vim /etc/sudoers.d/grader, type in grader ALL=(ALL:ALL) ALL, save and quit``` 
  5. To prevent host error, add the host to the hosts file:
  ```
  $ sudo nano /etc/hosts
  $ 127.0.1.1 ip-XX-XX-XX-XX
  ```
  #### 3. Configure ssh login from local machine
  1. Generate keys on local machine using ```ssh-keygen``` command.
  2. Save the public key generated on server.
    ```
    $ su - grader
    $ mkdir .ssh
    $ touch .ssh/authorized_keys
    $ vim .ssh/authorized_keys
    ```
    Copy the public key generated on local machine:
    ``` cat udacity_key.rsa```
    On virtual machine, store the key inside:
    ```
    $ chmod 700 .ssh
    $ chmod 644 .ssh/authorized_keys
    ```
  3. Restart ssh using ```sudo service restart```
  4. SSH into server from local machine using:
  ```ssh -i [privateKeyFilename] grader@35.165.104.19```
  
  #### 4. Update all Packages
  ```
  sudo apt-get update
  sudo apt-get upgrade
  ```
  #### 5. Enforce key based authentication
  * Run: ``` sudo nano /etc/ssh/sshd_config```
  * Find the PasswordAuthentication line and edit it to no.
  * Save the file.
  * Run: ```sudo service ssh restart``` to restart the service.
  
  #### 6. Change SSH port from 22 to 2200
  * Find the Port line in the same file: ```/etc/ssh/sshd_config``` and edit it to 2200
  * Save the file.
  * Run ```$ sudo service ssh restart``` to restart the service.
  
  #### 7. Configure Time Zone
  * Configure the time zone ```sudo dpkg-reconfigure tzdata```
  * Follow direction to set local time.
    
  #### 8. Configure the Firewall : UFW
  ```
  sudo ufw allow 2200/tcp
  sudo ufw allow 80/tcp
  sudo ufw allow 123/udp
  sudo ufw enable 
  ```

   #### 9. Configure cron scripts to automatically manage package updates
  1. Install unattended-upgrades if not already installed using command:
   ```$ sudo apt-get install unattended-upgrades```
  2. Enable it using command:
   ``` $ sudo dpkg-reconfigure --priority=low unattended-upgrades```

   #### 10. Install and configure Apache to serve a Python mod_wsgi application
  1. Install Apache ```sudo apt-get install apache2```
  2. Install mod_wsgi: ```sudo apt-get install python-setuptools libapache2-mod-wsgi```
  3. Restart Apache: ```sudo service apache2 restart```

   #### 11. Install and configure PostgreSQL
  1. Install PostgreSQL ```sudo apt-get install postgresql```
  2. Check if no remote connections are allowed ```sudo vim /etc/postgresql/9.3/main/pg_hba.conf```
  3. Login as user "postgres" ```sudo su - postgres```
  4. Get into postgreSQL shell ```psql```
  5. Create a new database named catalog and create a new user named catalog in postgreSQL shell
    ```
    postgres=# CREATE DATABASE catalog;
    postgres=# CREATE USER catalog;
    ```
  6. Set a password for user catalog
    ```postgres=# ALTER ROLE catalog WITH PASSWORD 'password';```
  7. Give user "catalog" permission to "catalog" application database
     ```postgres=# GRANT ALL PRIVILEGES ON DATABASE catalog TO catalog;```
  8. Quit postgreSQL ```postgres=# \q```
  9. Exit from user "postgres" : ```exit```

  #### 12. Install git and configure project on server.

  1. Install Git: ``` sudo apt-get install git```
  2. move to the /var/www directory ```cd /var/www```
  3. Create the application directory: ``` sudo mkdir FlaskApp ```
  4. Move into FLaskApp ```cd FlaskApp```
  5. Clone the Book Catalog App:``` git clone https://github.com/ssachde8/Item-Catalog.git```
  6. Rename the projects name:  ```sudo mv ./Item-Catalog ./FlaskApp```
  7. Move to the inner FlaskApp directory: ``` cd FlaskApp```
  8. Rename website.py to __init__.py: ``` sudo mv website.py __init__.py```
  9. Edit database_setup.py and application.py. 
  ```
  Change engine = create_engine('sqlite:///bookCatalog.db') 
  to 
  engine = create_engine('postgresql://catalog:password@localhost/catalog')
  ```
  10. Install pip:``` sudo apt-get install python-pip```
  11. Install Flask and other dependencies. 
  ```
  $ sudo pip install Flask
  $ sudo pip install httplib2 oauth2client sqlalchemy psycopg2 sqlalchemy_utils
  $ sudo pip install requests
  ```
  12. Create database schema: ``` sudo python database_setup.py```
  13. Add books: ``` sudo python add_books.py ```
  13. Configure and Enable a New Virtual Host

  #### 13. Create FlaskApp.conf to edit: sudo nano /etc/apache2/sites-available/FlaskApp.conf
  * Add the following lines of code to the file to configure the virtual host.
    ```
    <VirtualHost *:80>
      ServerName 35.165.104.19
      ServerAdmin satvik.sachdevagmail.com
      WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
      <Directory /var/www/FlaskApp/FlaskApp/>
        Order allow,deny
        Allow from all
      </Directory>
      Alias /static /var/www/FlaskApp/FlaskApp/static
      <Directory /var/www/FlaskApp/FlaskApp/static/>
        Order allow,deny
        Allow from all
      </Directory>
      ErrorLog ${APACHE_LOG_DIR}/error.log
      LogLevel warn
      CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
    ```
  * Enable the virtual host with the following command: ``` sudo a2ensite FlaskApp ``` 

 #### 14.  Create the .wsgi File
  * Create the .wsgi File under /var/www/FlaskApp:
      ```
      cd /var/www/FlaskApp
      sudo nano flaskapp.wsgi 
      ```

  * Add the following lines of code to the flaskapp.wsgi file:
      ```
      #!/usr/bin/python
      import sys
      import logging
      logging.basicConfig(stream=sys.stderr)
      sys.path.insert(0,"/var/www/FlaskApp/")

      from FlaskApp import app as application
      application.secret_key = 'Add your secret key'
      ```
  
  #### 15. Restart Apache
  ```sudo service apache2 restart```

  #### 16. References:
  1. https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
  2. https://github.com/stueken/FSND-P5_Linux-Server-Configuration










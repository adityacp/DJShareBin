DJShareBin
==========

Introduction
^^^^^^^^^^^^

A Django project to create and share text data. An inspiration from pastebin :)


Requirements
^^^^^^^^^^^^

- Python 3.6
- mysqlclient 1.4.6

Installation
^^^^^^^^^^^^

- Installing system requirements
      
      
      **Debian/Ubuntu**
          
      ::
       
          $ sudo apt-get install python3-dev default-libmysqlclient-dev
      
      
      **Centos/RedHat**
          
      ::
          
          $ sudo yum install python3-devel mysql-devel
  
  
-  Clone the repository

      ::

          $ git clone https://github.com/adityacp/DJShareBin.git

-  Go to the project directory

      ::

          $ cd DJShareBin


- Installing project packages

      ::

          $ pip install -r requirements.txt


- Create superuser

      ::

          $ python manage.py createsuperuser


- Run server Locally
      
      ::

          $ python manage.py runserver

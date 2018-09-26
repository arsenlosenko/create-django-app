create-django-app
=================

Even though I rarely create new django apps from scratch, I still don't like initial procedure of creating it, too much steps that can be automated. So I created this script to make the process easier.

What this script does:
-----------------------

- Creates Django project 
- Creates corresponding apps
- Creates initial virtualenv (venv)
- Installs provided dependencies   
- Creates initial requirements.txt
- Initializes git repository
- Runs initial migration (using sqlitedb)
- Creates superuser
- Shows created application in browser  

Download and run the script:
----------------------------
Python version:
---------------
Download it from PyPi:

.. code-block:: bash

    pip3 install create-django-app


Bash version:
--------------
You can download it via wget/curl/whatever you prefer:

.. code-block:: bash

    curl -O https://raw.githubusercontent.com/arsenlosenko/create-django-app/master/create-django-app.sh

After that give it executable permission:

.. code-block:: bash

    chmod +x create-django-app.sh

And run it:

.. code-block:: bash

    ./create-django-app.sh -d foo_project -a 'foo_app bar_app' -d 'requests'

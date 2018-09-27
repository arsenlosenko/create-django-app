create-django-app
=================

Even though I rarely create new django apps from scratch, I still don't like initial procedure of creating it, too much steps that can be automated. That's the purpose of this tool.

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

    pip3 install create-django-app --user

Usage:

.. code-block:: bash

    # show help
    create-django-app --help

    # create django project
    create-django-app -p test_project -a 'test_app1 test_app2' -d requests

    # create project without admin user with --noadmin flag
    create-django-app -p test_project -a 'test_app1 test_app2' -d requests --noadmin

    # don't run server in the end with --nodemo flag
    create-django-app -p test_project -a 'test_app1 test_app2' -d requests --nodemo



Bash version:
--------------
DEPRECATED: this script does not recieve same updates as the python package, buy still gets the job done.
You can download it via wget/curl/whatever you prefer:

.. code-block:: bash

    curl -O https://raw.githubusercontent.com/arsenlosenko/create-django-app/master/create-django-app.sh

After that give it executable permission:

.. code-block:: bash

    chmod +x create-django-app.sh

And run it:

.. code-block:: bash

    ./create-django-app.sh -d foo_project -a 'foo_app bar_app' -d 'requests'

Show help:

.. code-block:: bash

    ./create-django-app.sh

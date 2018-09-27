#!/bin/bash 

NORMAL="\e[0m"
BOLD="\e[1m"
GREEN="\e[32m"
RED="\e[31m"
VENV="venv"

while getopts p:a:d: option
do
    case "${option}"
        in
        p) PROJECT_NAME=${OPTARG};;
        a) APP_NAME=${OPTARG};;
        d) DEPS=${OPTARG};;
    esac
done

create_django_project(){
    django-admin startproject $PROJECT_NAME;
    echo -e "Project created in $BOLD$(pwd)/$PROJECT_NAME $NORMAL";
}

create_django_app(){
    IFS=' ' read -ra APP_NAMES <<< $APP_NAME;
    for app in "${APP_NAMES[@]}"; do
        django-admin startapp $app
        echo -e "Application $BOLD$app$NORMAL created in $BOLD$(pwd)/$app $NORMAL"
    done
}

init_venv(){
    echo -e "$BOLD""Initializing virtualenv$NORMAL"
    python3 -m venv $VENV
    source $VENV/bin/activate
}

install_py_deps(){
    echo -e "$BOLD""Installing provided dependencies""$NORMAL";
    pip install django
    pip install $DEPS;
}

create_requirements(){
    pip freeze >> requirements.txt
    echo -e "Requirements file created, stored in$BOLD $(pwd)/requirements.txt$NORMAL"
}

git_init(){
    git init
}

initial_migration(){
    echo -e "$BOLD""Initial migration started $NORMAL"
    python manage.py migrate
}

create_super_user(){
    echo -e "$BOLD""Creating superuser account $NORMAL"
    python manage.py createsuperuser
}

run_and_demo(){
    echo "Starting server on port 8000.."
    nohup python manage.py runserver </dev/null > django-app.log 2>&1 &
    xdg-open http://localhost:8000 >> /dev/null 2>&1
}

show_help(){
    echo -e "
    Usage: ./create-django-app.sh -p PROJECT_NAME -a APP_NAME(s) -d DEPENDENCIES
    -p - name of the project
    -a - name of app, or apps, in quotes
    -d - dependencies, also in quotes

    Example:
    ./create-django-app.sh -d foo_project -a 'foo_app bar_app' -d 'requests'
    "
}


if [[ $PROJECT_NAME && $APP_NAME && $DEPS ]]
then
    init_venv
    install_py_deps
    create_django_project
    cd $PROJECT_NAME
    create_django_app
    create_requirements
    git_init
    initial_migration
    create_super_user
    run_and_demo
else
    echo -e "$RED Either project name or app name is not specified, please try again $NORMAL"
    show_help
fi

#!/bin/bash

NORMAL="\e[0m"
BOLD="\e[1m"
GREEN="\e[32m"
RED="\e[31m"

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

install_py_deps(){
    echo -e "Installing provided dependencies";
    pipenv install django
    pipenv install $DEPS;
}

create_django_app(){
    IFS=' ' read -ra APP_NAMES <<< $APP_NAME;
    for app in "${APP_NAMES[@]}"; do
        django-admin startapp $app
        echo -e "Application created in $BOLD$(pwd)/$app $NORMAL"
    done
}

git_init(){
    git init
}

initial_migration(){
    echo -e "$BOLD Initial migration started $NORMAL"
    pipenv run python manage.py migrate
}

create_super_user(){
    echo -e "$BOLD Creating superuser account $NORMAL"
    pipenv run python manage.py createsuperuser
}

run_and_demo(){
    echo "Starting server on port 8000.."
    nohup pipenv run python manage.py runserver </dev/null > django-app.log 2>&1 &
    xdg-open http://localhost:8000 >> /dev/null 2>&1
}

show_help(){
    echo -e "
    Usage: ./create.sh -p PROJECT_NAME -a APP_NAME(s) -d DEPENDENCIES
    -p - name of the project
    -a - name of app, or apps, in quotes
    -d - dependencies, also in quotes

    Example:
    ./create.sh -d foo_project -a 'foo_app bar_app' -d 'requests'
    "
}


if [[ $PROJECT_NAME && $APP_NAME && $DEPS ]]
then
    create_django_project
    cd $PROJECT_NAME
    create_django_app
    install_py_deps
    git_init
    initial_migration
    create_super_user
    run_and_demo
else
    echo -e "$RED Either project name or app name is not specified, please try again $NORMAL"
    show_help
fi

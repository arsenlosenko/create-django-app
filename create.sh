#!/bin/bash

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
    echo "Project created in $(pwd)/$PROJECT_NAME";
}

install_py_deps(){
    echo "Installing provided deps";
    pipenv install django
    pipenv install $DEPS;
}

create_django_app(){
    IFS=' ' read -ra APP_NAMES <<< $APP_NAME;
    for app in "${APP_NAMES[@]}"; do
        django-admin startapp $app
        echo "Application created in $(pwd)/$app"
    done
}

git_init(){
    git init
}

initial_migration(){
    echo "Initial migration started"
    pipenv run python manage.py migrate
}

create_super_user(){
    echo "Creating superuser account"
    pipenv run python manage.py createsuperuser
}

run_and_demo(){
    echo "Starting server.."
    nohup pipenv run python manage.py runserver >> django-app.log 2>&1 &
    google-chrome localhost
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
    echo "Either project name or app name are not specified, please try again"
fi

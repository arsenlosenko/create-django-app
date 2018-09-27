#!/usr/bin/env python3 
import os
import webbrowser
from os.path import abspath
from subprocess import run
from venv import EnvBuilder
from argparse import ArgumentParser

bold = lambda word: "\033[1;37;40m{}\033[0;37;40m".format(word)
green = lambda word: "\033[1;31;40m{}\033[0;37;40m".format(word)
red = lambda word: "\033[1;32;40m{}\033[0;37;40m".format(word)

def parse_args() -> None:
    parser = ArgumentParser(description='Create Django App: CLI tool for automatic django app creation')
    parser.add_argument('-p', '--project', help='name of the project', required=True)
    parser.add_argument('-a', '--apps', help='name of apps', required=True)
    parser.add_argument('-d', '--deps', help='dependency names', required=True)
    return parser.parse_args()

def run_django_admin(cmd: str, *args):
    return run(['django-admin', cmd, *args])

def pip_install(venv_folder: str, package: str) -> None:
    return run(['{}/venv/bin/pip'.format(venv_folder), 'install', package]) 

def run_manage_py(cmd, *args):
    python = os.getcwd() + '/venv/bin/python'
    run([python, 'manage.py', cmd, *args])

def create_django_project(project_name: str) -> None:
    print('Initializing Django project {}'.format(bold(project_name)))
    run_django_admin('startproject', project_name)

def create_django_apps(apps: str) -> None:
    for app in apps.split(' '):
        run_django_admin('startapp', app)
        print('Application {} created in {}'.format(bold(app), bold(os.path.abspath(app))))

def init_venv() -> None:
    venv_dir = os.getcwd() + '/venv'
    venv = EnvBuilder(with_pip=True)
    venv.create(venv_dir)
    
def install_deps(dependencies: str) -> None:
    print(bold('Installing dependencies'))
    project_dir = os.getcwd()
    pip_install(project_dir, 'django')
    if dependencies is not None:
        pip_install(project_dir, dependencies)

def create_requirements():
    pip = os.getcwd() + '/venv/bin/pip'
    run([pip, 'freeze'], stdout=open('requirements.txt', 'w'))
    print('Requirements file created, situated in {}'.format(bold(os.getcwd() + '/requirements.txt')))

def git_init():
    run(['git', 'init'])

def initial_migration():
    print(bold('Running initial migration'))
    run_manage_py('migrate')

def create_super_user():
    print(bold('Creating superuser'))
    run_manage_py('createsuperuser')

def run_and_demo():
    print(bold('Starting server on port 8000...'))
    python = os.getcwd() + '/venv/bin/python'
    run(['nohup', python, 'manage.py', 'runserver'], stdout=open('/dev/null', 'w'),
                                        stderr=open('django.log', 'a'), preexec_fn=os.setpgrp)
    run(['xdg-open', 'http://localhost:8000'], stdout=open('/dev/null', 'w'),
                                        stderr=open('/dev/null', 'w'), preexec_fn=os.setpgrp)

def create_project() -> None:
    args = parse_args()
    create_django_project(args.project)
    os.chdir(abspath(args.project))
    create_django_apps(args.apps)
    init_venv()
    install_deps(args.deps)
    create_requirements()
    git_init()
    initial_migration()
    create_super_user()
    run_and_demo()

if __name__ == '__main__':
    create_project()


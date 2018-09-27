#!/usr/bin/env python3 
import os
import webbrowser
from os.path import abspath
from subprocess import run
from virtualenv import create_environment
from argparse import ArgumentParser

bold = lambda word: "\033[1;37;40m{}\033[0;37;40m".format(word)
green = lambda word: "\033[1;32;40m{}\033[0;37;40m".format(word)
red = lambda word: "\033[1;31;40m{}\033[0;37;40m".format(word)


def parse_args() -> None:
    parser = ArgumentParser(description='Create Django App: CLI tool for automatic django app creation')
    parser.add_argument('-p', '--project', help='name of the project', required=True)
    parser.add_argument('-a', '--apps', help='name of apps', required=True)
    parser.add_argument('-d', '--deps', help='dependency names')
    parser.add_argument('--noadmin', help='skip superuser creation', action='store_true')
    parser.add_argument('--nodemo', help="don't run server in the end", action='store_true')
    return parser.parse_args()


def make_project_dir(dir_name: str):
    print(bold("Project creation begun..."))
    os.mkdir(abspath(dir_name))


def run_django_admin(project_dir: str, cmd: str, *args):
    return run(['{}/venv/bin/django-admin'.format(project_dir), cmd, *args])


def pip_install(venv_folder: str, package: str) -> None:
    return run(['{}/venv/bin/pip'.format(venv_folder), 'install', package]) 


def run_manage_py(cmd, *args):
    python = os.getcwd() + '/venv/bin/python'
    run([python, 'manage.py', cmd, *args])


def create_django_project(project_name: str) -> None:
    print('Initializing Django project {}'.format(bold(project_name)))
    run_django_admin(os.getcwd(), 'startproject', project_name, '.')


def create_django_apps(apps: str) -> None:
    for app in apps.split(' '):
        run_django_admin(os.getcwd(), 'startapp', app)
        print('Application {} created in {}'.format(bold(app), bold(os.path.abspath(app))))


def init_venv() -> None:
    venv_dir = os.getcwd() + '/venv'
    create_environment(venv_dir)

    
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
    webbrowser.open('http://localhost:8000', new=2)


def print_msg(msg, cmd):
    print("{}\n\n  {}\n".format(bold(msg), green(cmd)))


def create_project() -> None:
    args = parse_args()
    make_project_dir(args.project)
    os.chdir(abspath(args.project))
    init_venv()
    install_deps(args.deps)
    create_django_project(args.project)
    create_django_apps(args.apps)
    create_requirements()
    git_init()
    initial_migration()
    if args.noadmin:
        print_msg(
            "Project initialized wihtout superuser,"
            "to create him run this command inside of project's virtualenv:",
            "python manage.py createsuperuser")
    else:
        create_super_user()

    if args.nodemo:
        print_msg(
            "You are all set, project is ready for hacking!\n"
            "To start development server you can run this command:",
            "python manage.py runserver")
    else:
        run_and_demo()


if __name__ == '__main__':
    create_project()


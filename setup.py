from setuptools import setup

version = '0.0.8'

setup(
    name='create-django-app',
    version=version,
    packages=['create_django_app'],
    url='https://github.com/arsenlosenko/create-django-app',
    license='MIT',
    author='Arsen Losenko',
    author_email='arsenlosenko@gmail.com',
    description='CLI tool to automate initialization of Django project',
    long_description=open('readme.rst').read(),
    keywords='python django cli CLI',
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5'
    ],
    entry_points = {
        'console_scripts': ['create-django-app=create_django_app.cli:create_project']
    }
)

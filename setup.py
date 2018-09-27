from setuptools import setup

version = '0.0.9.1'

setup(
    name='create-django-app',
    version=version,
    packages=['create_django_app'],
    url='https://github.com/arsenlosenko/create-django-app',
    license='MIT',
    author='Arsen Losenko',
    author_email='arsenlosenko@gmail.com',
    description='CLI tool to quickstart Django app',
    long_description=open('README.rst').read(),
    keywords='python django cli CLI',
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5'
    ],
    install_requires=[
        'virtualenv'
    ],
    entry_points = {
        'console_scripts': ['create-django-app=create_django_app.cli:create_project']
    }
)

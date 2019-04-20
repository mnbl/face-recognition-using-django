## Python Facial Recognition System
Facial Recognition System using Python

> This version is tested to work on Ubuntu 18.04.2 with Python 3.6.7 and Django version 1.11.8


### Requirement
- Python 3.*
- PIP3
- OpenCV
- Django
- Pillow

### Installation of Project

- Make git pull of the whole project
```sh
$ git clone https://github.com/mnbl/website.git/
```
- Install pip3
```sh
$ sudo apt-get install python3-pip
```
- To run face recognition training and dataset folders are required. Create emplty folders using: 
```sh
$ cd home
$ mkdir trainer dataset
```

## Run Face Recognition
```sh
$ python3 manage.py migrate
$ python3 manage.py runserver
```
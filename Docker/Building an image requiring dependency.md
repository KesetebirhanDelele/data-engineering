# Table of Content

<!-- TOC -->

- [Table of Content](#table-of-content)
- [Building an image needing dependency](#building-an-image-needing-dependency)
    - [Create a Python file containing faker library in src](#create-a-python-file-containing-faker-library-in-src)
    - [Create a Dockerfile](#create-a-dockerfile)
        - [Base image](#base-image)
        - [Copy requirements.text into temp file to show what library to import](#copy-requirementstext-into-temp-file-to-show-what-library-to-import)
        - [Update Python base image and install requirements from the text file](#update-python-base-image-and-install-requirements-from-the-text-file)
        - [Copies python code file from src folder by going back a level and going in src folder](#copies-python-code-file-from-src-folder-by-going-back-a-level-and-going-in-src-folder)
        - [ENTRYPOINT informs docker what is going to happen when the container is up and running: run python code using the hello-faked-person file](#entrypoint-informs-docker-what-is-going-to-happen-when-the-container-is-up-and-running-run-python-code-using-the-hello-faked-person-file)
    - [Checking if there is an active container which is running](#checking-if-there-is-an-active-container-which-is-running)
    - [Moving to the folder where the python code is located](#moving-to-the-folder-where-the-python-code-is-located)
    - [Biulding the Docker image](#biulding-the-docker-image)
    - [Run the python code image just created without argument](#run-the-python-code-image-just-created-without-argument)
    - [Run the python code image just created with an argument](#run-the-python-code-image-just-created-with-an-argument)

<!-- /TOC -->

# Building an image needing dependency

## 1. Create a Python file containing faker library in src
> This library will generate a fake name and state every time it is run. Note that faker library is not found in Python and needs to be imported 
## 2. Create a Dockerfile
> Make sure a dockerfile containing the following content is placed in the working folder (Docker-Fundamentals):

### Base image
> FROM python:3.9

### Copy requirements.text into temp file to show what library to import
> COPY requirements.txt /tmp/

### Update Python base image and install requirements from the text file
> RUN pip install --no-cache-dir --upgrade pip && \
>     pip install --requirement /tmp/requirements.txt

### Copies python code file from src folder by going back a level and going in src folder
> copy ./src/hello-faked-person.py /src/hello-faked-person.py

### ENTRYPOINT informs docker what is going to happen when the container is up and running: run python code using the hello-faked-person file
> ENTRYPOINT ["python","./src/hello-faked-person.py"]

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows


## 3. Checking if there is an active container which is running
PS C:\Users\keset>
>__docker ps__


CONTAINER ID   IMAGE                           COMMAND        CREATED       STATUS       PORTS                                                                    NAMES
a5ecfc58cc86   portainer/portainer-ce:2.11.1   "/portainer"   2 hours ago   Up 2 hours   0.0.0.0:8000->8000/tcp, 0.0.0.0:9000->9000/tcp, 0.0.0.0:9443->9443/tcp   portainer

## 4. Moving to the folder where the python code is located 
__PS C:\Users\keset> cd OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals__

## 5. Biulding the Docker image
PS C:\Users\keset\OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals> 
> __docker build -f dockerfile-user -t hello-user .__


[+] Building 11.0s (10/10) FINISHED                                                                      docker:default
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load build definition from dockerfile-user                                                          0.0s
 => => transferring dockerfile: 314B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                      1.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                      0.0s
 => CACHED [1/4] FROM docker.io/library/python:3.9@sha256:98f018a1afd67f2e17a4abd5bfe09b998734ba7c1ee54780e7ed216  0.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 242B                                                                                  0.0s
 => [2/4] COPY requirements.txt /tmp/                                                                              0.0s
 => [3/4] RUN pip install --no-cache-dir --upgrade pip &&     pip install --requirement /tmp/requirements.txt      9.3s
 => [4/4] COPY ./src/hello-faked-person.py /src/hello-faked-person.py                                              0.0s
 => exporting to image                                                                                             0.3s
 => => exporting layers                                                                                            0.3s
 => => writing image sha256:2d144017996c8899205a3a2fbf72413ad7596f0d1a5c97b1882865d98afa1c49                       0.0s
 => => naming to docker.io/library/hello-user                                                                      0.0s

What's Next?
  View summary of image vulnerabilities and recommendations → docker scout quickview
PS C:\Users\keset\OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals> docker run hello-faked-person

## 6. Run the python code image just created without argument
PS C:\Users\keset\OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals> 
> docker run hello-user


Hello Phyllis Phillips from Arkansas

## 7. Run the python code image just created with an argument
PS C:\Users\keset\OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals> 
> docker run hello-user


Hello Deanna Matthews from Maine

Start a build
PS C:\Users\keset\OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals> docker build -f dockerfile-user -t hello-user .


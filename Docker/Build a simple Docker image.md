## Table of Content

<!-- TOC -->

    - [Table of Content](#table-of-content)
- [Building a Simple Docker Image](#building-a-simple-docker-image)
        - [Create a Python file containing application code and place it in src resource folder](#create-a-python-file-containing-application-code-and-place-it-in-src-resource-folder)
        - [Create a Dockerfile](#create-a-dockerfile)
            - [Base image](#base-image)
            - [Copies python code file from src folder by going back a level and going in src folder](#copies-python-code-file-from-src-folder-by-going-back-a-level-and-going-in-src-folder)
            - [ENTRYPOINT informs docker what is going to happen when the container is up and running: run python code using the hello-world file](#entrypoint-informs-docker-what-is-going-to-happen-when-the-container-is-up-and-running-run-python-code-using-the-hello-world-file)
        - [CHecking if there is an active container which is running](#checking-if-there-is-an-active-container-which-is-running)
        - [Moving to the folder where the python code is located](#moving-to-the-folder-where-the-python-code-is-located)
        - [Biulding the Docker image](#biulding-the-docker-image)
        - [Run the python code image just created without argument](#run-the-python-code-image-just-created-without-argument)
        - [Run the python code image just created with an argument](#run-the-python-code-image-just-created-with-an-argument)

<!-- /TOC -->

# Building a Simple Docker Image

### 1. Create a Python file containing application code and place it in src (resource folder)

### 2. Create a Dockerfile
> Make sure a dockerfile containing with the following content is placed in the working folder (Docker-Fundamentals):

#### Base image
> FROM python:3.9

#### Copies python code file from src folder by going back a level and going in src folder
> copy ./src/hello-world.py /src/hello-world.py

#### ENTRYPOINT informs docker what is going to happen when the container is up and running: run python code using the hello-world file
> ENTRYPOINT ["python","./src/hello-world.py"]

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows


### 3. CHecking if there is an active container which is running
PS C:\Users\keset>
>__docker ps__


CONTAINER ID   IMAGE                           COMMAND        CREATED       STATUS       PORTS                                                                    NAMES
a5ecfc58cc86   portainer/portainer-ce:2.11.1   "/portainer"   2 hours ago   Up 2 hours   0.0.0.0:8000->8000/tcp, 0.0.0.0:9000->9000/tcp, 0.0.0.0:9443->9443/tcp   portainer

### 4. Moving to the folder where the python code is located 
__PS C:\Users\keset> cd OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals__

### 5. Biulding the Docker image
PS C:\Users\keset\OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals> 
> __docker build -t hello-world .__


[+] Building 428.8s (8/8) FINISHED                                                                       docker:default
 => [internal] load build definition from dockerfile                                                               0.1s
 => => transferring dockerfile: 149B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  0.1s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                      1.9s
 => [auth] library/python:pull token for registry-1.docker.io                                                      0.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 260B                                                                                  0.0s
 => [1/2] FROM docker.io/library/python:3.9@sha256:98f018a1afd67f2e17a4abd5bfe09b998734ba7c1ee54780e7ed216f8b80  426.1s
 => => resolve docker.io/library/python:3.9@sha256:98f018a1afd67f2e17a4abd5bfe09b998734ba7c1ee54780e7ed216f8b8095  0.0s
 => => sha256:98f018a1afd67f2e17a4abd5bfe09b998734ba7c1ee54780e7ed216f8b8095c3 1.86kB / 1.86kB                     0.0s
 => => sha256:ec2b820b8e87758dde67c29b25d4cbf88377601a4355cc5d556a9beebc80da00 24.03MB / 24.03MB                  57.1s
 => => sha256:284f2345db055020282f6e80a646f1111fb2d5dfc6f7ee871f89bc50919a51bf 64.11MB / 64.11MB                 253.5s
 => => sha256:8d6fcdcf73c918683b9933499461b75bd20b5beb08ee96758bed081feb5a2d2d 2.01kB / 2.01kB                     0.0s
 => => sha256:618db5c0a924c7db9c3779147b637b806bcf6b23d11adde5de1f70aa353c6807 7.51kB / 7.51kB                     0.0s
 => => sha256:bba7bb10d5baebcaad1d68ab3cbfd37390c646b2a688529b1d118a47991116f4 49.55MB / 49.55MB                 198.0s
 => => sha256:fea23129f080a6e28ebff8124f9dc585b412b1a358bba566802e5441d2667639 211.00MB / 211.00MB               417.2s
 => => sha256:7c62c924b8a6474ab5462996f6663e07a515fab7f3fcdd605cae690a64aa01c7 6.39MB / 6.39MB                   235.8s
 => => extracting sha256:bba7bb10d5baebcaad1d68ab3cbfd37390c646b2a688529b1d118a47991116f4                          2.3s
 => => extracting sha256:ec2b820b8e87758dde67c29b25d4cbf88377601a4355cc5d556a9beebc80da00                          0.6s
 => => sha256:b2210932934efec1c984a1fad98942bb3f4d73106610e8db5185fc5037f18409 15.82MB / 15.82MB                 273.0s
 => => extracting sha256:284f2345db055020282f6e80a646f1111fb2d5dfc6f7ee871f89bc50919a51bf                          2.7s
 => => sha256:ee9c01829d92f672ccecca7eaf47c437ad8ed4ca4f62101f7d6d2081bf54231e 242B / 242B                       254.1s
 => => sha256:d6285f41f1b6dc5d19e09aff87fbf4700c8df6453fb2608328f9aa648b08972c 2.85MB / 2.85MB                   259.5s
 => => extracting sha256:fea23129f080a6e28ebff8124f9dc585b412b1a358bba566802e5441d2667639                          7.0s
 => => extracting sha256:7c62c924b8a6474ab5462996f6663e07a515fab7f3fcdd605cae690a64aa01c7                          0.3s
 => => extracting sha256:b2210932934efec1c984a1fad98942bb3f4d73106610e8db5185fc5037f18409                          0.6s
 => => extracting sha256:ee9c01829d92f672ccecca7eaf47c437ad8ed4ca4f62101f7d6d2081bf54231e                          0.0s
 => => extracting sha256:d6285f41f1b6dc5d19e09aff87fbf4700c8df6453fb2608328f9aa648b08972c                          0.2s
 => [2/2] COPY ./src/hello-world.py /src/hello-world.py                                                            0.6s
 => exporting to image                                                                                             0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:6418dd7029862dd4e5187fd8a969be314b99bc4700aeb26f75bbf7747610e8e6                       0.0s
 => => naming to docker.io/library/hello-world                                                                     0.0s

What's Next?
  View summary of image vulnerabilities and recommendations → docker scout quickview

### 6. Run the python code image just created without argument
PS C:\Users\keset\OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals> 
> docker run hello-world


hello-world

### 7. Run the python code image just created with an argument
PS C:\Users\keset\OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals> 
> docker run hello-world kesete


hello-world kesete
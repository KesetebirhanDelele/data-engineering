# Table of Content

<!-- TOC -->

- [Table of Content](#table-of-content)
    - [build image for repo](#build-image-for-repo)
    - [push image into repo](#push-image-into-repo)

<!-- /TOC -->

## build image for repo
> __docker build -f dockerfile-user -t kesetebirhan/hello-user:latest .__


[+] Building 0.7s (10/10) FINISHED                                                                                                           docker:default
 => [internal] load build definition from dockerfile-user                                                                         0.0s
 => => transferring dockerfile: 314B                                                                                    0.0s
 => [internal] load .dockerignore                                                                            0.0s
 => => transferring context: 2B                                                                                      0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                                                       0.7s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                      0.0s
 => [internal] load build context                                                                                 0.0s
 => => transferring context: 104B                                                                                    0.0s
 => [1/4] FROM docker.io/library/python:3.9@sha256:98f018a1afd67f2e17a4abd5bfe09b998734ba7c1ee54780e7ed216f8b8095c3               0.0s
 => CACHED [2/4] COPY requirements.txt /tmp/                                                                                    0.0s
 => CACHED [3/4] RUN pip install --no-cache-dir --upgrade pip &&     pip install --requirement /tmp/requirements.txt                                                     0.0s
 => CACHED [4/4] COPY ./src/hello-faked-person.py /src/hello-faked-person.py                                                                                      0.0s
 => exporting to image                                                                                   0.0s
 => => exporting layers                                                                                  0.0s
 => => writing image sha256:2d144017996c8899205a3a2fbf72413ad7596f0d1a5c97b1882865d98afa1c49                 0.0s
 => => naming to docker.io/kesetebirhan/hello-user:latest                                                                       0.0s

What's Next?
  View summary of image vulnerabilities and recommendations → docker scout quickview

## push image into repo
> __docker push kesetebirhan/hello-user:latest__

PS C:\Users\keset\OneDrive\Desktop\projects\data-engineering\Docker\Docker-Fundamentals> docker push kesetebirhan/hello-user:latest
The push refers to repository [docker.io/kesetebirhan/hello-user]
d73289dac510: Pushed
f037f6ca7a17: Pushed
e7b19189b011: Pushed
68361737f8ab: Mounted from library/python
d489e554906d: Mounted from library/python
c76ff3d38b1d: Mounted from library/python
037f26f86912: Mounted from library/python
e67fb4bad8f4: Mounted from library/python
964529c819bb: Mounted from library/python
2f98f42985b1: Mounted from library/python
332b199f36eb: Mounted from library/python
latest: digest: sha256:b1e6f09bc263f955390610daedc0d264074db51ca3101adb54d4c11c497fe5d7 size: 2633


<!-- TOC -->

- [The Ultimate Docker Cheat Sheet](#the-ultimate-docker-cheat-sheet)
    - [Basic Docker CLIs](#basic-docker-clis)
    - [Container Management CLIs](#container-management-clis)
    - [Inspecting The Container](#inspecting-the-container)
    - [Interacting with Container](#interacting-with-container)
    - [Image Management Commands](#image-management-commands)
    - [Image Transfer Commands](#image-transfer-commands)
    - [Builder Main Commands](#builder-main-commands)
- [see docker create for options](#see-docker-create-for-options)

<!-- /TOC -->

# The Ultimate Docker Cheat Sheet
![image.png](attachment:image.png)

## Basic Docker CLIs
Here’s the list of the basic Docker commands that works on both Docker Desktop as well as Docker Engine:
![image.png](attachment:image.png)

## Container Management CLIs
Here’s the list of the Docker commands that manages Docker images and containers flawlessly:
![image.png](attachment:image.png)

## Inspecting The Container
Here’s the list of the basic Docker commands that helps you inspect the containers seamlessly:
![image.png](attachment:image.png)

## Interacting with Container
Do you want to know how to access the containers? Check out these fundamental commands:
![image.png](attachment:image.png)

## Image Management Commands
Here’s the list of Docker commands that helps you manage the Docker Images:
![image.png](attachment:image.png)

## Image Transfer Commands
![image.png](attachment:image.png)

## Builder Main Commands
Want to know how to build Docker Image? Do check out the list of Image Build Commands:
![image.png](attachment:image.png)

Builder Main Commands

The Docker CLI
Manage images


docker build


docker build [options] .
  -t "app/container_name"    # name
Create an image from a Dockerfile.

docker run


docker run [options] IMAGE
  # see `docker create` for options
Run a command in an image.

Manage containers


docker create


docker create [options] IMAGE
  -a, --attach               # attach stdout/err
  -i, --interactive          # attach stdin (interactive)
  -t, --tty                  # pseudo-tty
      --name NAME            # name your image
  -p, --publish 5000:5000    # port map
      --expose 5432          # expose a port to linked containers
  -P, --publish-all          # publish all ports
      --link container:alias # linking
  -v, --volume `pwd`:/app    # mount (absolute paths needed)
  -e, --env NAME=hello       # env vars
Example


$ docker create --name app_redis_1 \
  --expose 6379 \
  redis:3.0.2
Create a container from an image.

docker exec


docker exec [options] CONTAINER COMMAND
  -d, --detach        # run in background
  -i, --interactive   # stdin
  -t, --tty           # interactive
Example
$ docker exec app_web_1 tail logs/development.log
$ docker exec -t -i app_web_1 rails c
Run commands in a container.

docker start
docker start [options] CONTAINER
  -a, --attach        # attach stdout/err
  -i, --interactive   # attach stdin

docker stop [options] CONTAINER
Start/stop a container.

docker ps
$ docker ps
$ docker ps -a
$ docker kill $ID
Manage containers using ps/kill.

Images
docker images
$ docker images
  REPOSITORY   TAG        ID
  ubuntu       12.10      b750fe78269d
  me/myapp     latest     7b2431a8d968
$ docker images -a   # also show intermediate
Manages images.

docker rmi
docker rmi b750fe78269d
Deletes images.
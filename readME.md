## 160122771054 DevOps Tools Assignment 2

### About

Developed a python script that generates words of length 4 to 7 for given set of letters. This project's complete development is tracked using Git, containerized using Docker and its image deployed as a Kubernetes pod.

### Tools

- Python 3.12.4
- Git 2.50.1
- Docker 28.4.0
- Minikube 1.37.0
- Kubectl 1.32.2

### Syntax Used

- git
    1.  checkout -b newBranch
    2.  push remote local
    3.  merge other current
    4.  add .
    5.  commit -m 'message'
    6.  clone \<url\>
    7. status
- docker
    1. images
    2. containers
    3. build -t imageName .
    4. run -it imageName
    5. tag imageName:latest username/repo:latest
    6. login
    7. push username/repo:lastest
- minikube
    1. start --driver=docker
    2. stop
- kubectl
    1. get pods
    2. build -f file.yml
    3. describe pod podName
    4. delete pod podName
    5. logs podName
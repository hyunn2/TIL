#!/bin/bash


# 1. minikube 실행
minikube start --driver=docker

eval $(minikube docker-env)
MINIKUBE_IP=$(minikube ip)

sed -i '' "s/MINIKUBE_IP/$MINIKUBE_IP/g" ./metallb.yaml
sed -i '' "s/MINIKUBE_IP/$MINIKUBE_IP/g" ./redis.yaml
sed -i '' "s/MINIKUBE_IP/$MINIKUBE_IP/g" ./backend.yaml
sed -i '' "s/MINIKUBE_IP/$MINIKUBE_IP/g" ./frontend.yaml

# minikube addons enable metallb
# kubectl apply -f metallb.yaml

# 2. docker build
docker build -f ./redis.Dockerfile -t redis .

docker build -f ./backend.Dockerfile -t back .

docker build -f ./frontend.Dockerfile -t front .

# 3. kubectl apply yaml
kubectl apply -f redis.yaml

kubectl apply -f backend.yaml

kubectl apply -f frontend.yaml

#!/bin/bash

MINIKUBE_IP=$(minikube ip)

sed -i '' "s/$MINIKUBE_IP/MINIKUBE_IP/g" ./metallb.yaml
sed -i '' "s/$MINIKUBE_IP/MINIKUBE_IP/g" ./redis.yaml
sed -i '' "s/$MINIKUBE_IP/MINIKUBE_IP/g" ./backend.yaml
sed -i '' "s/$MINIKUBE_IP/MINIKUBE_IP/g" ./frontend.yaml

sed -i '' "s/$MINIKUBE_IP/MINIKUBE_IP/g" ./backend/Redis/user_login.py
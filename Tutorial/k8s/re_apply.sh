#!/bin/bash

kubectl apply -f metallb.yaml

kubectl apply -f redis.yaml

kubectl apply -f backend.yaml

kubectl apply -f frontend.yaml
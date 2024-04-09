#!/bin/bash
read -p "dockerhub username " dockerhub_username

read -p "container name " container_name

image_name="$container_name"
docker build -t $image_name .
docker tag $image_name $dockerhub_username/$image_name
docker push $dockerhub_username/$image_name


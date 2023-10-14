# build_docker_image.sh

docker build -t $IMAGE_NAME:$TAG .
# Possibly automate the updating of image/build number in a file if needed here
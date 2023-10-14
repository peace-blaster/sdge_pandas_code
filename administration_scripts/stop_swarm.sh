# stop_swarm.sh

docker stack rm $STACK_NAME
docker swarm leave --force

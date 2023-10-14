# stop_swarm.sh

docker stack rm $STACK_NAME
# Optionally: docker swarm leave --force

# start_swarm.sh

docker swarm init
docker stack deploy -c docker-compose.yml $STACK_NAME

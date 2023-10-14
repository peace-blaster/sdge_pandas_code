#!/bin/bash


source administration_scripts/config.sh
while true; do
    CHOICE=$(whiptail --title "SDGE Example Dashboard Control Panel" --menu "Choose an option:" 16 78 10 \
        "build" "Build the Docker image" \
        "start_container" "Run a single Docker container" \
        "start_swarm" "Start the Docker Swarm" \
        "stop_swarm" "Stop the Docker Swarm" \
        "update_swarm" "Update the Docker Swarm" \
        "exit" "Exit Script" 3>&1 1>&2 2>&3)

    case $CHOICE in
        "build")
            ./administration_scripts/build_docker_image.sh
            ;;

        "start_container")
            ./administration_scripts/start_container.sh
            ;;

        "swarm_start")
            ./administration_scripts/swarm_start.sh
            ;;

        "swarm_stop")
            ./administration_scripts/swarm_stop.sh
            ;;

        "swarm_update")
            ./administration_scripts/swarm_update.sh
            ;;

        "exit")
            # Exit the script
            break
            ;;
    esac
done

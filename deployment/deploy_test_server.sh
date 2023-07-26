IMAGE_NAME="honkou/towns_herald"
TAG="dev"

docker pull "${IMAGE_NAME}:${TAG}"

container_ids=$(docker ps -q --filter "ancestor=${IMAGE_NAME}:${TAG}")

    if [ -n "$container_ids" ]; then
        # Stop the containers
        docker stop $container_ids

        # Delete the containers
        docker rm $container_ids
    fi

cd /home/honkou/Discord-docker

docker run -d --env-file .env --restart unless-stopped --name "dev_bot" "${IMAGE_NAME}:${TAG}"

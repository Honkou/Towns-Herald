IMAGE_NAME="honkou/towns_herald"
TAG="dev"

# Pull the dev image from repo
docker pull "${IMAGE_NAME}:${TAG}"

# Get the IMAGE ID of the <none> image (dangling due to the pull)
none_image_id=$(docker images -f "dangling=true" -q)

if [ -z "$none_image_id" ]; then
  echo "No images with <none> tag found."
else
  # List all containers and check if they are based on the <none> image
  containers=$(docker ps -aq)

  for container in $containers; do
    image_id=$(docker inspect --format "{{.Image}}" $container)
    if [ "$image_id" = "$none_image_id" ]; then
      echo "Stopping container $container..."
      docker stop $container
      echo "Removing container $container..."
      docker rm $container
    fi
  done

  # Remove the <none> image after there are no more containers based on it
  echo "Removing <none> image..."
  docker rmi $none_image_id
fi

# Get the CONTAINER IDs that would still be present and have the same name
container_ids=$(docker ps -q --filter name=dev_bot)

    if [ -n "$container_ids" ]; then
        # Stop the containers
        echo "Stopping named containers $container_ids..."
        docker stop $container_ids

        # Delete the containers
        echo "Removing named containers $container_ids..."
        docker rm $container_ids
    fi

cd /home/honkou/Discord-docker

docker run -d --env-file .env --restart unless-stopped --name "dev_bot" "${IMAGE_NAME}:${TAG}"

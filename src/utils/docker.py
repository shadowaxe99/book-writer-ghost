```python
import docker

class DockerManager:
    def __init__(self):
        self.client = docker.from_env()

    def build_image(self, dockerfile_path, tag):
        self.client.images.build(path=dockerfile_path, tag=tag)

    def run_container(self, image_name, detach=True, ports=None, volumes=None):
        self.client.containers.run(image_name, detach=detach, ports=ports, volumes=volumes)

    def stop_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.stop()

    def remove_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.remove()

    def list_containers(self):
        return self.client.containers.list()

    def list_images(self):
        return self.client.images.list()

docker_manager = DockerManager()
```
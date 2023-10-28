```python
import os
from docker import from_env as docker_from_env
from kubernetes import client, config

class DeploymentManager:
    def __init__(self):
        self.docker_client = docker_from_env()
        self.kubernetes_client = client.CoreV1Api()

    def build_docker_image(self, dockerfile_path, tag):
        self.docker_client.images.build(path=dockerfile_path, tag=tag)

    def push_docker_image(self, tag):
        image = self.docker_client.images.get(tag)
        repo, tag = tag.split(":")
        image.tag(repo, tag=tag)
        self.docker_client.images.push(repo, tag=tag)

    def deploy_to_kubernetes(self, deployment_config_path):
        config.load_kube_config()
        with open(deployment_config_path) as f:
            dep = yaml.safe_load(f)
            resp = self.kubernetes_client.create_namespaced_deployment(
                body=dep, namespace="default")
            print(f"Deployment created. status='{resp.status}'")

if __name__ == "__main__":
    manager = DeploymentManager()

    # Build Docker image
    dockerfile_path = os.path.join(os.getcwd(), "Dockerfile")
    image_tag = "autobiographyai:latest"
    manager.build_docker_image(dockerfile_path, image_tag)

    # Push Docker image to registry
    manager.push_docker_image(image_tag)

    # Deploy to Kubernetes
    deployment_config_path = os.path.join(os.getcwd(), "k8s_deployment.yaml")
    manager.deploy_to_kubernetes(deployment_config_path)
```
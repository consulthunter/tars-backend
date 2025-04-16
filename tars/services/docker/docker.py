import docker
from docker.types import Mount


class DockerRunner:
    def __init__(self, project):
        self.project = project

    def run_docker(self):
        try:
            client = docker.from_env()
            mount = Mount(target=self.project.docker, source=self.project.project_temp_dir, type="bind")
            client.containers.run(image=self.project.docker, command="/bin/bash run.sh", detach=True, mounts=[mount], auto_remove=True)
        except Exception as e:
            self.project.logger.log_error(f"Error running docker: {e}")
import asyncio

from tars.services.docker.docker import DockerRunner


class Analyze:
    def __init__(self, project):
        self.project = project

    async def run_analyze_async(self):
        self.project.logger.log_info(f"Analyzing project {self.project.project_id}")
        docker = DockerRunner(self.project)
        return await asyncio.to_thread(docker.run_docker())
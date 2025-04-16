
class Delete:

    def __init__(self, project):
        self.project = project

    async def run_delete_async(self):
        self.project.logger.log_info(f"Deleting for project {self.project.project_id}")

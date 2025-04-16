import asyncio

from tars.core.models.analysis_project import AnalysisProject
from tars.core.models.tars_project import TarsProject
from tars.services.project_operations.clone import Clone
from tars.services.project_operations.load import Load
from tars.services.project_operations.analyze import Analyze
from tars.services.project_operations.delete import Delete

class TarsRunner:
    def __init__(self, configuration, logger):
        self.tasks = []
        self.configuration = configuration
        self.logger = logger
        self.projects = []
        self.get_projects()
        self.set_tasks()

    def get_projects(self):
        for language in self.configuration.languages:
            with open(language['target'], 'r') as target:
                for line in target:
                    project = TarsProject(line, configuration=self.configuration,
                                          logger=self.logger, language=language['name'], docker=language['docker'])
                    self.projects.append(project)

    def set_tasks(self):
        for project in self.projects:
            self.logger.log_info(f"Project number: {self.projects.index(project)}")
            self.logger.log_info(f"Target project {project.project_id}")
            self.logger.log_info(f"Creating TARS analysis project {project.project_id}.")
            clone = Clone(project)
            analyze = Analyze(project)
            load = Load(project)
            delete = Delete(project)
            analysis_project = AnalysisProject(
                project,
                self.configuration,
                clone,
                analyze,
                load,
                delete,
            )
            self.tasks.append(self.run_analysis(analysis_project))

    async def tars_runner(self):
        # Create batches of tasks to avoid overloading the system
        batch_size = (
            self.configuration.max_concurrency * 10
        )  # Adjust the batch size based on system capacity
        for i in range(0, len(self.tasks), batch_size):
            batch = self.tasks[i : i + batch_size]
            await asyncio.gather(*batch)

    async def run_analysis(self, analysis_project):
        semaphore = asyncio.Semaphore(self.configuration.max_concurrency)
        async with semaphore:
            try:
                self.logger.log_info(f"Running TARS analysis for project {analysis_project.project.project_id}")
                await asyncio.gather(
                    *[analysis_project.run_collect()]
                )
            except Exception as e:
                self.logger.log_error(
                    f"Error running TARS analysis for project {analysis_project.project.project_id}: {e}"
                )
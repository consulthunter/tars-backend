
import os
import aiofiles
import aiofiles.os
from pathlib import Path

class AnalysisProject:
    def __init__(self, project, configuration, clone, analyze, load, delete):
        self.project = project
        self.configuration = configuration
        self.clone = clone
        self.analyze = analyze
        self.load = load
        self.delete = delete

    async def run_collect(self):
        await self.clone.run_clone_async()
        await self.analyze.run_analyze_async()
        await self.load.run_loading_async()
        await self.delete.run_delete_async()
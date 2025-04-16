from tars.core.models.coverage_data import CoverageData
from tars.core.models.source_method import SourceMethod


class NonTestMethod(SourceMethod):
    def __init__(self):
        super().__init__()
        coverage_data = CoverageData
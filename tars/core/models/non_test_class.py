from tars.core.models.coverage_report import CoverageReport
from tars.core.models.source_class import SourceClass


class NonTestClass(SourceClass):
    def __init__(self):
        super().__init__()
        coverage_report = CoverageReport
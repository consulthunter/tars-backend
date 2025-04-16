from tars.core.models.location import Location
from tars.core.models.source_method import SourceMethod
from tars.core.models.test_status import TestStatus

class TestMethod(SourceMethod):
    def __init__(self):
        super().__init__()
        test_type = ""
        status = TestStatus
        assertions = []

from tars.core.models.non_test_class import NonTestClass
from tars.core.models.source_class import SourceClass
from tars.core.models.test_method import TestMethod
from tars.core.models.location import Location
from typing import List

class TestClass(SourceClass):
    def __init__(self):
        super().__init__()
        name = ""
        location = Location
        namespace = ""
        modifiers = ""
        imports = []
        properties = []
        attributes = []
        testing_framework = ""
        body = ""
        replacement = ""
        summary = ""
        test_methods: List[TestMethod] = []
        mapped_non_test_classes: List[NonTestClass] = []

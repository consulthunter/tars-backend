from tars.core.models.location import Location
from tars.core.models.non_test_method import NonTestMethod
from typing import List


class SourceClass:
    def __init__(self):
        name = ""
        location = Location
        namespace = ""
        modifiers = ""
        imports = []
        properties = []
        attributes = []
        body = ""
        replacement = ""
        summary = ""
        non_test_methods: List[NonTestMethod] = []
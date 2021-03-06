import uuid
import base64

from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404

from .models import TestRun, Test, Solution, Language, TestType


class TestFactory:
    @staticmethod
    def create_test(data):
        test_file = base64.b64decode(data['test'])
        test_file = ContentFile(content=test_file, name=str(uuid.uuid4()))
        test = Test(file=test_file)

        if data.get("extra_options", {}).get("archive_test_type"):
            test.is_archive = True

        return test

    @staticmethod
    def create_solution(data):
        solution_file = base64.b64decode(data['solution'])
        solution_file = ContentFile(content=solution_file, name=str(uuid.uuid4()))
        solution = Solution(file=solution_file)

        if data.get("extra_options", {}).get("archive_solution_type"):
            solution.is_archive = True

        return solution


class TestRunFactory:
    @staticmethod
    def create_run(data, files=None):
        language = get_object_or_404(Language, name=data['language'])
        test_type = get_object_or_404(TestType, value=data['test_type'])
        extra_options = data.get('extra_options', {})

        tests = TestFactory.create_test(data)
        tests.save()

        solution = TestFactory.create_solution(data)
        solution.save()

        run = TestRun(status='pending',
                      language=language,
                      test_type=test_type,
                      solution=solution,
                      test=tests,
                      extra_options=extra_options)

        return run

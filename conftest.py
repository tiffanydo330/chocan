import pytest
import client
import report_generator

@pytest.fixture
def _client_fixture():
    return client.Client()

@pytest.fixture
def _report_gen_fixture():
    return report_generator.ReportGenerator()
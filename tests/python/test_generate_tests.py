import pytest
from unittest.mock import patch, MagicMock
from requests.exceptions import RequestException
from test_generator import TestGenerator

@pytest.fixture
def test_generator():
    return TestGenerator()

def test_get_changed_files_no_args(test_generator):
    assert test_generator.get_changed_files() == []

def test_get_changed_files_with_args():
    import sys
    sys.argv = ['test.py', 'file1.py file2.py']
    test_generator = TestGenerator()
    assert test_generator.get_changed_files() == ['file1.py', 'file2.py']

def test_detect_language_python(test_generator):
    assert test_generator.detect_language('file.py') == 'Python'

def test_detect_language_unknown(test_generator):
    assert test_generator.detect_language('file.unknown') == 'Unknown'

def test_get_test_framework_python(test_generator):
    assert test_generator.get_test_framework('Python') == 'pytest'

def test_get_test_framework_unknown(test_generator):
    assert test_generator.get_test_framework('Unknown') == 'unknown'

@patch('requests.post')
def test_call_openai_api_success(mock_post, test_generator):
    mock_response = MagicMock()
    mock_response.json.return_value = {'choices': [{'message': {'content': 'Test code'}}]}
    mock_post.return_value = mock_response

    assert test_generator.call_openai_api('prompt') == 'Test code'

@patch('requests.post')
def test_call_openai_api_request_error(mock_post, test_generator):
    mock_post.side_effect = RequestException()

    assert test_generator.call_openai_api('prompt') is None

def test_create_prompt(test_generator):
    assert test_generator.create_prompt('file.py', 'Python') is not None

def test_save_test_cases_success(test_generator, tmp_path):
    test_cases = 'Generated test cases'
    test_generator.save_test_cases(str(tmp_path / 'file.py'), test_cases, 'Python')
    assert (tmp_path / 'tests/python/test_file.py').read_text() == test_cases

def test_save_test_cases_error(test_generator, tmp_path):
    test_cases = 'Generated test cases'
    with patch('builtins.open', side_effect=IOError):
        test_generator.save_test_cases(str(tmp_path / 'file.py'), test_cases, 'Python')
        assert (tmp_path / 'tests/python/test_file.py').exists() is False
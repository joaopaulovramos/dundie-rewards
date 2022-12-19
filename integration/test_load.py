import pytest
from subprocess import check_output
from tests.constants import PEOPLE_FILE


@pytest.mark.integration
@pytest.mark.medium
def test_load():
    out = check_output(
      ["dundie", "load", PEOPLE_FILE]
      ).decode('utf-8').split('\n')
    assert len(out) == 2

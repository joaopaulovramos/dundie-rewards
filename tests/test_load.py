import pytest
from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load():
    assert len(load(
      PEOPLE_FILE
      )) == 2

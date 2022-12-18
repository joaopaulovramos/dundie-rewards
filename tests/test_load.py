import pytest
from dundie.core import load


@pytest.mark.unit
def test_load():
    assert len(load(
      r'tests/assets/people.csv'
      )) == 2

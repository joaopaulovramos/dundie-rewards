import pytest
from dundie.core import load


@pytest.mark.unit
def test_load():
    assert len(load(
      r'D:\Linuxtips\dundie-rewards\tests\assets\people.csv'
      )) == 2

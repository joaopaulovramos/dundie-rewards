import pytest

from dundie.core import load
from tests.constants import PEOPLE_FILE

EXPECTED_NAMES = ["Jim Halpert", "Dwight Schrute", "Gabe Lewis"]
EXPECTED_DEPTS = ["Sales", "Directory"]
EXPECTED_ROLES = ["Salesman", "Sales Manager", "Manager"]
EMAIL_DOMAIN = "dundlermifflin.com"


@pytest.mark.unit
@pytest.mark.high
def test_load():
    result = load(PEOPLE_FILE)
    assert len(result) == 3

    for line in result:
        data = line.split(",")
        assert data[0] in EXPECTED_NAMES
        assert data[1] in EXPECTED_DEPTS
        assert data[2] in EXPECTED_ROLES
        assert EMAIL_DOMAIN in data[3]

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


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(request):
    """Test function load function."""
    assert load(PEOPLE_FILE)[0]["name"] == "Jim Halpert"

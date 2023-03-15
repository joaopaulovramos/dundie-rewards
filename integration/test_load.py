from subprocess import CalledProcessError, check_output

import pytest

from tests.constants import PEOPLE_FILE


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    out = (
        check_output(["dundie", "load", PEOPLE_FILE])
        .decode("utf-8")
        .split("\n")
    )
    assert len(out) == 2


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command(wrong_command):
    with pytest.raises(CalledProcessError):
        check_output(["dundie", wrong_command, PEOPLE_FILE]).decode(
            "utf-8"
        ).split("\n")

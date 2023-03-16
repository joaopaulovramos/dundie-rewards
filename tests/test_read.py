import pytest

from dundie.core import read
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_read_withy_query():
    db = connect()

    pk = "joe@doe.com"
    data = {"name": "Joe Doe", "role": "Salesman", "dept": "Sale"}
    _, created = add_person(db, pk, data)
    assert created == True
    commit(db)

    pk = "jim@doe.com"
    data = {"name": "Jim Doe", "role": "Manager", "dept": "Management"}
    _, created = add_person(db, pk, data)
    assert created == True
    commit(db)

    response = read()
    assert len(response) == 2

    response = read(dept="Management")
    assert len(response) == 1
    assert response[0]["name"] == "Jim Doe"

    response = read(email="joe@doe.com")
    assert len(response) == 1
    assert response[0]["name"] == "Joe Doe"

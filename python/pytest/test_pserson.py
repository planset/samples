import pytest
from person import Person

class TestPerson(object):
    @pytest.fixture
    def person(self):
        return Person('Daisuke', 99)

    def test_type(self, person):
        assert isinstance(person, Person)

    def test_val(self, person):
        assert person.age == 99

class TestPerson2(object):
    @pytest.fixture
    def person(self):
        return Person('Daisuke', 99)

    def test_type(self, person):
        assert isinstance(person, Person)

    def test_val(self, person):
        assert person.age == 99

if __name__ == '__main__':
    pytest.main()


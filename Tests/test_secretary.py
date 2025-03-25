import pytest

from Tests.secretary import get_name, get_directory, add


@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    original_documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
    ]
    original_directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }
    monkeypatch.setattr("Tests.secretary.documents", original_documents.copy())
    monkeypatch.setattr("Tests.secretary.directories", original_directories.copy())


def test_get_name_existing():
    assert get_name("10006") == "Аристарх Павлов"


def test_get_directory_existing():
    assert get_directory("11-2") == '1'


def test_get_name_non_existing():
    assert get_name("101") == "Документ не найден"


def test_add_document():
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    assert get_directory("311 020203") == '3'
    assert get_name("311 020203") == 'Александр Пушкин'

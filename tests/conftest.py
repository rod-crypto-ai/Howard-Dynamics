import pytest

from howard_site import create_app


@pytest.fixture()
def app(tmp_path):
    database = tmp_path / "test.sqlite3"
    app = create_app(
        {
            "TESTING": True,
            "WTF_CSRF_ENABLED": False,
            "SECRET_KEY": "test-secret",
            "DATABASE": str(database),
            "SERVER_NAME": "localhost",
        }
    )
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

from html import escape

from howard_site.content import CAPABILITIES


def test_public_pages_load(client):
    endpoints = [
        "/",
        "/capabilities",
        "/about",
        "/government-contracting",
        "/contact",
        "/careers",
        "/privacy",
        "/health",
        "/robots.txt",
        "/sitemap.xml",
    ]
    for endpoint in endpoints:
        response = client.get(endpoint)
        assert response.status_code == 200, endpoint


def test_capability_pages_load(client):
    for capability in CAPABILITIES:
        response = client.get(f"/capabilities/{capability['slug']}")
        assert response.status_code == 200
        assert escape(capability["title"]).encode() in response.data


def test_unknown_capability_returns_404(client):
    response = client.get("/capabilities/not-real")
    assert response.status_code == 404


def test_contact_submission_is_saved(client, app):
    response = client.post(
        "/contact",
        data={
            "name": "Test Buyer",
            "email": "buyer@example.gov",
            "phone": "555-555-5555",
            "organization": "Test Agency",
            "interest": "maintenance",
            "message": "We need maintenance support for a defined field requirement.",
            "website": "",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Your message was received" in response.data

    import sqlite3

    with sqlite3.connect(app.config["DATABASE"]) as db:
        row = db.execute("SELECT name, email FROM contact_submissions").fetchone()
    assert row == ("Test Buyer", "buyer@example.gov")


def test_honeypot_does_not_save(client, app):
    response = client.post(
        "/contact",
        data={
            "name": "Spam Bot",
            "email": "spam@example.com",
            "interest": "other",
            "message": "This is a spam submission that should not be stored anywhere.",
            "website": "https://spam.invalid",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200

    import sqlite3

    with sqlite3.connect(app.config["DATABASE"]) as db:
        count = db.execute("SELECT COUNT(*) FROM contact_submissions").fetchone()[0]
    assert count == 0

from __future__ import annotations

import os
from pathlib import Path

from flask import Flask

from .db import close_db, init_db
from .routes import bp


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    database_path = Path(app.instance_path) / "howard_dynamics.sqlite3"
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "development-only-change-me"),
        DATABASE=os.getenv("DATABASE_PATH", str(database_path)),
        COMPANY_NAME=os.getenv("COMPANY_NAME", "Howard Dynamics"),
        COMPANY_TAGLINE=os.getenv("COMPANY_TAGLINE", "Satisfaction is always the mission."),
        COMPANY_LOCATION=os.getenv("COMPANY_LOCATION", "Texarkana, Texas"),
        CONTACT_EMAIL=os.getenv("CONTACT_EMAIL", ""),
        CONTACT_PHONE=os.getenv("CONTACT_PHONE", ""),
        UEI=os.getenv("UEI", ""),
        CAGE_CODE=os.getenv("CAGE_CODE", ""),
        DEBUG=os.getenv("FLASK_DEBUG", "0") == "1",
        MAX_CONTENT_LENGTH=2 * 1024 * 1024,
        WTF_CSRF_TIME_LIMIT=3600,
        SMTP_HOST=os.getenv("SMTP_HOST", ""),
        SMTP_PORT=int(os.getenv("SMTP_PORT", "587")),
        SMTP_USERNAME=os.getenv("SMTP_USERNAME", ""),
        SMTP_PASSWORD=os.getenv("SMTP_PASSWORD", ""),
        SMTP_USE_TLS=os.getenv("SMTP_USE_TLS", "1") == "1",
        SMTP_FROM=os.getenv("SMTP_FROM", ""),
        CONTACT_NOTIFY_TO=os.getenv("CONTACT_NOTIFY_TO", ""),
    )

    if test_config:
        app.config.update(test_config)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    app.teardown_appcontext(close_db)
    app.register_blueprint(bp)

    with app.app_context():
        init_db()

    return app

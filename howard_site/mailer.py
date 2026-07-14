from __future__ import annotations

import smtplib
from email.message import EmailMessage

from flask import current_app


def send_notification(subject: str, body: str, reply_to: str) -> bool:
    config = current_app.config
    required = [
        config.get("SMTP_HOST"),
        config.get("SMTP_USERNAME"),
        config.get("SMTP_PASSWORD"),
        config.get("SMTP_FROM"),
        config.get("CONTACT_NOTIFY_TO"),
    ]
    if not all(required):
        return False

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = config["SMTP_FROM"]
    message["To"] = config["CONTACT_NOTIFY_TO"]
    message["Reply-To"] = reply_to
    message.set_content(body)

    with smtplib.SMTP(config["SMTP_HOST"], config["SMTP_PORT"], timeout=15) as smtp:
        if config.get("SMTP_USE_TLS"):
            smtp.starttls()
        smtp.login(config["SMTP_USERNAME"], config["SMTP_PASSWORD"])
        smtp.send_message(message)

    return True

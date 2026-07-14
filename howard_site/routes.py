from __future__ import annotations

from datetime import UTC, datetime
from smtplib import SMTPException

from flask import (
    Blueprint,
    Response,
    abort,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from .content import CAPABILITIES, CAPABILITY_MAP, DIFFERENTIATORS, NAICS_CODES
from .db import get_db
from .forms import CareerForm, ContactForm
from .mailer import send_notification

bp = Blueprint("main", __name__)


@bp.app_context_processor
def inject_globals() -> dict:
    return {
        "company_name": current_app.config["COMPANY_NAME"],
        "company_tagline": current_app.config["COMPANY_TAGLINE"],
        "company_location": current_app.config["COMPANY_LOCATION"],
        "contact_email": current_app.config["CONTACT_EMAIL"],
        "contact_phone": current_app.config["CONTACT_PHONE"],
        "current_year": datetime.now(UTC).year,
        "nav_capabilities": CAPABILITIES,
    }


@bp.get("/")
def home():
    return render_template(
        "index.html",
        capabilities=CAPABILITIES,
        differentiators=DIFFERENTIATORS,
        page_title="Operations and maintenance services",
        page_description=(
            "Howard Dynamics provides focused operations and maintenance support across "
            "fleet maintenance, facility operations, logistics, field services, and readiness."
        ),
    )


@bp.get("/capabilities")
def capabilities():
    return render_template(
        "capabilities.html",
        capabilities=CAPABILITIES,
        page_title="Capabilities",
        page_description=(
            "Explore Howard Dynamics operations and maintenance services for equipment, "
            "facilities, logistics, field support, and workforce readiness."
        ),
    )


@bp.get("/capabilities/<slug>")
def capability_detail(slug: str):
    capability = CAPABILITY_MAP.get(slug)
    if capability is None:
        abort(404)

    return render_template(
        "capability_detail.html",
        capability=capability,
        page_title=capability["title"],
        page_description=capability["summary"],
    )


@bp.get("/about")
def about():
    return render_template(
        "about.html",
        differentiators=DIFFERENTIATORS,
        page_title="About Howard Dynamics",
        page_description=(
            "Founded in 2017 in Texarkana, Texas, Howard Dynamics delivers focused operations "
            "and maintenance support with field-informed execution and direct accountability."
        ),
    )


@bp.get("/government-contracting")
def government_contracting():
    identifiers = {
        "UEI": current_app.config["UEI"],
        "CAGE Code": current_app.config["CAGE_CODE"],
    }
    identifiers = {key: value for key, value in identifiers.items() if value}
    return render_template(
        "government_contracting.html",
        naics_codes=NAICS_CODES,
        identifiers=identifiers,
        page_title="Government Contracting",
        page_description=(
            "Howard Dynamics supports government agencies, prime contractors, and teaming "
            "partners with scalable operations and maintenance services."
        ),
    )


def _request_metadata() -> tuple[str, str]:
    forwarded_for = request.headers.get("X-Forwarded-For", "")
    source_ip = forwarded_for.split(",")[0].strip() if forwarded_for else request.remote_addr or ""
    return source_ip[:64], request.user_agent.string[:500]


@bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        if form.website.data:
            return redirect(url_for("main.contact"))

        source_ip, user_agent = _request_metadata()
        db = get_db()
        db.execute(
            """
            INSERT INTO contact_submissions
                (name, email, phone, organization, interest, message, source_ip, user_agent)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                form.name.data.strip(),
                form.email.data.strip().lower(),
                form.phone.data.strip(),
                form.organization.data.strip(),
                form.interest.data,
                form.message.data.strip(),
                source_ip,
                user_agent,
            ),
        )
        db.commit()

        body = (
            f"Name: {form.name.data}\n"
            f"Email: {form.email.data}\n"
            f"Phone: {form.phone.data or 'Not provided'}\n"
            f"Organization: {form.organization.data or 'Not provided'}\n"
            f"Interest: {form.interest.data}\n\n"
            f"{form.message.data}\n"
        )
        try:
            send_notification(
                subject=f"Website inquiry from {form.name.data}",
                body=body,
                reply_to=form.email.data,
            )
        except (SMTPException, OSError):
            current_app.logger.exception("Contact notification email failed.")

        flash("Your message was received. Howard Dynamics will follow up directly.", "success")
        return redirect(url_for("main.contact"))

    return render_template(
        "contact.html",
        form=form,
        page_title="Contact",
        page_description=(
            "Discuss an operations and maintenance requirement, request a capability response, "
            "or explore defined subcontracting workshare with Howard Dynamics."
        ),
    )


@bp.route("/careers", methods=["GET", "POST"])
def careers():
    form = CareerForm()
    if form.validate_on_submit():
        if form.website.data:
            return redirect(url_for("main.careers"))

        source_ip, user_agent = _request_metadata()
        db = get_db()
        db.execute(
            """
            INSERT INTO career_submissions
                (name, email, phone, location, specialty, clearance_status, message, source_ip, user_agent)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                form.name.data.strip(),
                form.email.data.strip().lower(),
                form.phone.data.strip(),
                form.location.data.strip(),
                form.specialty.data,
                form.clearance_status.data,
                form.message.data.strip(),
                source_ip,
                user_agent,
            ),
        )
        db.commit()

        body = (
            f"Name: {form.name.data}\n"
            f"Email: {form.email.data}\n"
            f"Phone: {form.phone.data or 'Not provided'}\n"
            f"Location: {form.location.data or 'Not provided'}\n"
            f"Specialty: {form.specialty.data}\n"
            f"Clearance: {form.clearance_status.data}\n\n"
            f"{form.message.data}\n"
        )
        try:
            send_notification(
                subject=f"Career interest from {form.name.data}",
                body=body,
                reply_to=form.email.data,
            )
        except (SMTPException, OSError):
            current_app.logger.exception("Career notification email failed.")

        flash("Your information was received and added to our candidate pipeline.", "success")
        return redirect(url_for("main.careers"))

    return render_template(
        "careers.html",
        form=form,
        page_title="Careers",
        page_description=(
            "Join the Howard Dynamics candidate network for maintenance, facility, logistics, "
            "technical field-service, and operational-support opportunities."
        ),
    )


@bp.get("/privacy")
def privacy():
    return render_template(
        "privacy.html",
        page_title="Privacy",
        page_description="Howard Dynamics website privacy notice.",
    )


@bp.get("/health")
def health():
    return {"status": "ok", "service": "howard-dynamics-site"}, 200


@bp.get("/robots.txt")
def robots():
    body = f"User-agent: *\nAllow: /\nSitemap: {url_for('main.sitemap', _external=True)}\n"
    return Response(body, mimetype="text/plain")


@bp.get("/sitemap.xml")
def sitemap():
    pages = [
        url_for("main.home", _external=True),
        url_for("main.capabilities", _external=True),
        url_for("main.about", _external=True),
        url_for("main.government_contracting", _external=True),
        url_for("main.contact", _external=True),
        url_for("main.careers", _external=True),
        url_for("main.privacy", _external=True),
    ]
    pages.extend(
        url_for("main.capability_detail", slug=item["slug"], _external=True)
        for item in CAPABILITIES
    )
    xml = render_template("sitemap.xml", pages=pages)
    return Response(xml, mimetype="application/xml")


@bp.app_errorhandler(404)
def not_found(_error):
    return render_template("404.html", page_title="Page not found"), 404


@bp.app_errorhandler(500)
def server_error(_error):
    return render_template("500.html", page_title="Server error"), 500

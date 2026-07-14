from __future__ import annotations

from flask_wtf import FlaskForm
from wtforms import EmailField, HiddenField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    email = EmailField("Email", validators=[DataRequired(), Email(), Length(max=254)])
    phone = StringField("Phone", validators=[Optional(), Length(max=40)])
    organization = StringField("Organization", validators=[Optional(), Length(max=150)])
    interest = SelectField(
        "How can we help?",
        choices=[
            ("", "Select an O&M service"),
            ("maintenance", "Fleet & equipment maintenance"),
            ("facility-operations", "Facility & site operations"),
            ("logistics", "Logistics & material support"),
            ("field-services", "Technical workforce & field services"),
            ("training", "Training & readiness support"),
            ("teaming", "Teaming or subcontracting"),
            ("other", "Other O&M requirement"),
        ],
        validators=[DataRequired()],
    )
    message = TextAreaField(
        "Requirement or message",
        validators=[DataRequired(), Length(min=20, max=3000)],
    )
    website = HiddenField("Website")


class CareerForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    email = EmailField("Email", validators=[DataRequired(), Email(), Length(max=254)])
    phone = StringField("Phone", validators=[Optional(), Length(max=40)])
    location = StringField("Current location", validators=[Optional(), Length(max=120)])
    specialty = SelectField(
        "Primary specialty",
        choices=[
            ("", "Select a specialty"),
            ("maintenance", "Fleet / equipment maintenance"),
            ("facility", "Facility / site operations"),
            ("logistics", "Logistics / warehouse / material handling"),
            ("field-service", "Technical field service"),
            ("training", "Training / readiness"),
            ("operator", "Driver / equipment operator"),
            ("site-lead", "Site lead / O&M coordination"),
            ("other", "Other"),
        ],
        validators=[DataRequired()],
    )
    clearance_status = SelectField(
        "Security clearance",
        choices=[
            ("not-provided", "Prefer not to say"),
            ("none", "None"),
            ("eligible", "Eligible / previously held"),
            ("active-secret", "Active Secret"),
            ("active-ts", "Active Top Secret or higher"),
        ],
        validators=[DataRequired()],
    )
    message = TextAreaField(
        "Experience summary",
        validators=[DataRequired(), Length(min=30, max=3000)],
    )
    website = HiddenField("Website")

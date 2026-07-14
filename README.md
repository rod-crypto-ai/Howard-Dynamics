# Howard Dynamics Python Website Rebuild

A clean Flask website for Howard Dynamics, structured around one clear business focus: operations and maintenance (O&M) services. The approved red, white, and slate branding and Howard Dynamics logo are integrated throughout the site.

## What is included

- Modern responsive red-and-white homepage
- Five connected O&M service lines
- Individual O&M service pages
- Approved Howard Dynamics logo and favicon
- Government-contracting and NAICS page
- Contact requirement form
- Career candidate-pipeline form
- SQLite submission storage
- Optional SMTP email notifications
- CSRF protection and spam honeypots
- Mobile navigation and accessible keyboard behavior
- Search-engine metadata, robots.txt, and sitemap.xml
- Automated tests and GitHub Actions
- Docker, Render, and local development configuration

## 1. Open and run in VS Code

Install Python 3.11 or newer.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd howard-dynamics-python-rebuild

python -m venv .venv
```

Activate the environment:

### macOS or Linux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Create the environment file:

```bash
cp .env.example .env
```

On Windows:

```powershell
Copy-Item .env.example .env
```

Generate a secure secret key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy that value into `SECRET_KEY` in `.env`.

Start the website:

```bash
flask --app run.py --debug run
```

Open:

```text
http://127.0.0.1:5000
```

## 2. Run quality checks

```bash
ruff check .
pytest -q
```

GitHub Actions runs both commands on every pull request and push to `main` or `develop`.

## 3. Information you must verify before launch

Do not launch the site with guessed procurement information.

Update `.env` with:

- Official legal business name
- Public contact email
- Public business phone
- Verified UEI
- Verified CAGE code
- Correct headquarters wording

Review `howard_site/content.py` and remove any NAICS code or O&M service Howard Dynamics cannot support through experience, qualified personnel, partners, or a realistic execution plan.

## 4. Contact form storage

Contact and candidate submissions are stored in:

```text
instance/howard_dynamics.sqlite3
```

The database is created automatically.

To inspect it in VS Code, install a trusted SQLite viewer extension, or run:

```bash
sqlite3 instance/howard_dynamics.sqlite3
```

Then:

```sql
.tables
SELECT * FROM contact_submissions;
SELECT * FROM career_submissions;
```

Do not commit the database. It is already excluded by `.gitignore`.

## 5. Optional email notifications

Set these values in `.env`:

```text
SMTP_HOST=
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_USE_TLS=1
SMTP_FROM=
CONTACT_NOTIFY_TO=
```

Forms still save to SQLite when email notification is not configured or temporarily fails.

For production, use a dedicated transactional email provider. Do not put a personal email password in GitHub.

## 6. Push to GitHub

Create an empty GitHub repository, then run:

```bash
git init
git add .
git commit -m "Rebuild Howard Dynamics website in Flask"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Use branches for changes:

```bash
git checkout -b feature/update-capabilities
```

After changes:

```bash
git add .
git commit -m "Refine maintenance capability content"
git push -u origin feature/update-capabilities
```

Open a pull request and let GitHub Actions test the change before merging.

## 7. Deployment

### Render

This repository includes `render.yaml`.

1. Push the repository to GitHub.
2. Create a new Render Blueprint or Web Service from the repository.
3. Add environment variables from `.env`.
4. Attach persistent storage or move form submissions to a managed database before relying on them operationally.
5. Point the Howard Dynamics domain to the deployed service after testing.

### Docker

```bash
cp .env.example .env
docker compose up --build
```

Open:

```text
http://127.0.0.1:8000
```

### SiteGround warning

A basic shared-hosting account is a poor fit for a continuously running Flask application. Python scripts may exist on the account, but that does not guarantee a supported production WSGI process, persistent application service, or dependency control.

The practical choices are:

1. Host this Python app on Render, Railway, Fly.io, Google Cloud Run, or a VPS and point the domain to it.
2. Keep SiteGround only for the domain/DNS or existing email.
3. Convert this design to a static site if you insist on simple shared hosting, then use an external form service.

Do not force a Python application into unsuitable hosting just because the domain is already there.

## 8. Recommended launch sequence

1. Run locally and review every page.
2. Verify the logo scale and placement on desktop and mobile.
3. Verify contact details, UEI, CAGE, NAICS, and O&M service claims.
4. Add the approved capability statement after it is finalized.
5. Configure production email and database storage.
6. Run tests.
7. Deploy to a staging URL.
8. Test mobile navigation, every form, sitemap, and error pages.
9. Connect the domain.
10. Keep the old site available until the new site is verified.

## Project structure

```text
howard-dynamics-python-rebuild/
├── .github/workflows/ci.yml
├── howard_site/
│   ├── static/
│   │   ├── css/styles.css
│   │   ├── img/
│   │   └── js/main.js
│   ├── templates/
│   ├── __init__.py
│   ├── content.py
│   ├── db.py
│   ├── forms.py
│   ├── mailer.py
│   └── routes.py
├── tests/
├── .env.example
├── compose.yaml
├── Dockerfile
├── pyproject.toml
├── render.yaml
├── requirements.txt
├── requirements-dev.txt
└── run.py
```

# O&M Website Rebuild Notes

## Completed

- Repositioned Howard Dynamics around one primary business focus: operations and maintenance services.
- Replaced the broad six-service structure with five connected O&M service lines:
  - Fleet & Equipment Maintenance
  - Facility & Site Operations
  - Logistics & Material Support
  - Technical Workforce & Field Services
  - Training & Readiness Support
- Rewrote the homepage, service pages, About page, Government Contracting page, Contact page, and Careers page.
- Rebuilt the visual system around the approved Howard Dynamics logo using red, white, and slate.
- Added optimized full-logo, logo-mark, and favicon image assets.
- Updated navigation, form choices, metadata, NAICS presentation, and mobile styling.
- Updated automated tests for HTML-safe capability titles.

## Verified

- `ruff check .` passes.
- `pytest -q` passes: 5 tests.

## Must be verified before launch

- Public email and phone number
- Legal business name
- UEI and CAGE code
- Current SAM.gov NAICS registrations
- Any capability or past-performance claims added later
- Production email and database configuration

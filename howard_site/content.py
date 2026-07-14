from __future__ import annotations

CAPABILITIES = [
    {
        "slug": "fleet-equipment-maintenance",
        "title": "Fleet & Equipment Maintenance",
        "eyebrow": "Asset readiness",
        "summary": (
            "Preventive and corrective maintenance support that keeps vehicles, "
            "equipment, and mission assets available, documented, and ready for use."
        ),
        "outcomes": [
            "Improved equipment availability",
            "Reduced repeat faults and downtime",
            "Clear maintenance status and records",
            "Faster field-level response",
        ],
        "services": [
            "Preventive maintenance inspections and services",
            "Diagnostics, troubleshooting, and corrective repair support",
            "Field service representative and technician coverage",
            "Equipment condition assessments and readiness reviews",
            "Parts, tools, and support-equipment coordination",
            "Maintenance documentation, work-order status, and reporting",
        ],
        "buyers": [
            "Defense and civilian agencies",
            "Fleet and equipment operators",
            "Installation support organizations",
            "Prime contractors requiring maintenance workshare",
        ],
    },
    {
        "slug": "facility-site-operations",
        "title": "Facility & Site Operations",
        "eyebrow": "Reliable daily operations",
        "summary": (
            "Practical site-support services that keep facilities, work areas, and "
            "operational infrastructure safe, functional, and accountable."
        ),
        "outcomes": [
            "More reliable facility operations",
            "Faster work-order response",
            "Improved site condition and safety",
            "Consistent operational reporting",
        ],
        "services": [
            "Routine facility and site-support services",
            "Work-order intake, tracking, and closeout coordination",
            "Grounds, shop, yard, and common-area support",
            "Minor repair and maintenance coordination",
            "Vendor, subcontractor, and service-provider oversight",
            "Site inspections, status reporting, and issue escalation",
        ],
        "buyers": [
            "Military installations",
            "Government facilities",
            "Industrial and commercial sites",
            "Prime contractors managing base or site operations",
        ],
    },
    {
        "slug": "logistics-material-support",
        "title": "Logistics & Material Support",
        "eyebrow": "Supply continuity",
        "summary": (
            "Receiving, inventory, warehousing, material movement, and transportation "
            "support built around accurate accountability and uninterrupted operations."
        ),
        "outcomes": [
            "Reliable material flow",
            "Better inventory visibility",
            "Reduced receiving and issue delays",
            "Documented supply accountability",
        ],
        "services": [
            "Receiving, staging, inventory, and issue support",
            "Warehouse and storage operations",
            "Material handling and forklift support",
            "Transportation and delivery coordination",
            "Parts and supply accountability",
            "Surge support for fielding, reset, and high-volume requirements",
        ],
        "buyers": [
            "Defense logistics organizations",
            "Government supply activities",
            "Prime contractors and integrators",
            "Fleet, warehouse, and distribution operations",
        ],
    },
    {
        "slug": "technical-workforce-field-services",
        "title": "Technical Workforce & Field Services",
        "eyebrow": "Qualified people at the point of need",
        "summary": (
            "Deployable technicians, mechanics, logisticians, operators, and site-support "
            "personnel backed by defined supervision and performance accountability."
        ),
        "outcomes": [
            "Faster staffing against mission demand",
            "Scalable surge and long-term coverage",
            "Defined roles and performance expectations",
            "Reduced mobilization burden",
        ],
        "services": [
            "Mechanics, technicians, and field service representatives",
            "Logistics, warehouse, and material-handling personnel",
            "Equipment operators and drivers",
            "Site leads, coordinators, and administrative support",
            "Recruiting, screening, onboarding, and deployment",
            "Subcontractor and teammate staffing support",
        ],
        "buyers": [
            "Government program offices",
            "Prime contractors",
            "Small-business teaming partners",
            "Organizations with distributed or variable staffing needs",
        ],
    },
    {
        "slug": "training-readiness-support",
        "title": "Training & Readiness Support",
        "eyebrow": "Sustained performance",
        "summary": (
            "Hands-on instruction, qualification support, job aids, and readiness "
            "assessments that strengthen operator and maintainer capability."
        ),
        "outcomes": [
            "Improved operator and maintainer proficiency",
            "Standardized task qualification",
            "Better knowledge transfer",
            "Measurable readiness improvement",
        ],
        "services": [
            "Equipment and technical training",
            "On-the-job training and apprenticeship support",
            "Qualification cards and task standards",
            "Training-material and job-aid development",
            "Readiness and skills-gap assessments",
            "Instructor and training-event support",
        ],
        "buyers": [
            "Military units",
            "Government training organizations",
            "Prime contractors",
            "Fleet and equipment operators",
        ],
    },
]

CAPABILITY_MAP = {item["slug"]: item for item in CAPABILITIES}

NAICS_CODES = [
    {"code": "561210", "title": "Facilities Support Services"},
    {"code": "811111", "title": "General Automotive Repair"},
    {"code": "811114", "title": "Specialized Automotive Repair"},
    {"code": "811310", "title": "Commercial and Industrial Machinery and Equipment Repair and Maintenance"},
    {"code": "488999", "title": "All Other Support Activities for Transportation"},
    {"code": "493110", "title": "General Warehousing and Storage"},
    {"code": "541614", "title": "Process, Physical Distribution, and Logistics Consulting Services"},
    {"code": "561320", "title": "Temporary Help Services"},
    {"code": "611430", "title": "Professional and Management Development Training"},
]

DIFFERENTIATORS = [
    {
        "title": "O&M-focused delivery",
        "body": "Every service is tied to keeping assets, facilities, people, and material ready for operations.",
    },
    {
        "title": "Field-informed execution",
        "body": "Work plans are built around actual site conditions, maintenance realities, access limits, and operational priorities.",
    },
    {
        "title": "Direct accountability",
        "body": "Customers receive defined ownership, documented status, and early escalation when performance is at risk.",
    },
    {
        "title": "Scalable support",
        "body": "Howard Dynamics can support direct requirements, subcontracted workshare, surge staffing, and distributed operations.",
    },
]

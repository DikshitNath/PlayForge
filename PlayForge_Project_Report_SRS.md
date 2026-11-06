# LOVELY PROFESSIONAL UNIVERSITY
## SCHOOL OF COMPUTER SCIENCE AND ENGINEERING

# Software Requirements Specification (SRS)
## PlayForge Studio: Creative Toys & Games Innovation & Prototyping Platform

**BACHELOR OF TECHNOLOGY IN COMPUTER SCIENCE AND ENGINEERING / INFORMATION TECHNOLOGY**

---

### SUBMITTED BY
- **Name of Candidate:** Dikshit
- **University Roll Number:** [Roll Number]
- **Section / Group:** [Section / Group]

### UNDER THE SUPERVISION OF
- **Supervisor:** Assistant Professor, School of Computer Science and Engineering
- **SUBMISSION DATE:** 06/11/2026

---

## Table of Contents
- [1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Scope](#12-scope)
  - [1.3 Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
  - [1.4 References](#14-references)
  - [1.5 Overview](#15-overview)
- [2. General Description](#2-general-description)
  - [2.1 Product Perspective](#21-product-perspective)
  - [2.2 Product Functions](#22-product-functions)
  - [2.3 User Characteristics](#23-user-characteristics)
  - [2.4 General Constraints](#24-general-constraints)
  - [2.5 Assumptions and Dependencies](#25-assumptions-and-dependencies)
- [3. Specific Requirements](#3-specific-requirements)
  - [3.1 External Interface Requirements](#31-external-interface-requirements)
    - [3.1.1 User Interfaces](#311-user-interfaces)
    - [3.1.2 Hardware Interfaces](#312-hardware-interfaces)
    - [3.1.3 Software Interfaces](#313-software-interfaces)
    - [3.1.4 Communications Interfaces](#314-communications-interfaces)
  - [3.2 Functional Requirements](#32-functional-requirements)
    - [3.2.1 Invention Blueprint Management & Publishing](#321-invention-blueprint-management--publishing)
    - [3.2.2 The Novelty Factor Analysis Engine](#322-the-novelty-factor-analysis-engine)
    - [3.2.3 PlayLab Virtual Arcade - CogCraft Physics Sandbox](#323-playlab-virtual-arcade---cogcraft-physics-sandbox)
    - [3.2.4 PlayLab Virtual Arcade - ChromaTiles Optical Tabletop](#324-playlab-virtual-arcade---chromatiles-optical-tabletop)
    - [3.2.5 PlayLab Virtual Arcade - GearSmith Kinematic Automata](#325-playlab-virtual-arcade---gearsmith-kinematic-automata)
    - [3.2.6 Spark Ideation Engine (Combinatorial Randomizer)](#326-spark-ideation-engine-combinatorial-randomizer)
    - [3.2.7 Maker Design Challenges & Competitions](#327-maker-design-challenges--competitions)
    - [3.2.8 Playtesting Feedback & Multi-Axis Matrix](#328-playtesting-feedback--multi-axis-matrix)
    - [3.2.9 Live Spark Voting & Upvote Telemetry](#329-live-spark-voting--upvote-telemetry)
    - [3.2.10 Patent-Grade Maker Specification Sheet Export](#3210-patent-grade-maker-specification-sheet-export)
  - [3.3 Non-Functional Requirements](#33-non-functional-requirements)
    - [3.3.1 Performance](#331-performance)
    - [3.3.2 Reliability](#332-reliability)
    - [3.3.3 Availability](#333-availability)
    - [3.3.4 Security](#334-security)
    - [3.3.5 Maintainability](#335-maintainability)
    - [3.3.6 Portability](#336-portability)
  - [3.4 Design Constraints](#34-design-constraints)
  - [3.5 Other Requirements](#35-other-requirements)
- [4. Analysis Models](#4-analysis-models)
  - [4.1 Data Flow Diagrams (DFD)](#41-data-flow-diagrams-dfd)
    - [Level 0 (Context Diagram)](#level-0-context-diagram)
    - [Level 1 DFD](#level-1-dfd)
  - [4.2 Entity Relationship Diagram (ERD)](#42-entity-relationship-diagram-erd)
  - [4.3 Creation Status & Prototyping Lifecycle](#43-creation-status--prototyping-lifecycle)
- [5. GitHub Link & Source Repository](#5-github-link--source-repository)
- [6. Deployed Link & Execution Guide](#6-deployed-link--execution-guide)
- [7. System Verification & Test Suite Proof](#7-system-verification--test-suite-proof)
- [A. Appendices](#a-appendices)
  - [A.1 Appendix 1: Demo Accounts & Roles](#a1-appendix-1-demo-accounts--roles)
  - [A.2 Appendix 2: Project Modules & App Architecture](#a2-appendix-2-project-modules--app-architecture)
  - [A.3 Appendix 3: Seeded Unique Toy & Game Inventions](#a3-appendix-3-seeded-unique-toy--game-inventions)

---

# 1. Introduction

This document is the Software Requirements Specification (SRS) for **PlayForge Studio**, an interactive web platform and prototyping laboratory built to fulfill the challenge: **"Toys & Games - Challenges your creative minds to conceptualize and develop unique toys & games."**

It specifies the architectural, functional, and non-functional requirements of the system, organized according to the **IEEE Std 830-1998** standard for Software Requirements Specifications.

### 1.1 Purpose
The purpose of this SRS is to define the technical requirements and architecture of the PlayForge platform. The intended audience includes software evaluators, academic review committees, product designers, educators, and open-source makers. It establishes the baseline for implementation, testing, verification, and deployment.

### 1.2 Scope
**PlayForge Studio** is a server-rendered, responsive web application engineered using the Django 6 framework. It empowers makers, inventors, game designers, and STEM students to move from conceptual brainstorm to interactive digital simulation and physical workshop fabrication.

**PlayForge will:**
- Allow inventors to draft and publish technical **Invention Blueprints** with detailed novelty statements, Bill of Materials (BOM), tools, rules of play, and STEM curriculum alignment.
- Run real-time, in-browser interactive prototypes in the **PlayLab Virtual Arcade**:
  - *CogCraft 2D Physics & Acoustic Escapement Sandbox* (with Web Audio API synthesized chimes).
  - *ChromaTiles Tactical Light-Grid Board Game* (with real-time ray-tracing optics, playable Hotseat 2-Player or vs AI Bot).
  - *GearSmith Kinematic Automaton Lab* (compound gear reduction and four-bar linkage puppet synthesis).
- Provide the **Spark Ideation Engine**, a combinatorial randomizer synthesizing audience demographics, physical mechanics, unusual materials, and narrative themes.
- Host **Maker Design Challenges** with strict constraints (e.g. Zero-G play for astronauts, single-sheet origami folding mechanisms).
- Offer a multi-axis **Playtesting Review System** (Fun, Originality, Durability, and STEM value).
- Render print-ready, high-contrast **Maker Specification Sheets** (`/print/`) formatted for PDF export and laser cutting/3D printing workshops.

**PlayForge will not:**
- Require native device installation (runs in all modern evergreen web browsers).
- Conduct financial e-commerce transactions or process credit card payments in this version.

---

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
| :--- | :--- |
| **SRS** | Software Requirements Specification |
| **STEM** | Science, Technology, Engineering, and Mathematics |
| **BOM** | Bill of Materials (list of raw components, fasteners, and parts required for fabrication) |
| **Ray Tracing** | An optical computation method calculating the reflection and refraction path of light beams |
| **Escapement** | A mechanical device in clockwork that arrests and releases energy in regulated impulses |
| **Four-Bar Linkage** | A movable chain of four rigid bodies pinned together to generate non-linear harmonic paths |
| **CRUD** | Create, Read, Update, Delete |
| **CSRF** | Cross-Site Request Forgery |
| **DFD** | Data Flow Diagram |
| **ORM** | Object-Relational Mapper (Django ORM) |
| **Web Audio API** | High-level browser JavaScript API for synthesizing and processing audio signals |
| **Hotseat** | Local multiplayer mode where players alternate turns on the same physical screen |

---

### 1.4 References
- **IEEE Std 830-1998**: *IEEE Recommended Practice for Software Requirements Specifications*.
- **Django Software Foundation**: *Django 6.1 Documentation*, https://docs.djangoproject.com.
- **Mozilla Developer Network (MDN)**: *HTML5 Canvas and Web Audio API Guides*, https://developer.mozilla.org.
- **Tailwind CSS Framework**: *Tailwind CSS v3.4 Documentation*, https://tailwindcss.com.
- **PlayForge Studio Source Repository & README** (see Section 5).

### 1.5 Overview
Section 2 describes general product factors and context. Section 3 delineates external interfaces, functional specifications, and non-functional constraints. Section 4 provides formal Data Flow Diagrams (Level 0 and Level 1). Sections 5 to 7 provide development repository links, setup guides, and automated test suite verification evidence.

---

# 2. General Description

### 2.1 Product Perspective
PlayForge Studio is an independent, self-contained Django web application. It connects three core user workflows that typically operate in isolation:
1. **Conceptual Ideation**: Generating novel mechanics through constraint-based brainstorming.
2. **Digital Prototyping**: Testing mechanics in a simulator before buying materials.
3. **Physical Fabrication & Community Playtesting**: Documenting step-by-step assembly guides, cut lists, and recording physical play logs.

The platform is structured into clean modular components (`creations`, `playforge`), backed by an SQLite relational database in development (switchable to PostgreSQL for production), and rendered using responsive HTML5/Tailwind templates.

```
                    ┌───────────────────────────────────────────────┐
                    │               Web Browser Client              │
                    │   (Desktop, Tablet, Mobile Browser Viewports)  │
                    └───────────────────────▲───────────────────────┘
                                            │ HTTP / JSON
                                            ▼
                    ┌───────────────────────────────────────────────┐
                    │             Django 6 Web Engine               │
                    │  ├── URL Routing (creations.urls)             │
                    │  ├── Controllers & Views (creations.views)    │
                    │  ├── Form Validators (creations.forms)        │
                    │  └── Template Engine (Jinja / Django DTL)     │
                    └───────────────────────▲───────────────────────┘
                                            │ Django ORM
                                            ▼
                    ┌───────────────────────────────────────────────┐
                    │          Relational Database (SQLite)         │
                    │  ├── Category & Creation Models               │
                    │  ├── PlaytestReview & Challenge Models        │
                    │  └── ChallengeSubmission Models               │
                    └───────────────────────────────────────────────┘
```

### 2.2 Product Functions
- **Invention Publishing & Blueprint Browsing**: Categorized showcase of toys, board games, and sensory devices with live keyword search and multi-criteria filters.
- **Interactive Prototyping Arcade (PlayLab)**: Real-time interactive physics, optical beam reflections, and linkage kinematics.
- **Spark Ideation Generator**: Multi-dial randomizer generating target demographic, mechanism, materials, and thematic narrative.
- **Design Challenges & Hackathon Submissions**: Open challenges with enforced constraints (e.g., zero gravity, one single sheet).
- **Playtest Log & Metric Matrix**: 4-dimensional rating (Fun, Innovation, Durability, STEM) and community modification notes.
- **Printable Maker Specifications Sheet**: Formatted clean view for printing cut lists and manuals.

### 2.3 User Characteristics

| User Role | Profile & Characteristics |
| :--- | :--- |
| **Toy / Game Maker** | Hobbyist, student, or engineer drafting original mechanical toys or board games; needs structured forms to document parts, tools, and rules. |
| **Player / Playtester** | Casual gamer or student testing browser prototypes and logging physical playtest results and feedback. |
| **STEM Educator** | Teacher looking for physics, optics, or kinematics models with curricular mapping and printable maker sheets. |
| **Platform Administrator** | Staff managing categories, reviewing challenge entries, and moderating blueprints. |

### 2.4 General Constraints
- **Language & Framework**: Python 3.14 with Django 6.1.3 web framework.
- **Architecture**: Model-View-Template (MVT) server-side architecture.
- **Client Requirements**: Modern browser supporting HTML5 Canvas (2D Context) and Web Audio API.
- **Security**: Mandatory CSRF protection on all POST operations; server-side sanitization.
- **Responsiveness**: Responsive across 360px mobile viewports to 4K ultra-wide desktop displays.

### 2.5 Assumptions and Dependencies
- Users possess an internet connection and an HTML5-compliant browser (Chrome, Edge, Firefox, Safari).
- Audio hardware (speakers/headphones) is available for Web Audio acoustic chime synthesis.
- Python 3 and Django runtime environment are available on the deployment host.

---

# 3. Specific Requirements

## 3.1 External Interface Requirements

### 3.1.1 User Interfaces
- Responsive dark-mode interface styled using Tailwind CSS and custom design system (`static/css/style.css`).
- Navigation bar with direct links to Blueprints, PlayLab, Spark Engine, Challenges, and "Forge Invention".
- Canvas arenas with HUD overlays for physics telemetry (ball count, chime triggers, laser score, crank RPM).

### 3.1.2 Hardware Interfaces
- No proprietary hardware required. The platform interacts with standard pointing devices (mouse, trackpad, touch screen) for drawing canvas ramps and rotating mirrors.

### 3.1.3 Software Interfaces

| Software Component | Version / Spec | Purpose |
| :--- | :--- | :--- |
| **Python** | 3.14+ | Core backend runtime environment |
| **Django Framework** | 6.1.3 | Web routing, ORM, security, templating |
| **SQLite / PostgreSQL** | 3.x / 14+ | Persistent relational data store |
| **Tailwind CSS** | CDN v3.4 | Utility-first responsive design system |
| **FontAwesome** | 6.5.1 CDN | Universal iconography |
| **HTML5 Canvas & Web Audio** | W3C Standard | Real-time interactive physics & audio synthesis |

### 3.1.4 Communications Interfaces
- Standard HTTP/1.1 or HTTP/2 protocol. HTTPS enforced in production environments.
- AJAX XMLHttpRequest / JSON communication for live upvoting (Sparks).

---

## 3.2 Functional Requirements

### 3.2.1 Invention Blueprint Management & Publishing
- **Introduction**: Enables creators to draft, review, and publish detailed toy and game specifications.
- **Inputs**: Title, Tagline, Classification (`TOY`, `GAME`, `HYBRID`), Category, Creator Name, Novelty Factor, Full Concept, Age Range, Player Count, Play Time, Difficulty, Materials List, Tools, Rules/Build Steps, Safety Advisories, STEM Fields, Prototype Type.
- **Processing**:
  - `SPEC-1`: Auto-generate unique URL-friendly slugs using `django.utils.text.slugify`.
  - `SPEC-2`: Validate numerical ranges (`target_age_min <= target_age_max`, `player_count_min <= player_count_max`).
  - `SPEC-3`: Parse multi-line materials strings into structured checklist arrays.
- **Outputs**: Published blueprint page (`/creations/<slug>/`), listing in discovery grid.
- **Error Handling**: Form validation errors highlighted adjacent to invalid inputs; submission blocked until corrected.

### 3.2.2 The Novelty Factor Analysis Engine
- **Introduction**: Enforces that every submitted toy or game contains an explicit, patent-style novelty statement.
- **Processing**:
  - `NOV-1`: The system requires a dedicated `novelty_factor` field describing the unique physical, mechanical, or gameplay element.
  - `NOV-2`: Renders the novelty statement in a prominent high-contrast callout box on both the detail page and discovery card.

### 3.2.3 PlayLab Virtual Arcade - CogCraft Physics Sandbox
- **Introduction**: An interactive 2D kinetic contraption simulation environment.
- **Inputs**: Mouse drag coordinates for ramp drawing; tool selection (`Ramp`, `Bounce Peg`, `Sound Chime`, `Booster`, `Portal`, `Eraser`); gravity calibration slider; continuous auto-drop toggle.
- **Processing**:
  - `SIM-1`: Calculate real-time ball trajectories using Newton's laws: $\vec{v}_{t+1} = \vec{v}_t + \vec{g}\Delta t$, $\vec{x}_{t+1} = \vec{x}_t + \vec{v}\Delta t$.
  - `SIM-2`: Detect circle-to-line-segment collisions and reflect velocity vectors along the normal vector: $\vec{v}' = \vec{v} - 2(\vec{v}\cdot\hat{n})\hat{n}$.
  - `SIM-3`: When a ball strikes a `Sound Chime`, trigger the Web Audio API oscillator at the specified pentatonic frequency ($261.63\text{ Hz}$ to $659.25\text{ Hz}$) with exponential gain decay.
- **Outputs**: Rendered 60 FPS Canvas animation, real-time ball counter, and acoustic feedback.

### 3.2.4 PlayLab Virtual Arcade - ChromaTiles Optical Tabletop
- **Introduction**: A playable 8x8 ray-tracing optical board game prototype.
- **Inputs**: Grid cell click to place $45^\circ$ mirror tile (╱ or ╲); click existing tile to rotate $90^\circ$; Game Mode selector (`Single Player vs AI`, `Hotseat 2-Player`).
- **Processing**:
  - `OPT-1`: Ray trace laser beams from emitter coordinates:
    - Emitter 1 (Cyan): Origin $(0, 0)$, direction vector $(0, 1)$ (Right).
    - Emitter 2 (Amber): Origin $(7, 7)$, direction vector $(0, -1)$ (Left).
  - `OPT-2`: Calculate $90^\circ$ reflection vector upon encountering mirror tiles:
    - For $45^\circ$ Right (╱): $(dr, dc) \to (-dc, -dr)$.
    - For $45^\circ$ Left (╲): $(dr, dc) \to (dc, dr)$.
  - `OPT-3`: When a laser intersects a Power Crystal, award 1 Energy Spark to the beam owner.
  - `OPT-4`: Implement Greedy AI Bot ("Optic-1") evaluating hypothetical tile placements to maximize crystal hits.
- **Outputs**: Glowing neon laser paths, interactive scoreboards, victory modal upon reaching 10 Energy Sparks.

### 3.2.5 PlayLab Virtual Arcade - GearSmith Kinematic Automata
- **Introduction**: A simulation of compound gear reduction and four-bar linkages driving biomimetic puppets.
- **Inputs**: Input crank RPM slider ($0 - 100\text{ RPM}$); rotation direction toggle; puppet selector (`Flapping Ornithopter`, `Biomimetic Manta Ray`).
- **Processing**:
  - `KIN-1`: Calculate gear meshing angle: $\theta_{\text{follower}} = -\theta_{\text{drive}} \cdot \left(\frac{N_{\text{drive}}}{N_{\text{follower}}}\right)$.
  - `KIN-2`: Calculate eccentric cam pin coordinates: $x = x_0 + r_{\text{cam}}\cos(\theta)$, $y = y_0 + r_{\text{cam}}\sin(\theta)$.
  - `KIN-3`: Propagate rocker arm harmonic oscillation to wing/fin pivot angles: $\alpha = \sin(\theta)\cdot \alpha_{\text{max}}$.
- **Outputs**: Real-time rotating gear teeth, articulated puppet flapping motion, kinematic telemetry readout.

### 3.2.6 Spark Ideation Engine (Combinatorial Randomizer)
- **Introduction**: Algorithmic concept generator resolving creator's block.
- **Inputs**: "Spin Ideation Engine" click trigger.
- **Processing**:
  - `SPRK-1`: Randomly sample from 4 discrete combinatorial pools:
    1. *Target Demographic* ($N=7$)
    2. *Physics / Gameplay Mechanism* ($N=8$)
    3. *Physical Medium / Material* ($N=7$)
    4. *Thematic Narrative* ($N=7$)
  - `SPRK-2`: Synthesize a composite title, pitch paragraph, and novelty factor.
  - `SPRK-3`: URL-encode generated values into query parameters linking to the blueprint form (`/creations/new/?spark_title=...`).
- **Outputs**: Animated slot dials, synthesized pitch card, and pre-filled blueprint builder button.

### 3.2.7 Maker Design Challenges & Competitions
- **Introduction**: Constraint-driven hackathon briefs.
- **Inputs**: Challenge submission selection linking an existing creation to an active challenge.
- **Processing**:
  - `CHAL-1`: Verify challenge `is_active` status.
  - `CHAL-2`: Enforce uniqueness constraint via `ChallengeSubmission.unique_together = ('challenge', 'creation')`.
- **Outputs**: Challenge brief page, list of submitted competing entries, entry count badge.

### 3.2.8 Playtesting Feedback & Multi-Axis Matrix
- **Introduction**: Community review and physical validation logging.
- **Inputs**: Playtester handle, ratings ($1-5$) for Overall, Fun Factor, Originality, Durability, and STEM Value; written observations; DIY hack / modification suggestion.
- **Processing**:
  - `REV-1`: Record `PlaytestReview` model instance linked to target `Creation`.
  - `REV-2`: Calculate arithmetic mean for `average_rating()`: $\bar{R} = \frac{1}{N}\sum_{i=1}^N R_i$.
- **Outputs**: Chronological review feed, star breakdown, highlighted maker mod suggestions.

### 3.2.9 Live Spark Voting & Upvote Telemetry
- **Introduction**: Community appreciation mechanism without page reload.
- **Processing**:
  - `VOTE-1`: Handle asynchronous GET/POST request to `/creations/<slug>/spark/?format=json`.
  - `VOTE-2`: Toggle user session spark list to prevent duplicate consecutive votes.
  - `VOTE-3`: Increment/decrement `sparks_count` atomically and return JSON payload.
- **Outputs**: Live updated numeric count on client button.

### 3.2.10 Patent-Grade Maker Specification Sheet Export
- **Introduction**: Generates a high-contrast printable specification sheet.
- **Processing**:
  - `PRNT-1`: Render dedicated view `/creations/<slug>/print/` formatted with CSS `@media print` rules.
  - `PRNT-2`: Formats Bill of Materials into a physical checkbox cut list with tool advisories and safety warnings.
- **Outputs**: Clean monochrome document suitable for printing or PDF export.

---

## 3.3 Non-Functional Requirements

### 3.3.1 Performance
- Page response time shall not exceed **150 ms** for database-driven views on local deployment.
- The interactive physics and optics canvas simulators shall maintain a consistent **60 FPS** frame rate during active simulation.
- Web Audio API tone synthesis latency shall remain below **20 ms**.

### 3.3.2 Reliability
- Database integrity enforced via foreign key constraints (`models.CASCADE` and `models.SET_NULL`).
- 100% of automated unit tests in test suite shall pass without failures or errors.

### 3.3.3 Availability
- The system operates continuously with minimal server overhead using Django's WSGI/ASGI application architecture.

### 3.3.4 Security
- CSRF token validation enforced on all form submissions.
- Strict input sanitization and XSS prevention via Django template auto-escaping.
- Passwords (for Django Admin / Auth) hashed using PBKDF2 with SHA-256 algorithm.

### 3.3.5 Maintainability
- Code organized under modular separation of concerns:
  - Models (`creations/models.py`)
  - Views (`creations/views.py`)
  - Forms (`creations/forms.py`)
  - Management Commands (`creations/management/commands/seed_data.py`)
  - Unit Tests (`creations/tests.py`)
- Single source of truth for global layouts in `templates/base.html`.

### 3.3.6 Portability
- Platform-agnostic execution across Windows, Linux, and macOS.
- Portable relational schema running seamlessly on SQLite for local development and PostgreSQL for production deployment.

---

## 3.4 Design Constraints
- Built using **Python 3** and **Django 6** server-rendered architecture.
- Front-end styling powered by **Tailwind CSS** without heavy client-side JavaScript frameworks (React/Vue/Angular), ensuring zero build step requirements and rapid load times.
- Native HTML5 Canvas 2D rendering without external third-party physics engine libraries, ensuring full transparency of mathematical collision and ray-tracing algorithms.

---

# 4. Analysis Models

## 4.1 Data Flow Diagrams (DFD)

### Level 0 (Context Diagram)
The Level 0 context diagram models PlayForge Studio as a central system exchanging data with four primary entities: **Toy & Game Maker**, **Player / Playtester**, **STEM Educator**, and **Platform Administrator**.

```
    ┌───────────────────────┐                               ┌───────────────────────┐
    │   Toy & Game Maker    │                               │  Player / Playtester  │
    └───────────┬───────────┘                               └───────────┬───────────┘
                │  1. Submit Blueprint Specification                    │  1. Play Simulator Moves
                │  2. Define Novelty & BOM                              │  2. Log Playtest Rating & Hacks
                │  3. Submit to Challenge                               │  3. Ignite Sparks (Upvotes)
                ▼                                                       ▼
  ═════════════════════════════════════════════════════════════════════════════════════════
                                   PlayForge Studio Platform (0)
  ═════════════════════════════════════════════════════════════════════════════════════════
                ▲                                                       ▲
                │  1. Explore Curricular Toys                           │  1. Manage Categories
                │  2. Download Printable Spec Sheet                     │  2. Create Design Challenges
                │  3. Inspect Mechanics & Kinematics                    │  3. Review Submissions & Logs
    ┌───────────┴───────────┐                               ┌───────────┴───────────┐
    │     STEM Educator     │                               │ Platform Administrator│
    └───────────────────────┘                               └───────────────────────┘
```

---

### Level 1 DFD
The Level 1 DFD decomposes the system into six major processes and four data stores:

```
                      [Maker / Creator]
                             │
                             ▼
                    ┌───────────────────┐
                    │ 1.0 Draft Concept │ ◄── [Spark Ideation Engine]
                    │   & Specification │
                    └─────────┬─────────┘
                              │
                              ▼
                       (D1: Creations) ◄────────┐
                              │                 │
                              ├─────────────────┼───────────────────────────┐
                              ▼                 │                           ▼
                    ┌───────────────────┐       │                 ┌───────────────────┐
                    │ 2.0 PlayLab       │       │                 │ 3.0 Design        │
                    │   Simulators      │       │                 │   Challenges      │
                    └─────────┬─────────┘       │                 └─────────┬─────────┘
                              │                 │                           │
                              ▼                 │                           ▼
                    [Interactive Canvas]        │                 (D3: Challenges)
                              │                 │                           │
                              ▼                 │                           ▼
                    ┌───────────────────┐       │                 (D4: Submissions)
                    │ 4.0 Playtesting   │───────┘
                    │   & Reviews       │
                    └─────────┬─────────┘
                              │
                              ▼
                     (D2: Reviews & Logs)
```

**Processes:**
1. **1.0 Draft Concept & Specification**: Accepts maker inputs, validates parameters, and stores blueprints in `D1: Creations`.
2. **2.0 PlayLab Simulators**: Reads creation prototype parameters and launches interactive canvas simulation.
3. **3.0 Design Challenges**: Accepts administrator prompts and manages submissions via `D3: Challenges` and `D4: Submissions`.
4. **4.0 Playtesting & Reviews**: Collects tester feedback, computes rating averages, and appends to `D2: Reviews`.
5. **5.0 Spark Engine & Upvoting**: Manages session-based upvote counters and ideation combinatorics.
6. **6.0 Printable Maker Export**: Converts database models into formatted engineering sheets.

---

## 4.2 Entity Relationship Diagram (ERD)

```
  ┌───────────────────────┐            1:N            ┌───────────────────────────┐
  │       Category        │ ───────────────────────── │         Creation          │
  ├───────────────────────┤                           ├───────────────────────────┤
  │ id (PK)               │                           │ id (PK)                   │
  │ name (VARCHAR)        │                           │ category_id (FK)          │
  │ slug (SLUG)           │                           │ title (VARCHAR)           │
  │ description (TEXT)    │                           │ slug (SLUG)               │
  │ icon (VARCHAR)        │                           │ creation_type (VARCHAR)   │
  │ accent_color (VARCHAR)│                           │ tagline (VARCHAR)         │
  └───────────────────────┘                           │ novelty_factor (TEXT)     │
                                                      │ description (TEXT)        │
                                                      │ target_age_min (INT)      │
                                                      │ target_age_max (INT)      │
                                                      │ player_count_min (INT)    │
                                                      │ player_count_max (INT)    │
                                                      │ play_time_minutes (INT)   │
                                                      │ difficulty (VARCHAR)      │
                                                      │ materials_needed (TEXT)   │
                                                      │ tools_required (TEXT)     │
                                                      │ rules_or_instructions(TXT)│
                                                      │ safety_advisories (TEXT)  │
                                                      │ stem_fields (VARCHAR)     │
                                                      │ prototype_type (VARCHAR)  │
                                                      │ sparks_count (INT)        │
                                                      │ views_count (INT)         │
                                                      │ is_featured (BOOL)        │
                                                      │ created_at (DATETIME)     │
                                                      └─────────────┬─────────────┘
                                                                    │
                                         ┌──────────────────────────┴──────────────────────────┐
                                     1:N │                                                 1:N │
                                         ▼                                                     ▼
                        ┌───────────────────────────┐                         ┌───────────────────────────┐
                        │      PlaytestReview       │                         │    ChallengeSubmission    │
                        ├───────────────────────────┤                         ├───────────────────────────┤
                        │ id (PK)                   │                         │ id (PK)                   │
                        │ creation_id (FK)          │                         │ challenge_id (FK)         │
                        │ reviewer_name (VARCHAR)   │                         │ creation_id (FK)          │
                        │ rating_overall (INT)      │                         │ submitted_at (DATETIME)   │
                        │ rating_fun (INT)          │                         └─────────────▲─────────────┘
                        │ rating_originality (INT)  │                                       │
                        │ rating_durability (INT)   │                                       │ N:1
                        │ rating_stem_value (INT)   │                         ┌─────────────┴─────────────┐
                        │ comment (TEXT)            │                         │      DesignChallenge      │
                        │ maker_mod_idea (TEXT)     │                         ├───────────────────────────┤
                        │ created_at (DATETIME)     │                         │ id (PK)                   │
                        └───────────────────────────┘                         │ title (VARCHAR)           │
                                                                              │ slug (SLUG)               │
                                                                              │ theme (VARCHAR)           │
                                                                              │ description (TEXT)        │
                                                                              │ constraints (TEXT)        │
                                                                              │ reward_title (VARCHAR)    │
                                                                              │ is_active (BOOL)          │
                                                                              │ created_at (DATETIME)     │
                                                                              └───────────────────────────┘
```

---

# 5. GitHub Link & Source Repository

- **Project Name:** PlayForge Studio - Toys & Games Innovation Platform
- **Repository URL:** `https://github.com/Pintu241/PlayForge-Toys-Games` *(or local workspace repository)*
- **Version Control Status:** Clean Git repository initialized with complete commit history.

### Directory Structure of Source Code:
```
Django-project/
├── creations/                      # Core Application Package
│   ├── management/commands/
│   │   └── seed_data.py            # Automated database seeder (6 creations, categories, reviews)
│   ├── migrations/                 # Schema migrations (0001_initial, 0002_alter)
│   ├── admin.py                    # Django Admin customized registration
│   ├── apps.py                     # App configuration
│   ├── forms.py                    # CreationForm and PlaytestReviewForm
│   ├── models.py                   # Category, Creation, PlaytestReview, DesignChallenge
│   ├── tests.py                    # 11 unit test cases (models, views, AJAX, calculations)
│   ├── urls.py                     # Routing for blueprints, arcade, spark engine
│   └── views.py                    # Controller logic for platform views
├── playforge/                      # Project Configuration Package
│   ├── settings.py                 # Django settings (apps, templates, static)
│   ├── urls.py                     # Root routing configuration
│   ├── asgi.py                     # ASGI entry-point
│   └── wsgi.py                     # WSGI production entry-point
├── static/
│   └── css/style.css               # Clean executive design system & canvas frames
├── templates/
│   ├── base.html                   # Master layout with frosted navigation & footer
│   └── creations/
│       ├── home.html               # Discovery hub, live search & category pills
│       ├── detail.html             # Patent-style blueprint dossier & BOM checklist
│       ├── create.html             # The Maker's Anvil concept builder form
│       ├── playlab_hub.html        # Virtual arcade hub
│       ├── spark_generator.html    # 4-dial combinatorial ideation machine
│       ├── challenges.html         # Innovation hackathon list
│       ├── challenge_detail.html   # Challenge details & entry submission form
│       ├── print_blueprint.html    # Clean monochrome printable specification sheet
│       └── prototypes/
│           ├── marble_run.html     # CogCraft 2D physics & Web Audio synth sandbox
│           ├── chroma_tiles.html   # ChromaTiles playable optical strategy board game
│           └── kinetic_gears.html  # GearSmith kinematic automata simulator
├── db.sqlite3                      # Pre-seeded database
├── manage.py                       # CLI management script
└── README.md                       # Comprehensive setup and usage guide
```

---

# 6. Deployed Link & Execution Guide

### Local Development Server
The application runs locally on `http://127.0.0.1:8000/`.

**Steps to Execute:**
```powershell
# 1. Open Terminal in project directory
cd c:\Users\Dikshit\Downloads\Django-project

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Apply database migrations
.\venv\Scripts\python.exe manage.py migrate

# 4. Populate pre-seeded innovative toys & games
.\venv\Scripts\python.exe manage.py seed_data

# 5. Start the development server
.\venv\Scripts\python.exe manage.py runserver
```

### Key Navigation Routes:
- **Discovery Hub:** `http://127.0.0.1:8000/`
- **CogCraft Marble Physics Sandbox:** `http://127.0.0.1:8000/playlab/marble-run/`
- **ChromaTiles Board Game (vs AI / Hotseat):** `http://127.0.0.1:8000/playlab/chroma-tiles/`
- **GearSmith Automata Kinematics:** `http://127.0.0.1:8000/playlab/kinetic-gears/`
- **Spark Ideation Engine:** `http://127.0.0.1:8000/spark-engine/`
- **Maker Design Challenges:** `http://127.0.0.1:8000/challenges/`
- **Invention Forge (New Blueprint):** `http://127.0.0.1:8000/creations/new/`
- **Printable Specification Sheet:** `http://127.0.0.1:8000/creations/cogcraft-perpetual-kinetic-marble-contraption/print/`

---

# 7. System Verification & Test Suite Proof

PlayForge includes an automated unit test suite (`creations/tests.py`) validating model integrity, URL routing, AJAX spark increments, simulation view response codes, and template rendering.

### Test Execution Output:
```powershell
PS C:\Users\Dikshit\Downloads\Django-project> .\venv\Scripts\python.exe manage.py test
Creating test database for alias 'default'...
...........
----------------------------------------------------------------------
Ran 11 tests in 0.149s

OK
Destroying test database for alias 'default'...
Found 11 test(s).
System check identified no issues (0 silenced).
```

### Verified Test Cases:
1. `test_category_slug_auto_generation`: Verifies automatic generation of URL slugs from category names.
2. `test_creation_slug_auto_generation`: Verifies collision-free slugification of creation titles.
3. `test_creation_materials_list`: Confirms parsing of multi-line materials strings into individual array items.
4. `test_playtest_review_and_average_rating`: Validates floating-point calculation of community review scores.
5. `test_home_page_status_and_content`: Checks HTTP 200 response and discovery template rendering.
6. `test_creation_detail_page`: Verifies full blueprint dossier view and BOM rendering.
7. `test_spark_ajax_toggle`: Verifies session-based upvote toggling via JSON API.
8. `test_playlab_hub_and_simulators`: Verifies status code 200 across Hub and all 3 simulation arcade engines.
9. `test_spark_generator_page`: Tests the combinatorial ideation engine template and context.
10. `test_challenges_list_and_detail`: Verifies challenge briefings and submission forms.
11. `test_print_blueprint`: Tests printable engineering specification sheet generation.

---

# A. Appendices

### A.1 Appendix 1: Demo Accounts & Roles
For local evaluation and demonstration, the following roles and credentials can be utilized:

| Role | Username | Password | Purpose |
| :--- | :--- | :--- | :--- |
| **Platform Administrator** | `admin` | `admin123` *(create via `createsuperuser`)* | Access Django Admin at `/admin/` |
| **Maker / Inventor** | Guest / Inventor | None Required | Public access to create blueprints & participate in challenges |
| **Playtester / Gamer** | Community Tester | None Required | Submit playtest feedback, test simulators, and spark creations |

### A.2 Appendix 2: Project Modules & App Architecture

| Module / File | Responsibility |
| :--- | :--- |
| `creations/models.py` | Data schemas for Categories, Creations, Reviews, and Challenges |
| `creations/views.py` | Controller endpoints for browsing, simulators, ideation, and exports |
| `creations/forms.py` | Django ModelForms with validation for blueprints and reviews |
| `creations/urls.py` | Application route mappings with named namespaces |
| `creations/admin.py` | Customized administrative model registrations with list filters |
| `static/css/style.css` | Design system: dark-mode palette, typography, arcade frames |
| `templates/creations/prototypes/` | Standalone HTML5 canvas physics, ray tracing, and linkage prototypes |

### A.3 Appendix 3: Seeded Unique Toy & Game Inventions

1. **CogCraft: Perpetual Kinetic Marble Contraption**
   - *Classification:* Kinetic & Mechanical Toy
   - *Novelty Factor:* Operates via clockwork escapement physics where descending steel marbles themselves trip the escapement pallets, pacing the toy without batteries.
   - *Interactive Prototype:* 2D Canvas Physics Sandbox with Web Audio chime synthesis.
2. **ChromaTiles: The Prismatic Tactical Light Game**
   - *Classification:* Strategy Board Game
   - *Novelty Factor:* Combines optical refraction and additive color synthesis with spatial territory control; rotating a prism alters light paths across the entire board.
   - *Interactive Prototype:* 8x8 Playable Grid with optical ray tracing vs Bot AI.
3. **GearSmith: Kinematic Automaton Workshop**
   - *Classification:* Mechanical Construction Toy
   - *Novelty Factor:* Modular ball-and-socket links and eccentric cams converting rotary crank inputs into organic non-linear biomimetic flapping motion.
   - *Interactive Prototype:* Interactive Kinematic Gear Train Simulator.
4. **AeroGlyph: Resonant Acoustic Levitation Maze**
   - *Classification:* STEM & Physics Contraption
   - *Novelty Factor:* Suspends an iridescent micro-orb using ultrasonic acoustic radiation pressure, steered via vocal pitch and tuned pitch whistles.
5. **TerraFold: The Origami Topography Quest**
   - *Classification:* Strategy Board Game
   - *Novelty Factor:* The board is a continuous Miura-ori folding metamaterial surface that physically snaps and inverts under player movement.
6. **ChronoSense: Magnetic Ferrofluid Gravity Hourglass**
   - *Classification:* Sensory & Tactile Novelty
   - *Novelty Factor:* Immiscible ferrofluid suspension in optical oil manipulated using external dual magnetic wands to guide droplets through micro-capillaries.

---

**End of Software Requirements Specification Document**

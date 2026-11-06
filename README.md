# 🎲 PlayForge Studio: Creative Toys & Games Innovation Platform

**PlayForge** is a full-featured Django web application designed for the challenge:
> *"Toys & Games - Challenges your creative minds to conceptualize and develop unique toys & games."*

PlayForge empowers makers, educators, and game designers to **conceptualize, prototype, playtest, and manufacture** never-before-seen physical toys and tabletop games.

---

## 🌟 Key Features

### 1. 📐 Invention Blueprints & Maker Dossiers
- Detailed specifications for original toys and tabletop games.
- **Novelty Factor**: Highlights what makes each creation fundamentally unique (e.g. clockwork escapements, magnetic fluidics, optical prisms, resonant sound waves).
- **Bill of Materials & Tools Checklist**: Interactive maker parts list.
- **STEM Disciplines**: Educational mapping to physics, mechanics, optics, topology, and kinematics.
- **Safety Advisories**: Age suitability, magnetic/choking hazard warnings.
- **Printable Blueprint Spec**: Clean, high-contrast engineering sheet formatted for workshops and 3D printing labs (`/creations/<slug>/print/`).

### 2. 🕹️ The PlayLab Arcade (Interactive In-Browser Prototypers)
Test toy physics and board game mechanics directly in the browser:
- **CogCraft Kinetic Sandbox (`/playlab/marble-run/`)**:
  - Interactive 2D physics sandbox. Draw gravity ramps, place bouncing pegs, resonant acoustic sound chimes (powered by Web Audio API synths), acceleration boosters, and warp portals. Drop steel balls or toggle the auto-dispenser!
- **ChromaTiles Tactical Light Grid (`/playlab/chroma-tiles/`)**:
  - Playable 8x8 optical ray tracing board game! Place and rotate angled prism mirrors to reflect laser beams, powering sensor crystals. Playable in **Hotseat (2-Player)** or **vs Bot AI**.
- **GearSmith Kinematic Automaton Lab (`/playlab/kinetic-gears/`)**:
  - Interactive mechanical gear train and four-bar linkage simulator. Adjust RPM, drive ratios, and watch articulated biomimetic puppet wings/fins move with authentic harmonic motion.

### 3. ⚡ The Spark Engine (Combinatorial Ideation Machine)
- Solves creator's block by spinning 4 independent dials:
  `[Target Audience]` + `[Physical Mechanism]` + `[Unconventional Material]` + `[Thematic World]`
- Generates titles, pitches, and novelty statements with one click.
- **"Send to Forge"**: Directly transfers the generated concept into the creation form!

### 4. 🏆 Maker Design Challenges & Hackathons
- Structured design contests with strict constraints (e.g., *The Zero-Gravity Play Challenge*, *The One-Sheet Material Wonder*).
- Submit invention blueprints to active challenges and track submissions.

### 5. 🔬 Community Playtesting & Maker Hacks
- Record playtest sessions with multi-axis ratings (Fun Factor, Innovation, Durability, STEM Value).
- Suggest DIY hacks, modifications, and expansions.
- Live AJAX "Spark" upvoting.

---

## 🚀 Quickstart Guide

### 1. Virtual Environment & Dependencies
The project uses Python and Django 6:
```powershell
# Activate the virtual environment
.\venv\Scripts\Activate.ps1
```

### 2. Database Migrations & Seed Data
Migrations and rich seed data are already configured:
```powershell
# Apply database migrations
.\venv\Scripts\python.exe manage.py migrate

# Seed sample innovative toys and games
.\venv\Scripts\python.exe manage.py seed_data
```

### 3. Run the Development Server
```powershell
.\venv\Scripts\python.exe manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

### 4. Run Unit Tests
```powershell
.\venv\Scripts\python.exe manage.py test
```
All 11 unit tests covering models, views, simulators, and AJAX endpoints pass with 0 errors.

---

## 📁 Project Structure

```
Django-project/
├── creations/                      # Core Toys & Games Application
│   ├── management/commands/
│   │   └── seed_data.py            # Rich database seeder with 6 innovative creations
│   ├── migrations/                 # Database migrations
│   ├── models.py                   # Category, Creation, PlaytestReview, DesignChallenge
│   ├── forms.py                    # CreationForm, PlaytestReviewForm
│   ├── views.py                    # Discovery, Blueprints, PlayLab, Spark Engine, Challenges
│   ├── urls.py                     # App URL routing
│   ├── tests.py                    # 11 unit tests
│   └── admin.py                    # Django Admin registration
├── playforge/                      # Project Configuration
│   ├── settings.py                 # Installed apps, templates, static files
│   ├── urls.py                     # Root routing
│   └── wsgi.py
├── static/
│   ├── css/style.css               # Blueprint grids, neon blooms, arcade styling
│   └── js/
├── templates/
│   ├── base.html                   # Global navigation, hero ticker, and footer
│   └── creations/
│       ├── home.html               # Discovery hub, search, category pills & grid
│       ├── detail.html             # Blueprint dossier, bill of materials, playtest reviews
│       ├── create.html             # The Maker's Forge (concept submission form)
│       ├── playlab_hub.html        # Interactive arcade overview
│       ├── spark_generator.html    # 4-dial combinatorial idea machine
│       ├── challenges.html         # Innovation hackathon briefs
│       ├── challenge_detail.html   # Challenge details & submission entry
│       ├── print_blueprint.html    # Printable engineering sheet view
│       └── prototypes/
│           ├── marble_run.html     # CogCraft 2D physics & Web Audio synth sandbox
│           ├── chroma_tiles.html   # ChromaTiles playable board game vs AI/Hotseat
│           └── kinetic_gears.html  # GearSmith kinematic automata simulator
└── manage.py
```

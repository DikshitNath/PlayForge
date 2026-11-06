from django.core.management.base import BaseCommand
from creations.models import Category, Creation, PlaytestReview, DesignChallenge, ChallengeSubmission

class Command(BaseCommand):
    help = 'Seeds initial toys, games, challenges, and categories'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding categories...")
        cat_kinetic, _ = Category.objects.get_or_create(
            name="Kinetic & Mechanical Toys",
            defaults={
                'description': 'Physical toys driven by gears, springs, escapements, pendulums, and kinetic chain reactions.',
                'icon': 'cog',
                'accent_color': '#f59e0b'
            }
        )
        cat_stem, _ = Category.objects.get_or_create(
            name="STEM & Physics Contraptions",
            defaults={
                'description': 'Hands-on inventions illustrating electromagnetism, acoustic resonance, fluidics, and optics.',
                'icon': 'atom',
                'accent_color': '#06b6d4'
            }
        )
        cat_board, _ = Category.objects.get_or_create(
            name="Novel Strategy Board Games",
            defaults={
                'description': 'Tactile, non-traditional tabletop games featuring shifting boards, light mechanics, or asymmetric rules.',
                'icon': 'dice-d20',
                'accent_color': '#8b5cf6'
            }
        )
        cat_sensory, _ = Category.objects.get_or_create(
            name="Sensory & Tactile Novelties",
            defaults={
                'description': 'Ergonomic, meditative, and sensory toys utilizing microfluidics, bistable flexures, and magnetic fields.',
                'icon': 'fingerprint',
                'accent_color': '#ec4899'
            }
        )
        cat_hybrid, _ = Category.objects.get_or_create(
            name="Digital-Physical Hybrids",
            defaults={
                'description': 'Games blending tangible physical components with sensors, acoustic feedback, and digital play spaces.',
                'icon': 'gamepad',
                'accent_color': '#10b981'
            }
        )

        self.stdout.write("Seeding creations...")

        c1, created = Creation.objects.get_or_create(
            title="CogCraft: Perpetual Kinetic Marble Contraption",
            defaults={
                'creation_type': 'TOY',
                'category': cat_kinetic,
                'creator_name': 'Prof. Leonardo Gearhart',
                'tagline': 'A gravity-and-escapement marble coaster where players engineer custom kinetic tracks.',
                'description': (
                    "CogCraft is a modular desktop kinetic toy that merges mechanical clock escapements with a dynamic marble track system. "
                    "A counterweighted pendulum slowly meters the descent of 12mm stainless steel balls, while an ingenious ratcheted helical Archimedes screw "
                    "lifts them back up using energy stored in a tensioned rubber-spring reel. "
                    "Players snap in customizable diversion switches, harmonic chime bells, loop-de-loops, and magnetic acceleration gates to compose physical, acoustic rhythm loops."
                ),
                'novelty_factor': (
                    "Unlike standard toy marble runs made of static plastic clips, CogCraft operates on clockwork escapement physics. "
                    "The balls themselves trigger escapement pallets, turning each dropped ball into a synchronized mechanical pulse that paces the entire toy without batteries or electricity."
                ),
                'target_age_min': 8,
                'target_age_max': 99,
                'player_count_min': 1,
                'player_count_max': 3,
                'play_time_minutes': 45,
                'difficulty': 'MEDIUM',
                'materials_needed': (
                    "- 3mm Baltic Birch Plywood sheets (or 3D printed PLA/PETG)\n"
                    "- 8x 608-ZZ Miniature Ball Bearings\n"
                    "- 12x 12mm Stainless Steel Ball Bearings\n"
                    "- 6x 10x2mm N52 Neodymium Ring Magnets\n"
                    "- 2x Heavy-duty silicone tension bands\n"
                    "- 4x Brass chime rods tuned to Pentatonic Scale"
                ),
                'tools_required': "Laser cutter or 3D printer, PVA wood glue, 2mm hex wrench, small needle-nose pliers",
                'rules_or_instructions': (
                    "1. Construct the escapement anchor tower using interlocking snap joints and secure bearings.\n"
                    "2. Calibrate pendulum counterweight to achieve a rhythmic 60 BPM cycle.\n"
                    "3. Connect modular track rails using magnetic coupling joints.\n"
                    "4. Release lead marble into primary hopper.\n"
                    "5. Challenge: Configure the track splitters so 4 marbles loop continuously without colliding for at least 120 seconds."
                ),
                'safety_advisories': "Contains small steel balls and strong magnets. Keep away from small children and medical implants.",
                'stem_fields': "Classical Mechanics, Escapement Physics, Harmonic Resonance, Gear Ratios",
                'prototype_type': 'MARBLE_RUN',
                'banner_color': 'from-amber-500 to-rose-600',
                'badge_tag': 'Playable Prototype Available',
                'sparks_count': 148,
                'views_count': 1240,
                'is_featured': True,
            }
        )

        c2, created = Creation.objects.get_or_create(
            title="ChromaTiles: The Prismatic Tactical Light Game",
            defaults={
                'creation_type': 'GAME',
                'category': cat_board,
                'creator_name': 'Lumina Design Collective',
                'tagline': 'Reflect, split, and refract beams of colored light across a shifting modular grid to claim energy nodes.',
                'description': (
                    "ChromaTiles is a tactical abstract strategy board game played on a luminous grid. "
                    "Each turn, players don't move chess-like tokens; instead, they position optical prism tiles, beam splitters, and polarized mirrors. "
                    "When light beams travel through the board, they refract, bend 90 degrees, or split into constituent spectrum colors (red + blue = violet). "
                    "Score points by directing targeted color wavelengths into your designated sensor pylons while blocking or deflecting your opponent's beams."
                ),
                'novelty_factor': (
                    "Combines real physical optics (refraction, additive color synthesis, polarized barriers) with spatial territorial conquest. "
                    "A single rotation of a prism tile can instantly alter the light paths across the entire board, triggering chain-reaction illumination flips."
                ),
                'target_age_min': 10,
                'target_age_max': 99,
                'player_count_min': 2,
                'player_count_max': 4,
                'play_time_minutes': 30,
                'difficulty': 'ADVANCED',
                'materials_needed': (
                    "- 1x 8x8 Matte Frosted Acrylic Game Board with recessed LED edge emitters\n"
                    "- 16x Double-sided Mirrored Acrylic Tiles (45° angled reflectors)\n"
                    "- 8x Triangular Dichroic Prisms (beam splitters)\n"
                    "- 4x Color Filter Gates (Cyan, Magenta, Yellow)\n"
                    "- 8x Scoring Node Pylons with light-pipe fiber optics"
                ),
                'tools_required': "Craft knife, scoring tool, 5V USB battery pack for board backlight",
                'rules_or_instructions': (
                    "Setup: Place board on flat table. Activate emitter diodes at four corners.\n"
                    "Turn Actions (Choose 2):\n"
                    "A. Place a prism or mirror tile onto an empty coordinate.\n"
                    "B. Rotate any existing friendly tile 90 or 45 degrees.\n"
                    "C. Shift an entire row or column one unit along outer rails.\n"
                    "Scoring: Maintain an uninterrupted light beam hitting target node for 1 full player round to gain 3 Solar Sparks. First to 15 Sparks wins."
                ),
                'safety_advisories': "Uses low-intensity Class 1 LED emitters. Safe for eyes, but avoid prolonged direct staring into high-intensity emitters.",
                'stem_fields': "Optics & Ray Tracing, Additive Color Theory, Graph Theory, Combinatorics",
                'prototype_type': 'CHROMA_TILES',
                'banner_color': 'from-indigo-600 to-purple-600',
                'badge_tag': 'Playable vs AI / Hotseat',
                'sparks_count': 234,
                'views_count': 1890,
                'is_featured': True,
            }
        )

        c3, created = Creation.objects.get_or_create(
            title="GearSmith: Kinematic Automaton Workshop",
            defaults={
                'creation_type': 'TOY',
                'category': cat_kinetic,
                'creator_name': 'Mechanica Lab',
                'tagline': 'Snap-together linkage kits that translate rotary motion into lifelike biomimetic movement.',
                'description': (
                    "GearSmith is a modular mechanical construction toy that teaches kids and makers how to design automatons. "
                    "Using patent-pending quick-click ball-and-socket links, eccentric cams, and compound gear trains, inventors can transform "
                    "a simple hand-crank turn into the undulating wave of a swimming ray, the predatory stride of a mechanical tiger, or the flapping wings of a mechanical bird."
                ),
                'novelty_factor': (
                    "Standard building toys only snap at rigid 90-degree angles. GearSmith features multi-axis rotational pivots and parametric eccentric cams, "
                    "allowing users to synthesize true organic harmonic motion and four-bar planar linkages with zero math required."
                ),
                'target_age_min': 7,
                'target_age_max': 99,
                'player_count_min': 1,
                'player_count_max': 2,
                'play_time_minutes': 40,
                'difficulty': 'MEDIUM',
                'materials_needed': (
                    "- 32x Snap-fit Spur Gears (20T, 40T, 60T)\n"
                    "- 16x Elliptical and Snail Cams\n"
                    "- 24x Variable-length Four-Bar Linkage arms\n"
                    "- 1x Heavy wooden pegboard chassis\n"
                    "- 4x Interchangeable laser-etched wooden puppet silhouettes"
                ),
                'tools_required': "None (all components snap together friction-fit)",
                'rules_or_instructions': (
                    "1. Mount drive crank axle into the center chassis port.\n"
                    "2. Mesh follower gears to adjust reduction ratios (e.g. 3:1 for slow majestic movement).\n"
                    "3. Connect eccentric pushrods to puppet rocker arms.\n"
                    "4. Turn crank clockwise and observe how continuous rotary speed translates into non-linear sinusoidal motion."
                ),
                'safety_advisories': "Pinch hazard around high-ratio gear mesh. Supervise children under 6.",
                'stem_fields': "Kinematics, Linkage Synthesis, Biomechanical Motion, Mechanical Advantage",
                'prototype_type': 'KINETIC_GEARS',
                'banner_color': 'from-cyan-500 to-blue-600',
                'badge_tag': 'Interactive Kinematics Sim',
                'sparks_count': 189,
                'views_count': 1420,
                'is_featured': True,
            }
        )

        c4, created = Creation.objects.get_or_create(
            title="AeroGlyph: Resonant Acoustic Levitation Maze",
            defaults={
                'creation_type': 'HYBRID',
                'category': cat_stem,
                'creator_name': 'VibeTech SoundWorks',
                'tagline': 'Guide a weightless floating particle through a 3D labyrinth using musical tones and harmonic frequencies.',
                'description': (
                    "AeroGlyph harnesses acoustic radiation pressure and standing sound waves to suspend an ultra-light iridescent micro-orb in mid-air. "
                    "The cylindrical puzzle contains tuned Helmholtz acoustic cavities. Players use pitch whistles, vocal humming, or slide flutes "
                    "to shift the standing wave node locations, levitating the bead up, down, and across obstacles without touching it."
                ),
                'novelty_factor': (
                    "First consumer DIY puzzle toy that translates vocal pitch and acoustic wave physics into direct physical object manipulation without tactile contact or magnetic fields."
                ),
                'target_age_min': 9,
                'target_age_max': 99,
                'player_count_min': 1,
                'player_count_max': 4,
                'play_time_minutes': 25,
                'difficulty': 'ADVANCED',
                'materials_needed': (
                    "- Transparent Acrylic Tube (70mm diameter x 300mm length)\n"
                    "- 4x Micro Ultrasonic Transducer arrays (40kHz)\n"
                    "- Mini 9V driver circuit with frequency modulation knob\n"
                    "- 6x Expanded polystyrene micro-spheres (coated in UV glow powder)\n"
                    "- 2x Tuned wooden pitch pipes"
                ),
                'tools_required': "Soldering iron (or quick-connect spring clips), hot glue",
                'rules_or_instructions': (
                    "1. Turn on the standing wave acoustic matrix.\n"
                    "2. Release orb into the acoustic levitation well; it will float steadily at the node point.\n"
                    "3. Play notes on the pitch pipe to displace the wave nodes through the labyrinth gates.\n"
                    "4. Complete the 5-tier altitude challenge without dropping the orb out of acoustic trap."
                ),
                'safety_advisories': "Ultrasonic waves are above human hearing range, but keep away from household pets sensitive to high frequencies.",
                'stem_fields': "Acoustic Levitation, Standing Waves, Wave Interference, Resonance",
                'prototype_type': 'NONE',
                'banner_color': 'from-emerald-500 to-teal-700',
                'badge_tag': 'Acoustic Physics Wonder',
                'sparks_count': 97,
                'views_count': 850,
                'is_featured': True,
            }
        )

        c5, created = Creation.objects.get_or_create(
            title="TerraFold: The Origami Topography Quest",
            defaults={
                'creation_type': 'GAME',
                'category': cat_board,
                'creator_name': 'Origami Tacticians Guild',
                'tagline': 'A living origami board game that physically folds, expands, and inverts under player movement.',
                'description': (
                    "In TerraFold, the board itself is an active tactical participant. "
                    "Constructed from a continuous tessellated Miura-ori fold pattern, the terrain shifts when players exert geometric pressure. "
                    "Stepping on an alpine vertex can trigger a bistable snap, causing a canyon to flatten into a plain and opening hidden subterranean paths for ally explorers."
                ),
                'novelty_factor': (
                    "Transforms board games from 2D static flat planes into 3D mechanically responsive kinetic metamaterial surfaces."
                ),
                'target_age_min': 10,
                'target_age_max': 99,
                'player_count_min': 2,
                'player_count_max': 4,
                'play_time_minutes': 40,
                'difficulty': 'MEDIUM',
                'materials_needed': (
                    "- 1x Pre-creased Heavyweight Tyvek Waterproof Folding Sheet\n"
                    "- 16x Magnetic Wood Explorer Totems\n"
                    "- 24x Terrain Activation Token Discs\n"
                    "- 4x Aluminum Tension Clamps"
                ),
                'tools_required': "Bone folder or scoring tool for initial crease preparation",
                'rules_or_instructions': (
                    "Each turn, place an explorer token and apply vertical pressure.\n"
                    "When three tokens converge on a fold intersection, invert that origami petal.\n"
                    "Control the 3 Apex Peaks to establish your realm and declare victory."
                ),
                'safety_advisories': "No hazardous materials; keep paper dry to ensure crisp mechanical folds.",
                'stem_fields': "Origami Mathematics, Metamaterials, Topology, Kinematic Metamaterials",
                'prototype_type': 'NONE',
                'banner_color': 'from-fuchsia-600 to-pink-600',
                'badge_tag': 'Shape-Shifting Board',
                'sparks_count': 112,
                'views_count': 990,
                'is_featured': False,
            }
        )

        c6, created = Creation.objects.get_or_create(
            title="ChronoSense: Magnetic Ferrofluid Gravity Hourglass",
            defaults={
                'creation_type': 'TOY',
                'category': cat_sensory,
                'creator_name': 'Flux Studio',
                'tagline': 'Sculpt dynamic magnetic liquid sculptures through a microfluidic obstacle maze.',
                'description': (
                    "ChronoSense is a tactile desk sculpture and sensory puzzle toy encased in optical acrylic. "
                    "Inside sits an immiscible suspension of jet-black magnetic ferrofluid in crystal-clear silicone solution. "
                    "Using dual precision neodymium magnetic wands, users drag spiked organic ferrofluid blobs through capillary chambers, "
                    "splitting droplets across hydrodynamic diverters, and bridging liquid contact switches to measure time intervals."
                ),
                'novelty_factor': (
                    "Bridges tactile fidget exploration with fluid mechanics and magnetic field visualization, offering mesmerizing organic visual feedback that feels alien and alive."
                ),
                'target_age_min': 8,
                'target_age_max': 99,
                'player_count_min': 1,
                'player_count_max': 1,
                'play_time_minutes': 15,
                'difficulty': 'EASY',
                'materials_needed': (
                    "- 1x Sealed Acrylic Double-Chamber Vessel (50ml capacity)\n"
                    "- 10ml Water-based Ferrofluid (EFH-1 or similar)\n"
                    "- 40ml Low-viscosity Mineral/Silicone Carrier Oil\n"
                    "- 2x Ergonomic Brass Stylus Pens with N52 Neodymium tips"
                ),
                'tools_required': "Syringe with blunt needle for fluid injection, UV cure sealant",
                'rules_or_instructions': (
                    "1. Invert the hourglass to initiate gravitational droplet cascade.\n"
                    "2. Use magnetic stylus against exterior surface to catch and hold ferrofluid droplets.\n"
                    "3. Guide liquid through narrow 2mm constriction baffles without splitting the droplet into secondary satellites.\n"
                    "4. Dock droplet into target capillary nest before the clear fluid settles."
                ),
                'safety_advisories': "Permanent magnetic wands. Do not open or consume fluid. Keep away from pacemakers.",
                'stem_fields': "Magnetohydrodynamics, Surface Tension, Fluid Viscosity, Magnetic Flux",
                'prototype_type': 'NONE',
                'banner_color': 'from-violet-600 to-indigo-900',
                'badge_tag': 'Sensory & Physics Fidget',
                'sparks_count': 175,
                'views_count': 1310,
                'is_featured': False,
            }
        )

        self.stdout.write("Seeding sample playtest reviews...")
        PlaytestReview.objects.get_or_create(
            creation=c1,
            reviewer_name="Elena Rostova (STEM Educator)",
            defaults={
                'rating_overall': 5,
                'rating_fun': 5,
                'rating_originality': 5,
                'rating_durability': 4,
                'rating_stem_value': 5,
                'comment': (
                    "Tested this with my 8th grade science class during our energy conservation unit! "
                    "The kids were mesmerized by the clockwork escapement mechanism. It clearly illustrates potential vs kinetic energy conversion. "
                    "The modular track connectors snapped cleanly into place."
                ),
                'maker_mod_idea': "We 3D-printed a miniature spiral funnel at the top of the lift which added a wonderful vortex spinning sound!"
            }
        )

        PlaytestReview.objects.get_or_create(
            creation=c2,
            reviewer_name="Marcus Vance (BoardGameGeek Reviewer)",
            defaults={
                'rating_overall': 5,
                'rating_fun': 5,
                'rating_originality': 5,
                'rating_durability': 5,
                'rating_stem_value': 4,
                'comment': (
                    "ChromaTiles completely blew our game night away. The tactical depth is on par with Chess or Hive, "
                    "yet the tactile beauty of rotating acrylic prisms and watching actual light beams refract across the table is breathtaking. "
                    "The interactive browser simulator is fantastic for testing moves in advance!"
                ),
                'maker_mod_idea': "Try playing with the room lights dimmed for maximum visual drama!"
            }
        )

        self.stdout.write("Seeding design challenges...")
        ch1, _ = DesignChallenge.objects.get_or_create(
            title="The Zero-Gravity Play Challenge",
            defaults={
                'theme': 'Toys and Games Built For Astronauts & Microgravity',
                'description': (
                    "Imagine entertaining an astronaut crew on a 3-year mission to Mars. "
                    "Traditional toys that rely on downward gravity or loose parts fail in space. "
                    "Design a toy or game that utilizes surface tension, magnetic anchor grids, air current currents, or gyroscopic inertia to create engaging play in zero-g!"
                ),
                'constraints': "Must not contain loose un-tethered small parts (<5mm); cannot rely on gravity; must be compact and weigh under 500g.",
                'reward_title': 'Orbital Inventor Gold Seal',
                'is_active': True,
            }
        )

        ch2, _ = DesignChallenge.objects.get_or_create(
            title="The One-Sheet Material Wonder",
            defaults={
                'theme': 'Extreme Minimalist Toymaking',
                'description': (
                    "Conceptualize and build a fully functioning kinetic toy or competitive tabletop game crafted from exactly ONE single sheet of material "
                    "(e.g. 1 sheet of cardboard, 1 sheet of plywood, or 1 sheet of recycled polypropylene). "
                    "No external screws, no glue—only folds, friction tabs, and geometric ingenuity."
                ),
                'constraints': "Strict limit of single sheet (max 400x400mm); zero adhesives or hardware; must have at least one moving mechanical action.",
                'reward_title': 'Geometric Origami Master Badge',
                'is_active': True,
            }
        )

        ChallengeSubmission.objects.get_or_create(challenge=ch1, creation=c4)
        ChallengeSubmission.objects.get_or_create(challenge=ch2, creation=c5)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully with imaginative toys and games!"))


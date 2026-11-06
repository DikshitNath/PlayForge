from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Creation, PlaytestReview, DesignChallenge, ChallengeSubmission

class PlayForgeModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Mechanical Puzzles",
            description="Intricate kinetic puzzles and locks.",
            icon="key",
            accent_color="#ec4899"
        )
        self.creation = Creation.objects.create(
            title="AeroGrip Gyroscope",
            category=self.category,
            tagline="A hand-held dual rotor kinetic toy.",
            description="Spinning brass flywheels generate angular momentum.",
            novelty_factor="Uses dual counter-rotating micro-flywheels.",
            target_age_min=8,
            target_age_max=99,
            player_count_min=1,
            player_count_max=1,
            play_time_minutes=15,
            difficulty='EASY',
            materials_needed="2x Brass flywheels\n1x Precision shaft",
            rules_or_instructions="Pull the rip-cord to accelerate rotors.",
            prototype_type='MARBLE_RUN',
            sparks_count=10
        )

    def test_category_slug_auto_generation(self):
        self.assertEqual(self.category.slug, "mechanical-puzzles")

    def test_creation_slug_auto_generation(self):
        self.assertEqual(self.creation.slug, "aerogrip-gyroscope")

    def test_creation_materials_list(self):
        mat_list = self.creation.materials_list()
        self.assertEqual(len(mat_list), 2)
        self.assertIn("2x Brass flywheels", mat_list)

    def test_playtest_review_and_average_rating(self):
        PlaytestReview.objects.create(
            creation=self.creation,
            reviewer_name="Maker 1",
            rating_overall=4,
            comment="Awesome toy!"
        )
        PlaytestReview.objects.create(
            creation=self.creation,
            reviewer_name="Maker 2",
            rating_overall=5,
            comment="Incredible balance!"
        )
        self.assertEqual(self.creation.average_rating(), 4.5)


class PlayForgeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name="Optics & Light Games",
            description="Light beam puzzles"
        )
        self.creation = Creation.objects.create(
            title="Prism Tactics",
            category=self.category,
            tagline="Light reflection game",
            description="Reflect lasers across tiles",
            novelty_factor="Dichroic optical prisms",
            materials_needed="Laser diodes\nPrisms",
            rules_or_instructions="Place mirrors to reflect laser",
            prototype_type='CHROMA_TILES',
            is_featured=True
        )
        self.challenge = DesignChallenge.objects.create(
            title="Zero-G Toys",
            theme="Space Play",
            description="Toys that don't need gravity",
            constraints="No loose particles"
        )

    def test_home_page_status_and_content(self):
        response = self.client.get(reverse('creations:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Prism Tactics")
        self.assertContains(response, "PlayForge")

    def test_creation_detail_page(self):
        response = self.client.get(reverse('creations:detail', kwargs={'slug': self.creation.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dichroic optical prisms")
        self.assertContains(response, "Bill of Materials")

    def test_spark_ajax_toggle(self):
        response = self.client.get(
            reverse('creations:spark', kwargs={'slug': self.creation.slug}) + '?format=json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['sparked'])
        self.assertEqual(data['sparks_count'], 1)

    def test_playlab_hub_and_simulators(self):
        res_hub = self.client.get(reverse('creations:playlab_hub'))
        self.assertEqual(res_hub.status_code, 200)

        res_marble = self.client.get(reverse('creations:playlab_simulator', kwargs={'prototype_type': 'marble-run'}))
        self.assertEqual(res_marble.status_code, 200)
        self.assertContains(res_marble, "CogCraft")

        res_chroma = self.client.get(reverse('creations:playlab_simulator', kwargs={'prototype_type': 'chroma-tiles'}))
        self.assertEqual(res_chroma.status_code, 200)
        self.assertContains(res_chroma, "ChromaTiles")

        res_gears = self.client.get(reverse('creations:playlab_simulator', kwargs={'prototype_type': 'kinetic-gears'}))
        self.assertEqual(res_gears.status_code, 200)
        self.assertContains(res_gears, "GearSmith")

    def test_spark_generator_page(self):
        response = self.client.get(reverse('creations:spark_generator'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Spark Engine")

    def test_challenges_list_and_detail(self):
        response = self.client.get(reverse('creations:challenges_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Zero-G Toys")

        res_detail = self.client.get(reverse('creations:challenge_detail', kwargs={'slug': self.challenge.slug}))
        self.assertEqual(res_detail.status_code, 200)
        self.assertContains(res_detail, "Strict Constraints")

    def test_print_blueprint(self):
        response = self.client.get(reverse('creations:print_blueprint', kwargs={'slug': self.creation.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maker Fabrication Blueprint Spec")

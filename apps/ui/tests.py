from django.test import TestCase


class UIViewTestCase(TestCase):

    def setUp(self):
        self.ghetto_fixtures()

    def tearDown(self):

        for p in self.__photos:
            p.delete()

    def ghetto_fixtures(self):

        from os.path import abspath, dirname, join
        from django.contrib.auth.models import User
        from django.core.files import File
        from photos.models import Photo, PhotoSet

        fixtures_dir = join(abspath(dirname(__file__)), "fixtures")

        self.admin = User.objects.create_user('admin', 'admin@example.com', 's3cure!1')
        self.set = PhotoSet.objects.create(name="default")

        self.__photos = []

        for i in range(1, 5):

            name = "photo_{0}.jpg".format(i)

            with open(join(fixtures_dir, name)) as f:

                p = Photo(
                    title="Photo {0}".format(i),
                    photo_set=self.set)
                p.image.save(name, File(f))

                self.__photos.append(p)
                p.save()

                setattr(self, "photo_%d" % i, p)

    def test_render_home(self):

        from django.core.urlresolvers import reverse
        from photos.models import Photo

        self.assertEqual(Photo.objects.count(), 4)

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_render_photo_set(self):

        from django.core.urlresolvers import reverse
        from photos.models import PhotoSet

        ps = PhotoSet.objects.get(slug="default")
        response = self.client.get(reverse("photo_set", args=(ps.slug, )))

        self.assertEqual(response.status_code, 200)

    def test_render_photo_detai(self):

        from django.core.urlresolvers import reverse
        from photos.models import Photo

        p = Photo.objects.get(slug="photo-1")
        response = self.client.get(reverse("photo_detail", args=(p.photo_set.slug, p.slug, )))

        self.assertEqual(response.status_code, 200)

from django.test import TestCase


class UIViewTestCases(TestCase):

    def setUp(self):
        self.ghetto_fixtures()

    def ghetto_fixtures(self):

        from os.path import abspath, dirname, join

        from django.contrib.auth.models import User
        from photos.models import Photo, PhotoSet

        fixtures_dir = join(abspath(dirname(__file__)), "fixtures")

        self.admin = User.objects.create_user('admin', 'admin@example.com', 's3cure!1')
        self.set = PhotoSet.objects.create(name="default")

        for i in range(1, 5):

            with open(join(fixtures_dir), "photo_{0}.jpg".format(i)) as f:

                p = Photo.objects.create(
                    title="Photo {0}".format(i),
                    image=f,
                    photo_set=self.set)

                setattr(self, "photo_%d" % i, p)

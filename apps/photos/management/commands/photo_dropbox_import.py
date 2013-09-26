from cStringIO import StringIO

from django.core.management.base import BaseCommand
from django.core.files import File
from optparse import make_option

from django.conf import settings
from dropbox.client import DropboxOAuth2FlowNoRedirect, DropboxClient
from easy_thumbnails.files import generate_all_aliases

from photos.models import Photo, PhotoSet


def login():

    app_key = settings.DROPBOX_APP_KEY
    app_secret = settings.DROPBOX_APP_SECRET

    flow = DropboxOAuth2FlowNoRedirect(app_key, app_secret)

    authorize_url = flow.start()

    authorize_url = flow.start()
    print '1. Go to: ' + authorize_url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'
    code = raw_input("Enter the authorization code here: ").strip()
    access_token, user_id = flow.finish(code)

    return DropboxClient(access_token)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--directory', help='Which directory in your Dropbox folder to import.'),
        make_option('--set-name', help='Which set to put the pictures in.'),
    )

    def handle(self, *args, **options):

        client = login()

        directory_name = options['directory']
        set_name = options.get('set_name', directory_name)

        files = client.metadata(directory_name)

        ps, _ = PhotoSet.objects.get_or_create(name=set_name)

        for image_dict in files['contents']:
            name = image_dict['path'].rsplit("/", 1)[-1]
            print name
            f, metadata = client.get_file_and_metadata(image_dict['path'])
            sf = StringIO()
            sf.write(f.read())
            img = File(sf)
            p = Photo(title=name, photo_set=ps)
            p.image.save(name, img)
            p.save()
            generate_all_aliases(p.image, include_global=True)

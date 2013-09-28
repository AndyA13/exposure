# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Photo.exif'
        db.add_column(u'photos_photo', 'exif',
                      self.gf('djorm_hstore.fields.DictionaryField')(default=None, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Photo.exif'
        db.delete_column(u'photos_photo', 'exif')


    models = {
        u'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'exif': ('djorm_hstore.fields.DictionaryField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photos.PhotoSet']", 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'title'", 'unique_with': '()'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'photos.photoset': {
            'Meta': {'object_name': 'PhotoSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        }
    }

    complete_apps = ['photos']
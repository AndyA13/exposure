# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Photo', fields ['slug']
        db.delete_unique(u'photos_photo', ['slug'])

        # Adding unique constraint on 'Photo', fields ['slug', 'photo_set']
        db.create_unique(u'photos_photo', ['slug', 'photo_set_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Photo', fields ['slug', 'photo_set']
        db.delete_unique(u'photos_photo', ['slug', 'photo_set_id'])

        # Adding unique constraint on 'Photo', fields ['slug']
        db.create_unique(u'photos_photo', ['slug'])


    models = {
        u'photos.photo': {
            'Meta': {'unique_together': "(('slug', 'photo_set'),)", 'object_name': 'Photo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'exif': ('djorm_hstore.fields.DictionaryField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photos.PhotoSet']", 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'title'"}),
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
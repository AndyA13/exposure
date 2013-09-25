# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PhotoSet.slug'
        db.add_column(u'photos_photoset', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default='', unique=True, max_length=50, populate_from='name', unique_with=()),
                      keep_default=False)

        # Adding field 'Photo.slug'
        db.add_column(u'photos_photo', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default='', unique=True, max_length=50, populate_from='title', unique_with=()),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PhotoSet.slug'
        db.delete_column(u'photos_photoset', 'slug')

        # Deleting field 'Photo.slug'
        db.delete_column(u'photos_photo', 'slug')


    models = {
        u'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
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
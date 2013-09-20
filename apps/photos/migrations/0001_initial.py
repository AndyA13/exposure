# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhotoSet'
        db.create_table(u'photos_photoset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'photos', ['PhotoSet'])

        # Adding model 'Photo'
        db.create_table(u'photos_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('photo_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.PhotoSet'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'photos', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'PhotoSet'
        db.delete_table(u'photos_photoset')

        # Deleting model 'Photo'
        db.delete_table(u'photos_photo')


    models = {
        u'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photos.PhotoSet']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'photos.photoset': {
            'Meta': {'object_name': 'PhotoSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['photos']
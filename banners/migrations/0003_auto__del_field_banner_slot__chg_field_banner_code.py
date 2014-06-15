# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Banner.slot'
        db.delete_column('banners_banner', 'slot')


        # Changing field 'Banner.code'
        db.alter_column('banners_banner', 'code', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True))

    def backwards(self, orm):
        # Adding field 'Banner.slot'
        db.add_column('banners_banner', 'slot',
                      self.gf('tagging.fields.TagField')(default=''),
                      keep_default=False)


        # Changing field 'Banner.code'
        db.alter_column('banners_banner', 'code', self.gf('django.db.models.fields.CharField')(null=True, max_length=1024))

    models = {
        'banners.banner': {
            'Meta': {'object_name': 'Banner'},
            'clicks': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True', 'default': '0'}),
            'code': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '1024', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True', 'default': '0'})
        },
        'banners.templatebanner': {
            'Meta': {'object_name': 'TemplateBanner', '_ormbases': ['banners.Banner']},
            'banner_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['banners.Banner']"}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '70', 'default': "'banner.html'"}),
            'url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['banners']
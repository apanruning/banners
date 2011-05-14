# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TemplateBanner'
        db.create_table('banners_templatebanner', (
            ('banner_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['banners.Banner'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('template', self.gf('django.db.models.fields.CharField')(default='banner.html', max_length=70)),
        ))
        db.send_create_signal('banners', ['TemplateBanner'])

        # Deleting field 'Banner.url'
        db.delete_column('banners_banner', 'url')

        # Deleting field 'Banner.image'
        db.delete_column('banners_banner', 'image')

        # Changing field 'Banner.code'
        db.alter_column('banners_banner', 'code', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))


    def backwards(self, orm):
        
        # Deleting model 'TemplateBanner'
        db.delete_table('banners_templatebanner')

        # Adding field 'Banner.url'
        db.add_column('banners_banner', 'url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Banner.image'
        raise RuntimeError("Cannot reverse this migration. 'Banner.image' and its values cannot be restored.")

        # Changing field 'Banner.code'
        db.alter_column('banners_banner', 'code', self.gf('django.db.models.fields.TextField')(default=''))


    models = {
        'banners.banner': {
            'Meta': {'object_name': 'Banner'},
            'clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('tagging.fields.TagField', [], {}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'banners.templatebanner': {
            'Meta': {'object_name': 'TemplateBanner', '_ormbases': ['banners.Banner']},
            'banner_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['banners.Banner']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'banner.html'", 'max_length': '70'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['banners']

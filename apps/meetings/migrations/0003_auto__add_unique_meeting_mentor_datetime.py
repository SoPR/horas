# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Meeting', fields ['mentor', 'datetime']
        db.create_unique('meetings_meeting', ['mentor_id', 'datetime'])


    def backwards(self, orm):
        # Removing unique constraint on 'Meeting', fields ['mentor', 'datetime']
        db.delete_unique('meetings_meeting', ['mentor_id', 'datetime'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'meetings.meeting': {
            'Meta': {'unique_together': "(('mentor', 'datetime'),)", 'object_name': 'Meeting'},
            'cancelled_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['profiles.User']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.User']", 'related_name': "'mentors'"}),
            'protege': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proteges'", 'to': "orm['profiles.User']", 'null': 'True', 'blank': 'True'})
        },
        'profiles.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'day_of_week': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'db_index': 'True', 'max_length': '1'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'facebook_username': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'github_username': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'google': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jitsi': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'skype': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True', 'null': 'True'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'website_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['meetings']
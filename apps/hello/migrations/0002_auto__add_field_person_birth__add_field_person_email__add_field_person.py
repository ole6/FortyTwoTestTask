# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.birth'
        db.add_column(u'hello_person', 'birth',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=50),
                      keep_default=False)

        # Adding field 'Person.email'
        db.add_column(u'hello_person', 'email',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=50),
                      keep_default=False)

        # Adding field 'Person.jabber'
        db.add_column(u'hello_person', 'jabber',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=50),
                      keep_default=False)

        # Adding field 'Person.skype'
        db.add_column(u'hello_person', 'skype',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=50),
                      keep_default=False)

        # Adding field 'Person.site'
        db.add_column(u'hello_person', 'site',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.birth'
        db.delete_column(u'hello_person', 'birth')

        # Deleting field 'Person.email'
        db.delete_column(u'hello_person', 'email')

        # Deleting field 'Person.jabber'
        db.delete_column(u'hello_person', 'jabber')

        # Deleting field 'Person.skype'
        db.delete_column(u'hello_person', 'skype')

        # Deleting field 'Person.site'
        db.delete_column(u'hello_person', 'site')


    models = {
        u'hello.person': {
            'Meta': {'object_name': 'Person'},
            'birth': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hello']
# encoding: utf-8
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from longeruserfields.util import get_field_length


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Changing field 'User.username'
        db.alter_column('auth_user', 'username', models.CharField(max_length=get_field_length("username")))
        # Changing field 'User.first_name'
        db.alter_column('auth_user', 'first_name', models.CharField(max_length=get_field_length("first_name")))
        # Changing field 'User.last_name'
        db.alter_column('auth_user', 'last_name', models.CharField(max_length=get_field_length("last_name")))


    def backwards(self, orm):
        # Changing field 'User.username'
        db.alter_column('auth_user', 'username', models.CharField(max_length=30))
        # Changing field 'User.first_name'
        db.alter_column('auth_user', 'first_name', models.CharField(max_length=30))
        # Changing field 'User.last_name'
        db.alter_column('auth_user', 'last_name', models.CharField(max_length=30))


    models = {
        
    }

    complete_apps = ['django_monkeypatches']

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Certificate.der_encoded'
        db.alter_column('pki_certificate', 'der_encoded', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'Certificate.active'
        db.alter_column('pki_certificate', 'active', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'Certificate.pkcs12_encoded'
        db.alter_column('pki_certificate', 'pkcs12_encoded', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'CertificateAuthority.der_encoded'
        db.alter_column('pki_certificateauthority', 'der_encoded', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'CertificateAuthority.active'
        db.alter_column('pki_certificateauthority', 'active', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'x509Extension.key_usage_critical'
        db.alter_column('pki_x509extension', 'key_usage_critical', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'x509Extension.extended_key_usage_critical'
        db.alter_column('pki_x509extension', 'extended_key_usage_critical', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'x509Extension.crl_distribution_point'
        db.alter_column('pki_x509extension', 'crl_distribution_point', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'x509Extension.basic_constraints_critical'
        db.alter_column('pki_x509extension', 'basic_constraints_critical', self.gf('django.db.models.fields.BooleanField')(blank=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'Certificate.der_encoded'
        db.alter_column('pki_certificate', 'der_encoded', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Certificate.active'
        db.alter_column('pki_certificate', 'active', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Certificate.pkcs12_encoded'
        db.alter_column('pki_certificate', 'pkcs12_encoded', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'CertificateAuthority.der_encoded'
        db.alter_column('pki_certificateauthority', 'der_encoded', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'CertificateAuthority.active'
        db.alter_column('pki_certificateauthority', 'active', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'x509Extension.key_usage_critical'
        db.alter_column('pki_x509extension', 'key_usage_critical', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'x509Extension.extended_key_usage_critical'
        db.alter_column('pki_x509extension', 'extended_key_usage_critical', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'x509Extension.crl_distribution_point'
        db.alter_column('pki_x509extension', 'crl_distribution_point', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'x509Extension.basic_constraints_critical'
        db.alter_column('pki_x509extension', 'basic_constraints_critical', self.gf('django.db.models.fields.BooleanField')())
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pki.certificate': {
            'Meta': {'unique_together': "(('name', 'parent'), ('common_name', 'parent'))", 'object_name': 'Certificate'},
            'OU': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'action': ('django.db.models.fields.CharField', [], {'default': "'create'", 'max_length': '32'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'ca_chain': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'CN'", 'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'crl_dpoints': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'der_encoded': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pki.x509Extension']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_length': ('django.db.models.fields.IntegerField', [], {'default': '2048'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pki.CertificateAuthority']", 'null': 'True', 'blank': 'True'}),
            'parent_passphrase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'passphrase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pkcs12_encoded': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pkcs12_passphrase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'revoked': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'subjaltname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'valid_days': ('django.db.models.fields.IntegerField', [], {})
        },
        'pki.certificateauthority': {
            'Meta': {'object_name': 'CertificateAuthority'},
            'OU': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'action': ('django.db.models.fields.CharField', [], {'default': "'create'", 'max_length': '32'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'ca_chain': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'CN'", 'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'crl_dpoints': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'der_encoded': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pki.x509Extension']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_length': ('django.db.models.fields.IntegerField', [], {'default': '2048'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pki.CertificateAuthority']", 'null': 'True', 'blank': 'True'}),
            'parent_passphrase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'passphrase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'policy': ('django.db.models.fields.CharField', [], {'default': "'policy_anything'", 'max_length': '50'}),
            'revoked': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'valid_days': ('django.db.models.fields.IntegerField', [], {})
        },
        'pki.extendedkeyusage': {
            'Meta': {'object_name': 'ExtendedKeyUsage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'pki.keyusage': {
            'Meta': {'object_name': 'KeyUsage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'pki.pkichangelog': {
            'Meta': {'object_name': 'PkiChangelog', 'db_table': "'pki_changelog'"},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'changes': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'pki.x509extension': {
            'Meta': {'object_name': 'x509Extension'},
            'authority_key_identifier': ('django.db.models.fields.CharField', [], {'default': "'keyid:always,issuer:always'", 'max_length': '255'}),
            'basic_constraints': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'basic_constraints_critical': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'crl_distribution_point': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'extended_key_usage': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['pki.ExtendedKeyUsage']", 'null': 'True', 'blank': 'True'}),
            'extended_key_usage_critical': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_usage': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['pki.KeyUsage']", 'null': 'True', 'blank': 'True'}),
            'key_usage_critical': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'subject_key_identifier': ('django.db.models.fields.CharField', [], {'default': "'hash'", 'max_length': '255'})
        }
    }
    
    complete_apps = ['pki']

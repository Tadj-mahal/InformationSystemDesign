# Generated by Django 4.1.7 on 2023-04-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing', '0002_alter_clientcodes_iac'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcodes',
            name='OS',
            field=models.CharField(choices=[('windows', 'Windows'), ('linux', 'Linux'), ('debian', 'Debian'), ('openbsd', 'OpenBSD'), ('macos', 'Mac OS')], default='windows', max_length=30),
        ),
    ]

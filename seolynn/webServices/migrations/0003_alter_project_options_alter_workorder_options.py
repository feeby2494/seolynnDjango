# Generated by Django 4.1.7 on 2023-02-24 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webServices', '0002_alter_project_description_alter_project_project_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('project_name',)},
        ),
        migrations.AlterModelOptions(
            name='workorder',
            options={'ordering': ('-date_submitted',)},
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-10 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.project')),
                ('stack_used', models.TextField()),
                ('desc', models.TextField()),
            ],
            bases=('portfolio.project',),
        ),
        migrations.CreateModel(
            name='CaseStudy',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.project')),
                ('r_lang', models.BooleanField()),
                ('python', models.BooleanField()),
                ('short_desc', models.TextField()),
            ],
            bases=('portfolio.project',),
        ),
    ]
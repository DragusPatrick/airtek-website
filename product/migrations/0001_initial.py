# Generated by Django 3.0.2 on 2020-02-21 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Product Page',
                'verbose_name_plural': 'Product Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]

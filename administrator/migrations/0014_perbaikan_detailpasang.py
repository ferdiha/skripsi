# Generated by Django 3.1.7 on 2022-07-04 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0013_remove_settingpembayaran_va'),
    ]

    operations = [
        migrations.AddField(
            model_name='perbaikan',
            name='detailpasang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.detailpasang'),
        ),
    ]
# Generated by Django 2.2.7 on 2019-11-24 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191124_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='fDepartmet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Department'),
        ),
    ]
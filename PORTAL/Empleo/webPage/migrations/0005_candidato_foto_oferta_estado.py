# Generated by Django 4.0.4 on 2022-05-23 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0004_remove_candidato_foto_remove_oferta_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='oferta',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
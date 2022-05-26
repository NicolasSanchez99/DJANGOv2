# Generated by Django 4.0.4 on 2022-05-26 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0009_postulados_unique_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='ciudad',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webPage.ciudad'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='tipo_documento',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webPage.tipo_doc'),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='tipo_contrato',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='webPage.tipocontrato'),
        ),
    ]

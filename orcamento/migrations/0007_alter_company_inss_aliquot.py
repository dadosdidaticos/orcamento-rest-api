# Generated by Django 4.2.1 on 2023-05-25 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamento', '0006_alter_company_options_company_inss_aliquot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='inss_aliquot',
            field=models.DecimalField(decimal_places=3, max_digits=20),
        ),
    ]

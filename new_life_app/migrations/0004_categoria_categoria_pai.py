# Generated by Django 5.2.3 on 2025-07-02 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_life_app', '0003_produto_lancamento_produto_mais_vendido'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='categoria_pai',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='new_life_app.categoria'),
        ),
    ]

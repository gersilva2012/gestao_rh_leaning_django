# Generated by Django 3.2.5 on 2021-07-27 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='a_quem_pertence',
            new_name='nome_colaborador',
        ),
    ]

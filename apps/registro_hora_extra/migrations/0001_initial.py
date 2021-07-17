# Generated by Django 3.2.5 on 2021-07-17 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colaborador', '0002_colaborador_no_setor'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroHoraExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_extra', models.CharField(help_text='Horas extras', max_length=100)),
                ('motivo_hora_extra', models.TextField(help_text='Faça uma breve descrição do motivo da hora extra')),
                ('data_hora_inicio', models.DateTimeField(help_text='Hora e data inicial')),
                ('data_hora_final', models.DateTimeField(help_text='Hora e data final')),
                ('slug', models.SlugField(help_text='Padrão de referencia', max_length=100, null=True, unique=True)),
                ('data_modificaao', models.DateTimeField(auto_now=True, help_text='Data da criação do arquivo')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, help_text='Data da criação do arquivo')),
                ('pertence_a', models.ForeignKey(help_text='A quem pertence a hora extra', on_delete=django.db.models.deletion.PROTECT, to='colaborador.colaborador')),
            ],
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-08 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planningpoker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now=True)),
                ('vote', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='poll',
            name='username',
            field=models.CharField(max_length=256),
        ),
        migrations.AddField(
            model_name='vote',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planningpoker.Poll'),
        ),
    ]

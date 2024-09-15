# Generated by Django 4.2.6 on 2023-10-16 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomAPIKey',
            fields=[
                ('id', models.CharField(editable=False, max_length=150, primary_key=True, serialize=False, unique=True)),
                ('prefix', models.CharField(editable=False, max_length=8, unique=True)),
                ('hashed_key', models.CharField(editable=False, max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(default=None, help_text='A free-form name for the API key. Need not be unique. 50 characters max.', max_length=50)),
                ('revoked', models.BooleanField(blank=True, default=False, help_text='If the API key is revoked, clients cannot use it anymore. (This cannot be undone.)')),
                ('expiry_date', models.DateTimeField(blank=True, help_text='Once API key expires, clients cannot use it anymore.', null=True, verbose_name='Expires')),
                ('key', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'API key',
                'verbose_name_plural': 'API keys',
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('sessionID', models.AutoField(primary_key=True, serialize=False)),
                ('startDateTime', models.DateTimeField(auto_now_add=True)),
                ('endDateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('modelID', models.AutoField(primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('documentID', models.AutoField(primary_key=True, serialize=False)),
                ('documentName', models.CharField(max_length=200)),
                ('modelID_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Application.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='ChatBox',
            fields=[
                ('chatID', models.AutoField(primary_key=True, serialize=False)),
                ('user_query', models.TextField()),
                ('answer', models.TextField()),
                ('starttime', models.DateTimeField(auto_now_add=True)),
                ('endtime', models.DateTimeField(auto_now_add=True)),
                ('session_fk2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Application.session')),
            ],
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-12 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0006_auto_20201211_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('entry_date', models.DateField(help_text='Joining Date')),
                ('exit_date', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('time_percent', models.IntegerField(verbose_name='100 if Full Time')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('comments', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
                ('org_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.orgunit')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.employee')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalEmployee',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('employee_id', models.CharField(db_index=True, max_length=20)),
                ('full_name', models.CharField(max_length=50)),
                ('entry_date', models.DateField(help_text='Joining Date')),
                ('exit_date', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('time_percent', models.IntegerField(verbose_name='100 if Full Time')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('comments', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('org', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.organization')),
                ('org_unit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.orgunit')),
                ('supervisor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.employee')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical employee',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RemoveField(
            model_name='person',
            name='org',
        ),
        migrations.RemoveField(
            model_name='person',
            name='org_unit',
        ),
        migrations.RemoveField(
            model_name='person',
            name='supervisor',
        ),
        migrations.DeleteModel(
            name='HistoricalPerson',
        ),
        migrations.AlterField(
            model_name='historicalorgunit',
            name='manager',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organization.employee'),
        ),
        migrations.AlterField(
            model_name='orgunit',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.employee'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]

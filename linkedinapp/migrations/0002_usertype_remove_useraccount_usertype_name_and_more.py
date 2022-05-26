# Generated by Django 4.0.4 on 2022-05-13 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkedinapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype_name', models.CharField(choices=[('jobseeker', 'Job Seeker'), ('company', 'Company')], max_length=9)),
            ],
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='usertype_name',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='usertype_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='linkedinapp.usertype'),
        ),
    ]
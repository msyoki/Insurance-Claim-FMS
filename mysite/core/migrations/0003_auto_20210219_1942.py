# Generated by Django 2.1.5 on 2021-02-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210219_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.DeleteModel(
            name='ClaimCategory',
        ),
        migrations.AlterField(
            model_name='motorclaim',
            name='image_one',
            field=models.ImageField(upload_to='RootFile/Motor_Claims/images/'),
        ),
        migrations.AlterField(
            model_name='motorclaim',
            name='image_three',
            field=models.ImageField(upload_to='RootFile/Motor_Claims/images/'),
        ),
        migrations.AlterField(
            model_name='motorclaim',
            name='image_two',
            field=models.ImageField(upload_to='RootFile/Motor_Claims/images/'),
        ),
    ]

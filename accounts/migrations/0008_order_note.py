# Generated by Django 3.0.7 on 2020-07-06 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200703_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for Delievery', 'Out for Delievery'), ('Delivered', 'Delivered')], max_length=1000, null=True),
        ),
    ]

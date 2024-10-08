# Generated by Django 5.1 on 2024-09-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divingrecord',
            name='discipline',
            field=models.CharField(choices=[('DYN', 'Dynamic with Fins (DYN)'), ('DNF', 'Dynamic No Fins (DNF)'), ('DYNB', 'Dynamic with Bi-Fins (DYNB)'), ('FIM', 'Free Immersion (FIM)'), ('CTW', 'Constant Weight (CTW)'), ('CTWB', 'Constant Weight Bi-Fins (CTWB)'), ('CNF', 'Constant Weight No Fins (CNF)'), ('STA', 'Static apnea (STA)')], default='DYN', max_length=4),
        ),
    ]

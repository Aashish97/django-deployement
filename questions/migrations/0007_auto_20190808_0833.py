# Generated by Django 2.1.7 on 2019-08-08 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_question_accepted_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='accepted_answer',
            new_name='approved_answer',
        ),
    ]

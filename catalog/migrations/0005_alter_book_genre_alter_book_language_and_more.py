# Generated by Django 4.2.6 on 2023-10-14 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Choose the genre', null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.genre', verbose_name="The book's genre"),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Choose language', null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.language', verbose_name="The book's language"),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.ForeignKey(help_text='Change status', null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.status', verbose_name='Status of the book'),
        ),
    ]

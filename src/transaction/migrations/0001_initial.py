# Generated by Django 3.1.6 on 2021-06-19 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='created_at', verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='modified_at', verbose_name='modified_at')),
                ('name', models.CharField(help_text='name', max_length=18, verbose_name='name')),
                ('email', models.CharField(help_text='email', max_length=18, verbose_name='email')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'transaction_user',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='created_at', verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='modified_at', verbose_name='modified_at')),
                ('total', models.SmallIntegerField(help_text='total', verbose_name='total')),
                ('status', models.CharField(choices=[('deposit', 'DEPOSIT'), ('withdraw', 'WITHDRAW')], default='deposit', help_text='status', max_length=18, verbose_name='status')),
                ('user', models.ForeignKey(help_text='user', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='transaction.user', verbose_name='user')),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
                'db_table': 'transaction_payments',
            },
        ),
    ]
# Generated by Django 3.2.6 on 2021-09-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingbasket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'در انتظار پرداخت'), ('S', 'درحال ارسال'), ('D', 'تحویل داده شده')], default='P', max_length=1, verbose_name='وضعیت'),
        ),
    ]
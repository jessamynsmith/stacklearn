# Generated by Django 2.0.1 on 2018-01-05 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180105_1743'),
        ('mathstack', '0004_booleananswer_integeranswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BooleanQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operand1', models.IntegerField()),
                ('operand2', models.IntegerField()),
                ('operator', models.CharField(choices=[('MODULUS', '%')], max_length=2)),
                ('correct_answer', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='booleananswer',
            name='right_answer',
        ),
        migrations.AlterField(
            model_name='booleananswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mathstack.BooleanQuestion'),
        ),
        migrations.AddField(
            model_name='activequestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mathstack.BooleanQuestion'),
        ),
        migrations.AddField(
            model_name='activequestion',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='activequestion',
            unique_together={('student', 'question')},
        ),
    ]

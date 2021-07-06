# Generated by Django 3.2.4 on 2021-07-06 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fb88',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Hay dien doi bong ban dat cuoc ', max_length=255, null=True, verbose_name='Dat cuoc cho doi bong than yeu')),
            ],
            options={
                'verbose_name': 'Fb88',
                'verbose_name_plural': 'Nha cai uy tin',
                'db_table': 'nhacai_fb88',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/images/%Y/%m/%d')),
                ('h', models.FloatField(blank=True, default=0, null=True)),
                ('w', models.FloatField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'tbl_image',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, help_text='Bạn muốn cược đội nào giải này', max_length=255, null=True, verbose_name='Dat cuoc')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('fb88', models.ForeignKey(blank=True, help_text='Chon dat cuoc', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Selection', to='fb88.fb88')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='question_image', to='fb88.image')),
            ],
            options={
                'verbose_name': 'Cau hoi',
                'verbose_name_plural': 'Cau hoi?',
                'db_table': 'fb88_question',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, help_text='Hay dien ten doi bong muon cuoc ', max_length=255, null=True, verbose_name='Cau tra loi ')),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('question', models.ForeignKey(blank=True, help_text='Selection', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='fb88.question')),
            ],
            options={
                'verbose_name': 'Cau tra loi',
                'verbose_name_plural': 'cau tra loi',
                'db_table': 'fb88_answer',
            },
        ),
    ]
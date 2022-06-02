# Generated by Django 4.0.3 on 2022-05-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('PostID', models.IntegerField(primary_key=True, serialize=False, verbose_name='번호')),
                ('Title', models.CharField(max_length=50, verbose_name='제목')),
                ('Contents', models.TextField(verbose_name='본문')),
                ('Category', models.CharField(max_length=15)),
                ('AccID', models.CharField(max_length=15, verbose_name='작성자')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('Clicked', models.IntegerField(verbose_name='조회수')),
            ],
            options={
                'db_table': 'community',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BoardContents',
            fields=[
                ('PostID', models.IntegerField(primary_key=True, serialize=False, verbose_name='번호')),
                ('Title', models.CharField(max_length=50, verbose_name='제목')),
                ('Contents', models.TextField(verbose_name='본문')),
                ('AccID', models.CharField(max_length=15, verbose_name='작성자')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('Clicked', models.IntegerField(verbose_name='조회수')),
            ],
            options={
                'db_table': 'community',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('CommentID', models.IntegerField(primary_key=True, serialize=False, verbose_name='번호')),
                ('AccID', models.CharField(max_length=15, verbose_name='작성자')),
                ('Comment', models.CharField(max_length=100, verbose_name='댓글')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('TeaserID', models.IntegerField(verbose_name='번호')),
                ('ParentID', models.IntegerField(verbose_name='부모댓글')),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('PostID', models.IntegerField(primary_key=True, serialize=False, verbose_name='번호')),
                ('Title', models.CharField(max_length=50, verbose_name='제목')),
                ('Category', models.CharField(max_length=15)),
                ('AccID', models.CharField(max_length=15, verbose_name='작성자')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('Clicked', models.IntegerField(verbose_name='조회수')),
            ],
            options={
                'db_table': 'community',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FinalComment',
            fields=[
                ('CommentID', models.IntegerField(primary_key=True, serialize=False, verbose_name='번호')),
                ('AccID', models.CharField(max_length=15, verbose_name='작성자')),
                ('Answer', models.CharField(max_length=100, verbose_name='댓글')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('PostID', models.IntegerField(verbose_name='번호')),
                ('Likes', models.IntegerField(verbose_name='추천')),
                ('ParentID', models.IntegerField(verbose_name='부모댓글')),
            ],
            options={
                'db_table': 'final_Comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('TeaserID', models.IntegerField(primary_key=True, serialize=False, verbose_name='번호')),
                ('Title', models.CharField(max_length=50, verbose_name='제목')),
                ('Teaser', models.TextField(verbose_name='본문')),
                ('Category', models.CharField(max_length=15)),
                ('AccID', models.CharField(max_length=15, verbose_name='작성자')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('Clicked', models.IntegerField(verbose_name='조회수')),
            ],
            options={
                'db_table': 'brainTeaser',
                'managed': False,
            },
        ),
    ]
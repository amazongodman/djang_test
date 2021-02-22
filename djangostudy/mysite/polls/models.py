from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    imege = models.ImageField(upload_to = 'media/')
    # mediaという場所に画像をアップロードするという指定
    body = models.TextField()
    # ブログ文書をかけるようにtextを入れる場所を作っておく
    # この文章たちが定義そのものとなり、makemigrateによって自動的に読み込まれ、整合性が取れるようにpipからパッケージを探してくれる。

    def __str__(self):
        return self.question_text

    def summary(self):
        return self.body[:30]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
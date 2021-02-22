from django.db import models

# Create your models here.

#モデルの中身に定義されているPostのクラスがデータべーずと繋がる？
#クラスごとにデータベースを分けること可能？テーブルを分けるとかでなく
#というかテーブルは何を基準に分かれるのか？

class Post(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()














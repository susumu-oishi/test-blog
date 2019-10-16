from django.conf import settings
from django.db import models
from django.utils import timezone

"""
class：オブジェクトを定義

models.Model:はポストがDjango Modelだという意味で、Djangoが、
これはデータベースに保存すべきものだと分かるようにしています。

author title text created_date published_date : プロパティを定義　フィールドのタイプを決めなくてはいけない。
    models.CharField – 文字数が制限されたテキストを定義するフィールド
    models.TextField – これは制限無しの長いテキスト用です。ブログポストのコンテンツに理想的なフィールドでしょ？
    models.DateTimeField – 日付と時間のフィールド
    models.ForeignKey – これは他のモデルへのリンク

publish(self): ブログを公開するメソッド（=関数？）

"""
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

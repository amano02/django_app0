from django.db import models
from django.utils import timezone

class Client(models.Model):
    """
    要件3.2 ① Client テーブル（顧客情報）
    """
    name = models.CharField("会社名・氏名", max_length=100)
    email = models.EmailField("連絡先", blank=True, null=True)
    note = models.TextField("特記事項", blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    要件3.2 ② Category テーブル（業務分類）
    """
    name = models.CharField("業務分類名", max_length=50) # イラスト, Web制作など

    def __str__(self):
        return self.name

class Project(models.Model):
    """
    要件3.2 ③ Project テーブル（案件情報）
    """
    # ステータス定義 (要件2.1)
    STATUS_CHOICES = [
        ('not_started', '未着手'),
        ('in_progress', '進行中'),
        ('checking', '確認中'),
        ('completed', '完了'),
        ('billed', '請求済'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="クライアント")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="カテゴリ")
    title = models.CharField("案件名", max_length=200)
    status = models.CharField("進捗状況", max_length=20, choices=STATUS_CHOICES, default='not_started')
    price = models.IntegerField("報酬額", default=0)
    deadline = models.DateField("納期")
    note = models.TextField("フリーメモ", blank=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['deadline'] # 納期順に表示

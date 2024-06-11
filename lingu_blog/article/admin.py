"""
需要“告诉”Django，后台中需要添加ArticlePost这个数据表供管理
"""
from django.contrib import admin

from .models import ArticlePost

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)

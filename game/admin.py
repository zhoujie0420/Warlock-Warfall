from django.contrib import admin
from game.models.player.player import Player # 引入自己定义的数据表


# Register your models here.


admin.site.register(Player) # 注册这个数据表

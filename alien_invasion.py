import sys
import pygame
from settings import Settings
from ship import Ship
import game_functons as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

#再次进行更改
#好像有点问题啊
#好像有点意思了
#有点迷糊了
#创建了一个分支
#创建了一个分支
#新添加的东西
#问题还是很多的啊
#new change2
#new change3
#哈哈
#哈哈
#不明白也没办法吗啊，只能自己搞啊
#切换前要commit
#新版本的Git
#出问题了
#重新测试一下，看看情况
run_game()
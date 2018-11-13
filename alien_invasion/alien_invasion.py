import pygame

from settings import Settings
from ship import Ship

import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():
	#初始化pygame，为使用硬件做准备。设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('外星人入侵')



	#创建play按钮
	play_button = Button(ai_settings, screen, 'Play')
	pygame.mixer_music.load('bgm.mp3')
	pygame.mixer_music.set_volume(0.2)
	pygame.mixer_music.play(50)
	
	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()

	#创建一个外星人编组
	aliens = Group()
	#创建外星人群
	gf.creat_fleet(ai_settings,screen,ship,aliens)


	#开始游戏的主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, stats, sb, play_button,
			ship, aliens, bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen, stats, sb, ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb, ship,aliens,bullets)

		gf.update_screen(ai_settings, screen, stats, sb, ship,aliens,bullets, 
			play_button)

		
run_game() 
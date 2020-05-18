#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-14 21:23:34
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-18 14:43:02
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

import os
import sys
import logging

import pygame
import pygame.locals as gloc

from .typing import Scene


class Game(object):
    """Main Game Object

    Attributes:
        screen (pygame.Surface): Screen object
        screen_size (Tuple[int, int]): Screen size
        width (int): Screen width
        height (int): Screen height
        
        font (pygame.font.Font): Font object
        clock (pygame.time.Clock): Clock object
        
        home (bool): Scene flag - home
        refresh (bool): Scene flag - refresh
        game (bool): Scene flag - game
        end (bool): Scene flag - end
        
        rects (Dict[str, pygame.Rect]): Rect objects
        words (Dict[str, pygame.Surface]): Static words
        images (Dict[str, pygame.Surface]): Static images
        
        delay (int): Delay
        score (int): Game score
        left_button (pygame.Surface): Left button image
        right_button (pygame.Surface): Right button image
        up_button (pygame.Surface): Up button image
        down_button (pygame.Surface): Down button image
    """

    def __init__(self):
        """Initialize the game. Including pictures, musics and variables
        """
        pygame.init()
        self.screen_size = self.width, self.height = 611, 916
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Tetris")

        # Init clock
        self.clock = pygame.time.Clock()

        # Init font
        self.font = pygame.font.Font(
            os.path.join(os.path.dirname(__file__), "assets/font/msyh.ttf"), 16)
        self.words = {
            "pause": self.font.render("Pause(P)", True, (0, 0, 0)),
            "sound": self.font.render("Sound(S)", True, (0, 0, 0)),
            "reset": self.font.render("Reset(R)", True, (0, 0, 0)),
            "space": self.font.render("Drop(SPACE)", True, (0, 0, 0)),
            "left": self.font.render("Left", True, (0, 0, 0)),
            "up": self.font.render("Rotation", True, (0, 0, 0)),
            "right": self.font.render("Right", True, (0, 0, 0)),
            "down": self.font.render("Down", True, (0, 0, 0))
        }

        # Load images
        self.load_images()
        self.rects = {
            "pause": pygame.Rect(46, 610, 50, 50),
            "sound": pygame.Rect(136, 610, 50, 50),
            "reset": pygame.Rect(226, 610, 50, 50),
            "space": pygame.Rect(82, 710, 153, 153),
            "left": pygame.Rect(314, 700, 96, 96),
            "up": pygame.Rect(404, 610, 96, 96),
            "right": pygame.Rect(494, 700, 96, 96),
            "down": pygame.Rect(404, 790, 96, 96),
        }

        # Init Scene flags
        self.home = True
        self.refresh = False
        self.game = False
        self.end = False

        self.init_vars()

    def load_images(self):
        """Load static images"""
        # 背景
        background = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "assets/image/background.png")).convert_alpha()

        # 按钮
        red = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "assets/image/red.png")).convert_alpha()
        red_pushed = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "assets/image/red_pushed.png")).convert_alpha()
        green = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "assets/image/green.png")).convert_alpha()
        green_pushed = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "assets/image/green_pushed.png")).convert_alpha()
        blue_sm = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "assets/image/blue_sm.png")).convert_alpha()
        blue_sm_pushed = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "assets/image/blue_sm_pushed.png")).convert_alpha()
        blue_lg = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "assets/image/blue_lg.png")).convert_alpha()
        blue_lg_pushed = pygame.image.load(
            os.path.join(os.path.dirname(__file__),
                         "assets/image/blue_lg_pushed.png")).convert_alpha()

        self.images = {
            "background": background,
            "red": red,
            "red_pushed": red_pushed,
            "green": green,
            "green_pushed": green_pushed,
            "blue_sm": blue_sm,
            "blue_sm_pushed": blue_sm_pushed,
            "blue_lg": blue_lg,
            "blue_lg_pushed": blue_lg_pushed
        }

    def init_vars(self):
        """Initialize the variables."""
        self.delay = 0
        self.score = 0

        # 按钮
        self.pause_button = self.images["green"]
        self.sound_button = self.images["green"]
        self.reset_button = self.images["red"]
        self.space_button = self.images["blue_lg"]
        self.left_button = self.images["blue_sm"]
        self.right_button = self.images["blue_sm"]
        self.up_button = self.images["blue_sm"]
        self.down_button = self.images["blue_sm"]

    def switch_scene(self, scene: Scene):
        """Switch current scene

        Args:
            scene (Scene): Target scene
        """
        if scene == Scene.HOME:
            self.home = True
            self.game = False
            self.end = False
        elif scene == Scene.REFRESH:
            self.home = False
            self.refresh = True
            self.game = False
            self.end = False
        elif scene == Scene.GAME:
            self.home = False
            self.game = True
            self.end = False
        elif scene == Scene.END:
            self.home = False
            self.game = False
            self.end = True
        else:
            logging.warning(f"Unknow Scene {scene!s}")

    def start(self):
        """Main game loop."""
        while True:
            # 事件响应
            for event in pygame.event.get():
                # 退出事件
                if event.type == gloc.QUIT:
                    pygame.quit()
                    sys.exit()

                # 键盘事件
                elif event.type == gloc.KEYDOWN:
                    ...

                elif event.type == gloc.KEYUP:
                    ...

                # 鼠标点击
                elif event.type == gloc.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if event.button == 1:
                        if self.rects["pause"].collidepoint(pos):
                            self.pause_button = self.images["green_pushed"]
                        elif self.rects["sound"].collidepoint(pos):
                            self.sound_button = self.images["green_pushed"]
                        elif self.rects["reset"].collidepoint(pos):
                            self.reset_button = self.images["red_pushed"]
                        elif self.rects["space"].collidepoint(pos):
                            self.space_button = self.images["blue_lg_pushed"]
                        elif self.rects["left"].collidepoint(pos):
                            self.left_button = self.images["blue_sm_pushed"]
                        elif self.rects["up"].collidepoint(pos):
                            self.up_button = self.images["blue_sm_pushed"]
                        elif self.rects["right"].collidepoint(pos):
                            self.right_button = self.images["blue_sm_pushed"]
                        elif self.rects["down"].collidepoint(pos):
                            self.down_button = self.images["blue_sm_pushed"]

                # 鼠标点击释放
                elif event.type == gloc.MOUSEBUTTONUP:
                    self.pause_button = self.images["green"]
                    self.sound_button = self.images["green"]
                    self.reset_button = self.images["red"]
                    self.space_button = self.images["blue_lg"]
                    self.left_button = self.images["blue_sm"]
                    self.right_button = self.images["blue_sm"]
                    self.up_button = self.images["blue_sm"]
                    self.down_button = self.images["blue_sm"]

            # 基础背景绘制
            self.screen.blit(self.images["background"], (0, 0))

            # 绘制按钮
            self.screen.blit(self.pause_button, self.rects["pause"])
            self.screen.blit(self.sound_button, self.rects["sound"])
            self.screen.blit(self.reset_button, self.rects["reset"])
            self.screen.blit(self.space_button, self.rects["space"])
            self.screen.blit(self.left_button, self.rects["left"])
            self.screen.blit(self.up_button, self.rects["up"])
            self.screen.blit(self.right_button, self.rects["right"])
            self.screen.blit(self.down_button, self.rects["down"])
            self.screen.blit(self.words["pause"], (46, 665))
            self.screen.blit(self.words["sound"], (136, 665))
            self.screen.blit(self.words["reset"], (226, 665))
            self.screen.blit(self.words["space"], (107, 868))
            self.screen.blit(self.words["left"], (346, 800))
            self.screen.blit(self.words["up"], (504, 630))
            self.screen.blit(self.words["right"], (520, 800))
            self.screen.blit(self.words["down"], (429, 886))

            # 首页
            if self.home:
                ...
            # 游戏界面
            elif self.game:
                ...
            # 游戏结束画面
            elif self.end:
                ...

            # 记录当前帧数
            self.delay = (self.delay + 1) % 30

            # 设置帧率为30
            self.clock.tick(30)

            # 刷新画面
            pygame.display.update()

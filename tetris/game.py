#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-14 21:23:34
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-15 22:18:10
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

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
        clock (pygame.time.Clock): Clock object
        home (bool): Scene flag - home
        help (bool): Scene flag - help
        game (bool): Scene flag - game
        end (bool): Scene flag - end
        score (int): Game score
    """

    def __init__(self):
        """Initialize the game. Including pictures, musics and variables
        """
        pygame.init()
        self.screen_size = self.width, self.height = 512, 512
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Tetris")

        # Init clock
        self.clock = pygame.time.Clock()

        # Init Scene flags
        self.home = True
        self.help = False
        self.game = False
        self.end = False

        self.init_vars()

    def init_vars(self):
        """Initialize the variables."""
        self.score = 0

    def switch_scene(self, scene: Scene):
        """Switch current scene

        Args:
            scene (Scene): Target scene
        """
        if scene == Scene.HOME:
            self.home = True
            self.help = False
            self.game = False
            self.end = False
        elif scene == Scene.HELP:
            self.help = True
        elif scene == Scene.GAME:
            self.home = False
            self.help = False
            self.game = True
            self.end = False
        elif scene == Scene.END:
            self.home = False
            self.help = False
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

                # 鼠标点击释放
                elif event.type == gloc.MOUSEBUTTONUP:
                    ...

            # 基础背景绘制

            # 帮助界面（临时界面优先）
            if self.help:
                ...
            # 首页
            elif self.home:
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-19 22:29:14
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-20 11:50:34
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

import pygame
import numpy as np


class Matrix(pygame.sprite.Sprite):
    """Matrix

    Attributes:
        matrix (numpy.ndarray): matrix (20x10)
        filled_rect (pygame.Surface): filled rectangle
        unfilled_rect (pygame.Surface): unfilled rectangle
        image (pygame.Surface): surface
        rect (pygame.Rect): rect
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.matrix = np.zeros((20, 10), dtype=np.int)
        self.unfilled_rect = pygame.Surface((18, 18)).convert_alpha()
        self.filled_rect = pygame.Surface((18, 18)).convert_alpha()
        for i in range(20):
            for j in range(20):
                if i < 2 or i > 15 or j < 2 or j > 15 or (3 < i < 14 and
                                                          3 < j < 14):
                    self.unfilled_rect.set_at((i, j), (135, 147, 114, 255))
                    self.filled_rect.set_at((i, j), (0, 0, 0, 255))
                else:
                    self.unfilled_rect.set_at((i, j), (135, 147, 114, 0))
                    self.filled_rect.set_at((i, j), (0, 0, 0, 0))

        self.update()

    def update(self):
        self.image = pygame.Surface((198, 398)).convert_alpha()
        self.image.fill((158, 173, 134, 0))
        for i in range(10):
            for j in range(20):
                self.image.blit(
                    self.filled_rect if self.matrix[j,
                                                    i] else self.unfilled_rect,
                    (i * 20, j * 20))
        self.rect = self.image.get_rect()

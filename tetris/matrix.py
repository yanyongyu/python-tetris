#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-19 22:29:14
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-19 22:59:02
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
        image (pygame.Surface): surface
        rect (pygame.Rect): rect
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.matrix = np.zeros((20, 10), dtype=np.int)
        self.update()

    def update(self):
        self.image = pygame.Surface((218, 438))

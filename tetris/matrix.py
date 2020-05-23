#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-19 22:29:14
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-23 18:10:22
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

import random
from typing import List

import pygame
import numpy as np

from .tetris import Tetris
from .tetris import ITetris, TTetris, LTetris, JTetris, OTetris, ZTetris1, ZTetris2


class Matrix(pygame.sprite.Sprite):
    """Matrix

    Attributes:
        matrix (numpy.ndarray): matrix (20x10)
        filled_rect (pygame.Surface): filled rectangle
        unfilled_rect (pygame.Surface): unfilled rectangle
        image (pygame.Surface): surface
        rect (pygame.Rect): rect
        
        bag (List[Tetris]): 7bag
        current (Tetris): current tetris
        next (Tetris): next tetris
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.matrix = np.zeros((25, 14), dtype=np.int)
        self.matrix[:, :2] = 1
        self.matrix[:, -2:] = 1
        self.matrix[-3:, :] = 1
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

        self.bag = self.fill_bag()
        self.current = self.bag.pop(random.randint(0, len(self.bag) - 1))
        self.next = self.bag.pop(random.randint(0, len(self.bag) - 1))
        self.update()

    def update(self):
        x = self.current.x + 2
        y = self.current.y + 2
        shape = self.current.matrix.shape
        matrix_ = self.matrix.copy()
        matrix_[y:y + shape[0],
                x:x + shape[1]] += self.current.matrixs[self.current.index]
        self.image = pygame.Surface((198, 398)).convert_alpha()
        self.image.fill((158, 173, 134, 0))
        for i in range(10):
            for j in range(20):
                self.image.blit(
                    self.filled_rect if matrix_[j + 2,
                                                i + 2] else self.unfilled_rect,
                    (i * 20, j * 20))
        self.rect = self.image.get_rect()

    def random_startline(self, start_line: int = 0):
        self.matrix[-3 - start_line:-3,
                    2:-2] += np.random.randint(0, 2, (start_line, 10))

    def check_collision(self) -> bool:
        x = self.current.x + 2
        y = self.current.y + 2
        shape = self.current.matrix.shape
        matrix_ = self.matrix.copy()
        matrix_[y:y + shape[0],
                x:x + shape[1]] += self.current.matrixs[self.current.index]
        return np.any(matrix_ > 1)

    def check_gameover(self) -> bool:
        return np.any(self.matrix[:2, 2:-2] > 0)

    def add_tetris(self):
        x = self.current.x + 2
        y = self.current.y + 2
        shape = self.current.matrix.shape
        self.matrix[y:y + shape[0],
                    x:x + shape[1]] += self.current.matrixs[self.current.index]

    def next_tetris(self):
        self.current = self.next
        self.next = self.bag.pop(random.randint(0, len(self.bag) - 1))
        if not self.bag:
            self.bag = self.fill_bag()

    def fill_bag(self) -> List[Tetris]:
        """7bag"""
        return [
            ITetris(3, -2),
            TTetris(3, -2),
            LTetris(3, -2),
            JTetris(3, -2),
            OTetris(4, -2),
            ZTetris1(3, -2),
            ZTetris2(3, -2)
        ]

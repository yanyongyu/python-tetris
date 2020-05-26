#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-19 22:29:14
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-26 14:28:58
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
        matrix (numpy.ndarray): matrix (25x16)
        filled_rect (pygame.Surface): filled rectangle
        unfilled_rect (pygame.Surface): unfilled rectangle
        image (pygame.Surface): surface
        rect (pygame.Rect): rect
        
        bag (List[Tetris]): 7bag
        current (Tetris): current tetris
        next (Tetris): next tetris
        clearing (bool): whether there are lines to clear
        clear_delay (int): delay of clearing
        clear_lines (numpy.ndarray): array of lines whether to clear or not
        clear_rects (List[pygame.Surface]): List of clearing animation surfaces
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.matrix = np.zeros((25, 16), dtype=np.int)
        self.matrix[:, :3] = 1
        self.matrix[:, -3:] = 1
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

        self.clear_rects = []
        for index in range(8):
            surface = self.unfilled_rect.copy()
            for i in range(2 + index, 16 - index):
                for j in range(2 + index, 16 - index):
                    surface.set_at((i, j), (0, 0, 0, 255))
            self.clear_rects.append(surface)

        self.bag = self.fill_bag()
        self.current = self.bag.pop(random.randint(0, len(self.bag) - 1))
        self.next = self.bag.pop(random.randint(0, len(self.bag) - 1))
        self.clearing = False
        self.clear_delay = 0
        self.clear_lines = np.zeros((25,), dtype=np.bool)
        self.update()

    def update(self):
        x = self.current.x + 3
        y = self.current.y + 2
        shape = self.current.matrix.shape
        matrix_ = self.matrix.copy()
        matrix_[y:y + shape[0],
                x:x + shape[1]] += self.current.matrixs[self.current.index]
        self.image = pygame.Surface((198, 398)).convert_alpha()
        self.image.fill((158, 173, 134, 0))
        if self.clearing:
            for i in range(10):
                for j in range(20):
                    if self.clear_lines[j + 2]:
                        self.image.blit(self.clear_rects[self.clear_delay // 2],
                                        (i * 20, j * 20))
                    else:
                        self.image.blit(
                            self.filled_rect if matrix_[j + 2, i + 3] else
                            self.unfilled_rect, (i * 20, j * 20))

            self.clear_delay = (self.clear_delay + 1) % (2 *
                                                         len(self.clear_rects))
            if self.clear_delay == 0:
                self.after_clear()
        else:
            for i in range(10):
                for j in range(20):
                    self.image.blit(
                        self.filled_rect if matrix_[j + 2, i +
                                                    3] else self.unfilled_rect,
                        (i * 20, j * 20))
        self.rect = self.image.get_rect()

    def random_startline(self, start_line: int = 0):
        self.matrix[-3 - start_line:-3,
                    3:-3] += np.random.randint(0, 2, (start_line, 10))

    def check_collision(self) -> bool:
        x = self.current.x + 3
        y = self.current.y + 2
        shape = self.current.matrix.shape
        matrix_ = self.matrix.copy()
        matrix_[y:y + shape[0],
                x:x + shape[1]] += self.current.matrixs[self.current.index]
        return np.any(matrix_ > 1)

    def check_clear(self) -> int:
        self.clear_lines = np.all(self.matrix, axis=1)
        self.clearing = np.any(self.clear_lines[2:-3])
        return sum(self.clear_lines[2:-3])

    def after_clear(self):
        self.clearing = False
        for index, line in enumerate(self.clear_lines[2:-3]):
            if line:
                tmp = np.delete(self.matrix, index + 2, 0)
                self.matrix = np.insert(tmp, 0, 1, axis=0)
                self.matrix[0, 3:-3] = 0

    def check_gameover(self) -> bool:
        return np.any(self.matrix[:2, 3:-3] > 0)

    def add_tetris(self):
        x = self.current.x + 3
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

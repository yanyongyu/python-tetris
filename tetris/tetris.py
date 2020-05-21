#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-20 16:50:46
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-21 23:26:56
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

import numpy as np


class Tetris(object):

    matrixs = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.index = 0

    def rotate(self):
        raise NotImplementedError()


class ITetris(Tetris):

    matrix = np.zeros((4, 4), dtype=np.int)
    matrix[1] = 1
    matrixs = [matrix, np.rot90(matrix)]

    def rotate(self):
        if 0 <= self.x <= 7:
            self.index = (self.index + 1) % len(self.matrixs)


class TTetris(Tetris):

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[0, 1] = 1
    matrix[1] = 1
    matrixs = [
        matrix,
        np.rot90(matrix),
        np.rot90(matrix, 2),
        np.rot90(matrix, -1)
    ]

    def rotate(self):
        self.index = (self.index + 1) % len(self.matrixs)


class LTetris(Tetris):
    """
    0 1 0  0 0 1  1 1 0  0 0 0
    0 1 0  1 1 1  0 1 0  1 1 1
    0 1 1  0 0 0  0 1 0  1 0 0
    
    """

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[2, 2] = 1
    matrix[:, 1] = 1
    matrixs = [
        matrix,
        np.rot90(matrix),
        np.rot90(matrix, 2),
        np.rot90(matrix, -1)
    ]

    def rotate(self):
        self.index = (self.index + 1) % len(self.matrixs)


class JTetris(Tetris):

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[:, 2] = 1
    matrix[1, 2] = 1
    matrixs = [
        matrix,
        np.rot90(matrix),
        np.rot90(matrix, 2),
        np.rot90(matrix, -1)
    ]


class OTetris(Tetris):

    matrix = np.ones((2, 2), dtype=np.int)
    matrixs = [matrix]

    def rotate(self):
        pass


class ZTetris1(Tetris):

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[:2, 0] = 1
    matrix[1:, 1] = 1
    matrixs = [matrix, np.rot90(matrix)]


class ZTetris2(Tetris):

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[1:, 0] = 1
    matrix[:2, 1] = 1
    matrixs = [matrix, np.rot90(matrix)]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-20 16:50:46
@LastEditors    : yanyongyu
@LastEditTime   : 2020-06-05 21:39:33
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from typing import List

import numpy as np


class Tetris(object):
    """Base Tetris object

    Attributes:
        matrix (numpy.ndarray): base shape of tetris
        matrixs (List[numpy.ndarray]): List of shapes
        x (int): X coordinate
        y (int): Y coordinate
        index (int): Index of the shape
    """

    matrix: np.ndarray = None
    matrixs: List[np.ndarray] = []

    def __init__(self, x: int, y: int, index: int = 0):
        self.x = x
        self.y = y
        self.index = index

    def rotate(self, direction: bool = False):
        """Rotate the tetris

        Args:
            direction (bool, optional): True to rotate counterclockwise. Defaults to False.
        """
        if direction:
            self.index = (self.index + 1) % len(self.matrixs)
        else:
            self.index = (self.index - 1) % len(self.matrixs)

    def move(self, direction: bool = False):
        """Move the tetris

        Args:
            direction (bool, optional): True to move right. Defaults to False.
        """
        if direction:
            self.x += 1
        else:
            self.x -= 1


class ITetris(Tetris):
    """
    Shapes:
        0 0 0 0  0 1 0 0
        1 1 1 1  0 1 0 0
        0 0 0 0  0 1 0 0
        0 0 0 0  0 1 0 0
    """

    matrix = np.zeros((4, 4), dtype=np.int)
    matrix[1, :] = 1
    matrixs = [matrix, np.rot90(matrix)]


class TTetris(Tetris):
    """
    Shapes:
        0 1 0  0 1 0  0 0 0  0 1 0
        1 1 1  1 1 0  1 1 1  0 1 1
        0 0 0  0 1 0  0 1 0  0 1 0
    """

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[0, 1] = 1
    matrix[1, :] = 1
    matrixs = [
        matrix,
        np.rot90(matrix),
        np.rot90(matrix, 2),
        np.rot90(matrix, -1)
    ]


class LTetris(Tetris):
    """
    Shapes:
        0 0 1  1 1 0  0 0 0  0 1 0
        1 1 1  0 1 0  1 1 1  0 1 0
        0 0 0  0 1 0  1 0 0  0 1 1
    """

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[1, :] = 1
    matrix[0, 2] = 1
    matrixs = [
        matrix,
        np.rot90(matrix),
        np.rot90(matrix, 2),
        np.rot90(matrix, -1)
    ]


class JTetris(Tetris):
    """
    Shapes:
        1 0 0  0 1 0  0 0 0  0 1 1
        1 1 1  0 1 0  1 1 1  0 1 0
        0 0 0  1 1 0  0 0 1  0 1 0
    """

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[1, :] = 1
    matrix[0, 0] = 1
    matrixs = [
        matrix,
        np.rot90(matrix),
        np.rot90(matrix, 2),
        np.rot90(matrix, -1)
    ]


class OTetris(Tetris):
    """
    Shapes:
        1 1
        1 1
    """

    matrix = np.ones((2, 2), dtype=np.int)
    matrixs = [matrix]


class ZTetris1(Tetris):
    """
    Shapes:
        1 1 0  0 1 0  0 0 0  0 0 1
        0 1 1  1 1 0  1 1 0  0 1 1
        0 0 0  1 0 0  0 1 1  0 1 0
    """

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[0, :2] = 1
    matrix[1, 1:] = 1
    matrixs = [matrix, np.rot90(matrix)]


class ZTetris2(Tetris):
    """
    Shapes:
        0 1 1  1 0 0  0 0 0  0 1 0
        1 1 0  1 1 0  0 1 1  0 1 1
        0 0 0  0 1 0  1 1 0  0 0 1
    """

    matrix = np.zeros((3, 3), dtype=np.int)
    matrix[0, 1:] = 1
    matrix[1, :2] = 1
    matrixs = [matrix, np.rot90(matrix)]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-26 22:09:24
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-30 13:33:09
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

import logging
from typing import List
from dataclasses import dataclass

import numpy as np


@dataclass
class Result(object):
    index: int
    x: int
    y: int
    score: float
    priority: int


def _check_collision(matrix: np.ndarray) -> bool:
    return np.any(matrix > 1)


def _landing_height(current: np.ndarray, y: int) -> int:
    return 20 - y - np.argmax(np.any(current, axis=1))


def _eroded_piece_cells_metric(matrix: np.ndarray, current: np.ndarray,
                               y: int) -> int:
    score = 0
    cleared = np.all(matrix[2:-3, :], axis=1)
    cleared_num = sum(cleared)
    for index, line in enumerate(cleared):
        if line:
            score += sum(current[index - y])
    return score * cleared_num
    # return cleared_num


def _board_row_transitions(matrix: np.ndarray) -> int:
    score = 0
    for j in range(20):
        for i in range(11):
            if matrix[j + 2, i + 3] != matrix[j + 2, i + 2]:
                score += 1
    return score


def _board_column_transitions(matrix: np.ndarray) -> int:
    score = 0
    matrix_ = matrix.copy()
    matrix_[1, :] = 1
    for i in range(10):
        for j in range(21):
            if matrix[j + 2, i + 3] != matrix[j + 1, i + 3]:
                score += 1
    return score


def _board_buried_holes(matrix: np.ndarray) -> int:
    score = 0
    for i in range(10):
        column = matrix[:, i + 3]
        index = np.argmax(column)
        score += sum(column[index:] == 0)
    return score


def _board_wells(matrix: np.ndarray) -> int:
    score = 0
    for i in range(10):
        wells = 0
        for j in range(21):
            if matrix[j + 2, i +
                      3] == 0 and matrix[j + 2, i +
                                         2] == 1 and matrix[j + 2, i + 4] == 1:
                wells += 1
            else:
                score += wells * (wells + 1) // 2
                wells = 0
    return score


def pierre_dellacherie(matrix: np.ndarray,
                       current: List[np.ndarray]) -> List[Result]:
    """Pierre Dellacherie algorithm for tetris
    
    Improve:
        El-Tetris
        https://imake.ninja/el-tetris-an-improvement-on-pierre-dellacheries-algorithm/

    Args:
        matrix (np.ndarray): Matrix of the game
        current (np.ndarray): Shapes of the current tetris
    """
    results = []
    for index, shape in enumerate(current):
        for x in range(-1, 9):
            y = 0
            height, width = shape.shape
            new_matrix = matrix.copy()
            new_matrix[y + 2:y + height + 2, x + 3:x + width + 3] += shape
            while not _check_collision(new_matrix):
                y += 1
                new_matrix = matrix.copy()
                new_matrix[y + 2:y + height + 2, x + 3:x + width + 3] += shape
            y -= 1
            new_matrix = matrix.copy()
            new_matrix[y + 2:y + height + 2, x + 3:x + width + 3] += shape

            # 找到一个可摆放位置
            if y >= 0:
                # 计算评估参数
                # 方块海拔
                landing_height = _landing_height(shape, y)
                # 消除行数
                eroded_piece_cells_metric = _eroded_piece_cells_metric(
                    new_matrix, shape, y)
                # 行变换
                board_row_transitions = _board_row_transitions(new_matrix)
                # 列变换
                board_column_transitions = _board_column_transitions(new_matrix)
                # 空洞数
                board_buried_holes = _board_buried_holes(new_matrix)
                # 井深度
                board_wells = _board_wells(new_matrix)

                # 评估分数
                # Origin PD
                # score = (-landing_height + eroded_piece_cells_metric -
                #          board_row_transitions - board_column_transitions -
                #          4 * board_buried_holes - board_wells)
                # El-Tetris
                score = (-4.500158825082766 * landing_height +
                         3.4181268101392694 * eroded_piece_cells_metric -
                         3.2178882868487753 * board_row_transitions -
                         9.348695305445199 * board_column_transitions -
                         7.899265427351652 * board_buried_holes -
                         3.3855972247263626 * board_wells)
                # 计算优先级
                priority = 100 * abs((10 - width) // 2 - x) + index

                results.append(Result(index, x, y, score, priority))
                logging.debug(
                    f"\n[.] landing_height: {landing_height}"
                    f"\n[.] eroded_piece_cells_metric: {eroded_piece_cells_metric}"
                    f"\n[.] board_row_transitions: {board_row_transitions}"
                    f"\n[.] board_column_transitions: {board_column_transitions}"
                    f"\n[.] board_buried_holes: {board_buried_holes}"
                    f"\n[.] board_wells: {board_wells}")
                logging.debug(f"\n[i] x: {x}, y: {y}, index: {index}"
                              f"\n[i] score: {score},  priority: {priority}")
    return sorted(results, key=lambda x: (x.score, -x.priority), reverse=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    test = np.zeros((25, 16))
    test[:, :3] = 1
    test[:, -3:] = 1
    test[-6:, :] = 1
    test[-6:-3, 7] = 0
    test[-7, 4:10] = 1
    test[-8, [5, 6, 8, 9]] = 1
    test[-9, [6, 8]] = 1
    test[-10, 8] = 1
    print(test)
    tetris = np.ones((2, 2))
    current = [tetris]
    print(pierre_dellacherie(test, current))

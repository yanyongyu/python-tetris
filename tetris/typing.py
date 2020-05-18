#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-15 21:40:43
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-18 11:53:21
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from enum import Enum, auto


class Scene(Enum):
    HOME = auto()
    REFRESH = auto()
    GAME = auto()
    END = auto()

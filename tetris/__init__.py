#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-14 22:08:31
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-14 22:22:55
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

import pygame
import logging

from .game import Game

logging.basicConfig(level=logging.INFO)


def main():
    try:
        game = Game()
        game.start()
    except SystemExit:
        pass
    except Exception as e:
        logging.exception(e)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

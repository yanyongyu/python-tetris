#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2020-05-18 16:22:25
@LastEditors    : yanyongyu
@LastEditTime   : 2020-05-19 22:26:11
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

import os
import sqlite3


class Database:

    @staticmethod
    def connect():
        conn = sqlite3.connect(
            os.path.join(os.path.dirname(__file__), "tetris.db"))
        return conn

    @classmethod
    def restore_data(cls):
        conn = cls.connect()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tetris("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "best INTEGER DEFAULT 0,"
                       "last INTEGER DEFAULT 0,"
                       "sound INTEGER DEFAULT 1,"
                       "start_line INTEGER DEFAULT 0,"
                       "level INTEGER DEFAULT 1"
                       ")")
        cursor.close()
        conn.commit()

        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO tetris (id) VALUES (0)")
        cursor.close()
        conn.commit()

        cursor = conn.cursor()
        cursor.execute(
            "SELECT best, last, sound, start_line, level FROM tetris")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @classmethod
    def update_data(cls, **kwargs):
        conn = cls.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE tetris SET " + ", ".join(
            f"{key}={value}" for key, value in kwargs.items()) + " WHERE id=0")

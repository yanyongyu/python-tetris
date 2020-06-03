<!--
 * @Author         : yanyongyu
 * @Date           : 2020-05-14 22:26:04
 * @LastEditors    : yanyongyu
 * @LastEditTime   : 2020-06-03 22:38:12
 * @Description    : None
 * @GitHub         : https://github.com/yanyongyu
-->

# Tetris

![PyPI](https://img.shields.io/pypi/v/pytetris)
![GitHub](https://img.shields.io/github/license/yanyongyu/python-tetris)
![GitHub repo size](https://img.shields.io/github/repo-size/yanyongyu/python-tetris)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pytetris)

## Overview

Simple tetris game made by pygame

Inspired by [react-tetris](https://github.com/chvin/react-tetris)

AI algorithm: Pierre Dellacherie ([El-Tetris](https://imake.ninja/el-tetris-an-improvement-on-pierre-dellacheries-algorithm/))

## Screenshots

<img src="./static/overview1.png" alt="Overview" width="50%">

## Play the Game

### Start

```shell
python -m pytetris
```

or you can run the project in the project folder by

```shell
poetry run game
```

### How to Play

In the home page, you can use `←→` or click the button to change to start level and use `↑↓` to change the start random line number.

- `↑` : Rotate the piece
- `←→` : Move the piece left or right
- `↓` : Speed up the piece
- `SPACE` : Drop down the piece
- `P` : Pause the game
- `S` : Mute control
- `R` : Reset the game (will loss current score)
- `A` : Make AI on or off

## Pierre Dellacherie

Pierre Dellacherie is a one-piece algorithm.

Six main features:

### Landing Height

The height where the piece is put. Top or center of the piece is both ok.

Example:

⬜⬜⬜⬜⬜<font color="aqua">⬛</font>⬜⬜⬜⬜  
⬜⬜⬛⬛<font color="aqua">⬛</font><font color="aqua">⬛</font>⬛⬛⬜⬜  
⬛⬛⬛⬛<font color="aqua">⬛</font>⬛⬛⬛⬛⬛  
⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛

Height: `4` or `3`

### Eroded Piece Cells Metric

### Board Row Transitions

### Board Column Transitions

### Board Buried Holes

### Board Wells

## Project Development Setup

Clone the repository then install dependencies.

```shell
poetry install --no-root
```

or you can install the dependencies using pip:

```shell
pip3 install pygame numpy
```

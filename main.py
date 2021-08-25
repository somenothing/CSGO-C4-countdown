# -*- coding:utf-8 -*-
"""
author: somenothing
e-mail: w98987@126.com
2021/08/25
"""

import pygame

import keyboard

import sys
import os
import time

import win32api
import win32con
import win32gui
from ctypes import windll


pygame.init()  # 初始化pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = '1250, 20'  # 设置窗口位置
screen = pygame.display.set_mode((240, 80), pygame.NOFRAME)  # 设置窗口大小、无边框 pygame.NOFRAME
pygame.display.set_caption("my first pygame")  # 设置窗口标题

# 设置透明背景
fuchsia = (255, 255, 255)  # 自定义颜色
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)  # 创建分层窗口
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)  # 设置窗口透明度颜色

# 窗口置顶
SetWindowPos = windll.user32.SetWindowPos
NOSIZE = 1
NOMOVE = 2
TOPMOST = -1
NOT_TOPMOST = -2
def always_on_top(yes_or_not):
    """窗口置顶"""
    zorder = (NOT_TOPMOST, TOPMOST)[yes_or_not]  # 根据布尔值判断
    hwnd = pygame.display.get_wm_info()['window']  # 传到窗口
    SetWindowPos(hwnd, zorder, 0, 0, 0, 0, NOMOVE | NOSIZE)


def countdown():
    global statue, start
    statue = 1
    start = time.perf_counter()

def restart():
    global statue
    statue = 0


def main():
    global statue
    statue = 0
    while statue is not 1:
        '''闲置界面'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        always_on_top(True)  # 窗口置顶
        screen.fill(fuchsia)  # 透明背景

        # 设置文字
        font = pygame.font.SysFont('Microsoft YaHei', 30)
        text = font.render('press "z" to countdown!', True, (0, 0, 255), (0, 255, 0))
        screen.blit(text, (0, 0))

        # 监听键盘
        keyboard.add_hotkey('z', countdown)

        pygame.display.update()  # 更新界面


    while statue is 1:
        '''倒计时界面'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        always_on_top(True)  # 窗口置顶
        screen.fill(fuchsia)  # 透明背景

        # 设置文字
        font = pygame.font.SysFont('Microsoft YaHei', 30)
        now = time.perf_counter()
        t = int(40 - now + start) + 1
        if t <= 0:
            statue = 0
        text = font.render('C4 : %d  |  with kit : %d' % (t, t + 5), True, (255, 255, 0), (255, 0, 0))
        screen.blit(text, (0, 0))

        keyboard.add_hotkey('z', restart)

        pygame.display.update()  # 更新界面


if __name__ == '__main__':
    while True:
        main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==========================================================
# Python-Painting-Doraemon
# Original Author: dong
# GitHub: PerpetualSmile
#
# Funny Eyes + Blink Edition by Ravinder Ozha
# 保留原作风格 + 眨眼 + 搞笑滚动眼睛
# Preserve original style + blinking + funny rolling eyes
# ==========================================================

from turtle import *
import math
import random  # IMPORT ADDED FOR RANDOM BLINKING

# 无轨迹跳跃 / No trace jump
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()

# 眼睛 / Eyes (original shape)
def eyes():
    fillcolor("#ffffff")
    begin_fill()

    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()

# 胡须 / Beard
def beard():
    my_goto(-32, 135)
    seth(165)
    fd(60)

    my_goto(-32, 125)
    seth(180)
    fd(60)

    my_goto(-32, 115)
    seth(193)
    fd(60)

    my_goto(37, 135)
    seth(15)
    fd(60)

    my_goto(37, 125)
    seth(0)
    fd(60)

    my_goto(37, 115)
    seth(-13)
    fd(60)

# 嘴巴 / Mouth
def mouth():
    my_goto(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)

# 围巾 / Scarf
def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()

# 鼻子 / Nose
def nose():
    my_goto(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()

# 黑眼睛 / Black eyes (original - MODIFIED FOR ANIMATION)
def black_eyes():
    # This function is replaced by animated eyes
    # Keeping it for reference but not used
    pass

# 脸 / Face
def face():
    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    my_goto(63.56,218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)

# 头型 / Head
def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()

# 画哆啦A梦 / Draw Doraemon
def Doraemon():
    # 头部 / Head
    head()

    # 围脖 / Scarf
    scarf()

    # 脸 / Face
    face()

    # 红鼻子 / Red nose
    nose()

    # 嘴巴 / Mouth
    mouth()

    # 胡须 / Beard
    beard()

    # 身体 / Body
    my_goto(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)

    fillcolor('#00a0de')
    begin_fill()

    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)

    seth(100)
    circle(-1000, 9)

    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)

    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()

    # 左手 / Left hand
    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()

    # 脚 / Feet
    my_goto(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()

    my_goto(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()

    # 右手 / Right hand
    my_goto(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()

    # 口袋 / Pocket
    my_goto(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    my_goto(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)

    # 铃铛 / Bell
    my_goto(-103.42, 15.09)
    fd(90)
    seth(70)
    fillcolor('#ffd200')
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180-10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    my_goto(0, -150)

# 创建动画眼睛 / Create animated eyes
def create_animated_eyes():
    global left_pupil, right_pupil, left_highlight, right_highlight, left_eye_white, right_eye_white
    
    # 左眼白 / Left eye white
    left_eye_white = Turtle()
    left_eye_white.hideturtle()
    left_eye_white.penup()
    left_eye_white.goto(-20, 195)
    left_eye_white.color("white")
    left_eye_white.begin_fill()
    left_eye_white.circle(13)
    left_eye_white.end_fill()
    
    # 右眼白 / Right eye white
    right_eye_white = Turtle()
    right_eye_white.hideturtle()
    right_eye_white.penup()
    right_eye_white.goto(20, 195)
    right_eye_white.color("white")
    right_eye_white.begin_fill()
    right_eye_white.circle(13)
    right_eye_white.end_fill()
    
    # 左瞳孔 / Left pupil
    left_pupil = Turtle()
    left_pupil.shape("circle")
    left_pupil.color("black")
    left_pupil.penup()
    left_pupil.shapesize(0.9, 0.9)
    left_pupil.goto(-20, 195)
    
    # 右瞳孔 / Right pupil
    right_pupil = Turtle()
    right_pupil.shape("circle")
    right_pupil.color("black")
    right_pupil.penup()
    right_pupil.shapesize(0.9, 0.9)
    right_pupil.goto(20, 195)
    
    # 左高光 / Left highlight
    left_highlight = Turtle()
    left_highlight.shape("circle")
    left_highlight.color("white")
    left_highlight.penup()
    left_highlight.shapesize(0.3, 0.3)
    left_highlight.goto(-23, 198)
    
    # 右高光 / Right highlight
    right_highlight = Turtle()
    right_highlight.shape("circle")
    right_highlight.color("white")
    right_highlight.penup()
    right_highlight.shapesize(0.3, 0.3)
    right_highlight.goto(17, 198)
    
    return left_pupil, right_pupil, left_highlight, right_highlight

# 动画循环 / Animation loop
tick = 0
blink_timer = 0
is_blinking = False

def animate_eyes():
    global tick, blink_timer, is_blinking
    
    try:
        # 搞笑滚动眼睛 / Funny rolling eyes
        offset_x = math.sin(tick * 0.15) * 6
        offset_y = math.cos(tick * 0.2) * 4
        
        # 限制偏移范围在眼睛白内 / Limit offset within eye white
        offset_x = max(-8, min(8, offset_x))
        offset_y = max(-8, min(8, offset_y))
        
        # 随机眨眼 / Random blinking
        blink_timer += 1
        if not is_blinking and blink_timer > random.randint(60, 120):
            is_blinking = True
            blink_timer = 0
            
            # 眨眼效果 - 隐藏瞳孔 / Blink effect - hide pupils
            left_pupil.hideturtle()
            right_pupil.hideturtle()
            left_highlight.hideturtle()
            right_highlight.hideturtle()
            
            # 绘制眼睑线 / Draw eyelid lines
            lid = Turtle()
            lid.hideturtle()
            lid.penup()
            lid.pensize(3)
            lid.color("#00a0de")  # Doraemon's blue color
            lid.goto(-33, 203)
            lid.pendown()
            lid.forward(26)
            lid.penup()
            lid.goto(7, 203)
            lid.pendown()
            lid.forward(26)
            lid.penup()
            
            # 0.15秒后睁开 / Open eyes after 0.15 seconds
            ontimer(open_eyes, 150)
        
        if not is_blinking:
            left_pupil.showturtle()
            right_pupil.showturtle()
            left_highlight.showturtle()
            right_highlight.showturtle()
            
            # 移动瞳孔 / Move pupils
            left_pupil.goto(-20 + offset_x, 195 + offset_y)
            right_pupil.goto(20 + offset_x, 195 + offset_y)
            left_highlight.goto(-23 + offset_x * 0.5, 198 + offset_y * 0.5)
            right_highlight.goto(17 + offset_x * 0.5, 198 + offset_y * 0.5)
        
        tick += 1
        ontimer(animate_eyes, 50)  # 20 FPS
        
    except Exception as e:
        # Silently handle any errors during animation
        pass

def open_eyes():
    global is_blinking
    is_blinking = False
    left_pupil.showturtle()
    right_pupil.showturtle()
    left_highlight.showturtle()
    right_highlight.showturtle()

# 签名 / Signature with bilingual text
def add_signature():
    my_goto(100, -300)
    color('navy')
    write('by dongdong | modified by Ravinder Ozha', 
          font=("Bradley Hand ITC", 16, "bold"))
    
    # 添加中文说明 / Add Chinese description
    my_goto(-350, -320)
    color('darkblue')
    write('哆啦A梦 - 眨眼版 | Doraemon - Blinking Edition', 
          font=("SimHei", 14, "bold"))

# ==================== MAIN PROGRAM ====================
if __name__ == '__main__':
    # 屏幕设置 / Screen setup
    screensize(800, 600, "#f0f0f0")
    pensize(3)  # 画笔宽度 / Pen width
    speed(9)    # 画笔速度 / Pen speed
    tracer(0)   # 关闭自动刷新 / Turn off auto refresh
    
    # 画哆啦A梦 / Draw Doraemon
    Doraemon()
    
    # 创建动画眼睛 / Create animated eyes
    left_pupil, right_pupil, left_highlight, right_highlight = create_animated_eyes()
    
    # 添加双语签名 / Add bilingual signature
    add_signature()
    
    # 更新显示 / Update display
    update()
    
    # 启动动画 / Start animation
    animate_eyes()
    
    # 主循环 / Main loop
    mainloop()

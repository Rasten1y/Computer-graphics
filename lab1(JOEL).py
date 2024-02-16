#!/usr/bin/env python3

import glfw
from OpenGL.GL import *
from math import cos, sin, sqrt, asin

alpha = 0.0
beta = 0.0
pos_x = 0.0
pos_y = 0.0
fill = False

def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, "LAB 1", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

def display(window):
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)

    # move
    glMultMatrixf([1, 0, 0, 0,
                   0, 1, 0, 0,
                   0, 0, 1, 0,
                   0.75, 0.75, 0, 1])

    fz = 0
    theta = 0
    phi = 0
    def projection():
        glMultMatrixf([
            cos(phi), sin(phi)*sin(theta), sin(theta)*cos(theta), 0,
            0, cos(theta), -sin(theta), 0,
            sin(phi), -cos(phi)*sin(theta), -cos(phi)*cos(theta), 0,
            0, 0, 0, 1,
        ])
    projection()

    def cube(pos_x, pos_y):
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0);
        glVertex3f(-0.3+pos_x, 0+pos_y, 0)
        glVertex3f(0+pos_x, 0.3+pos_y, 0)
        glVertex3f(0.6+pos_x, 0.3+pos_y, 0)
        glVertex3f(0.9+pos_x, 0.03+pos_y, 0)
        glVertex3f(1.2+pos_x, 0.3+pos_y, 0)
        glVertex3f(1.2+pos_x, -0.3+pos_y, 0)
        glVertex3f(0.9+pos_x, -0.03+pos_y, 0)
        glVertex3f(0.6+pos_x, -0.3+pos_y, 0)
        glVertex3f(0+pos_x, -0.3+pos_y, 0)
        glEnd()
        

    glLoadIdentity()

    global alpha
    global beta
    x = 0.7
    y = 0.7
    fz = sqrt(x*x+y*y)
    theta = asin(fz/sqrt(2)) + alpha
    phi = asin(fz/sqrt(2-fz*fz)) + beta
    projection()

    cube(pos_x, pos_y)

    glfw.swap_buffers(window)
    glfw.poll_events()

def key_callback(window, key, scancode, action, mods):
    global alpha
    global beta
    global pos_x
    global pos_y
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_RIGHT:
            beta += 0.3
        elif key == glfw.KEY_LEFT:
            beta -= 0.3
        elif key == glfw.KEY_UP:
            alpha += 0.3
        elif key == glfw.KEY_DOWN:
            alpha -= 0.3
        elif key == glfw.KEY_W:
            pos_y += 0.15
        elif key == glfw.KEY_A:
            pos_x += 0.15
        elif key == glfw.KEY_S:
            pos_y -= 0.15
        elif key == glfw.KEY_D:
            pos_x -= 0.15



if __name__ == "__main__":
    main()

'''
A test object which defines a primitive shape for rendering
All primitive shapes must inherit from Displayable class
First version in 10/21/2018

:author: Alex Necakov
:version: 2021.9.29
'''
import os
import numpy as np
import string

try:
    import wx
    from wx import glcanvas
except ImportError:
    raise ImportError("Required dependency wxPython not present")

try:
    import OpenGL

    try:
        import OpenGL.GL as gl
        import OpenGL.GLU as glu
        import OpenGL.GLUT as glut  # this fails on OS X 11.x
    except ImportError:
        from ctypes import util

        orig_util_find_library = util.find_library


        def new_util_find_library(name):
            res = orig_util_find_library(name)
            if res:
                return res
            return '/System/Library/Frameworks/' + name + '.framework/' + name


        util.find_library = new_util_find_library
        import OpenGL.GL as gl
        import OpenGL.GLU as glu
        import OpenGL.GLUT as glut
except ImportError:
    raise ImportError("Required dependency PyOpenGL not present")

try:
    # From pip package "Pillow"
    from PIL import Image
except:
    print("Need to install PIL package. Pip package name is Pillow")
    raise ImportError

from Displayable import Displayable


class DisplayableSphere(Displayable):
    """
    Create a enclosed sphere whose one end is at z=0 and it grows along z coordinates
    """
    callListHandle = 0  # long int. override the one in Displayable
    qd = None  # Quadric
    scale = None
    edgeLength = 1
    _bufferData = None

    def __init__(self, parent, edgeLength, scale=None):
        super().__init__(parent)
        parent.context.SetCurrent(parent)
        self.edgeLength = edgeLength
        if scale is None:
            scale = [1, 1, 1]
        self.scale = scale

    def draw(self):
        gl.glCallList(self.callListHandle)

    def initialize(self):
        self.callListHandle = gl.glGenLists(1)
        self.qd = glu.gluNewQuadric()

        gl.glNewList(self.callListHandle, gl.GL_COMPILE)
        gl.glPushMatrix()

        gl.glScale(*self.scale)
        gl.glTranslate(0, 0, self.edgeLength / 2)

        glu.gluSphere(self.qd, self.edgeLength, 30, 30)

        gl.glPopMatrix()
        gl.glEndList()

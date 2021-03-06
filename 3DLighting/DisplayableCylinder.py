"""
Define displayable cube here. Current version only use VBO
First version in 10/20/2021

:author: micou(Zezhou Sun)
:version: 2021.1.1
"""

from Displayable import Displayable
from GLBuffer import VAO, VBO, EBO
import numpy as np
import ColorType
import math

try:
    import OpenGL

    try:
        import OpenGL.GL as gl
        import OpenGL.GLU as glu
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
except ImportError:
    raise ImportError("Required dependency PyOpenGL not present")


class DisplayableCylinder(Displayable):
    vao = None
    vbo = None
    ebo = None
    shaderProg = None

    vertices = None  # array to store vertices information
    indices = None  # stores triangle indices to vertices

    # stores current cube's information, read-only
    radius = None
    height = None
    slices = None
    color = None

    def __init__(self, shaderProg, radius=1, height = 1, slices=36, color=ColorType.BLUE):
        super(DisplayableCylinder, self).__init__()
        self.shaderProg = shaderProg
        self.shaderProg.use()

        self.vao = VAO()
        self.vbo = VBO()  # vbo can only be initiate with glProgram activated
        self.ebo = EBO()

        self.generate(radius, height, slices, color)

    def generate(self, radius=1, height = 1, slices=36, color=None):
        self.radius = radius
        self.height = height
        self.slices = slices
        self.color = color
        pi = math.pi

        self.vertices = np.zeros([4*(slices) + 6*slices, 11])
        self.vtxCoordTop = np.zeros([slices+1,3])
        self.vtxCoordBot = np.zeros([slices+1,3])
        self.indices = np.zeros([4*slices,3])
        self.vtxCoordTop[slices,:] = [0,0,height]
        self.vtxCoordBot[slices,:] = [0,0,0]
        for i in range(slices):
            theta = i / (slices) * 2 * pi
            self.vtxCoordTop[i,:] = [self.radius * math.cos(theta),
                                    self.radius * math.sin(theta),
                                    height]
            self.vtxCoordBot[i,:] = [self.radius * math.cos(theta),
                                    self.radius * math.sin(theta),
                                    0]
        #tube
        for i in range(slices):
            theta = i / (slices) * 2 * pi
            self.vertices[4*i+0, 0:3] = self.vtxCoordTop[(i+0)%slices,:]
            self.vertices[4*i+1, 0:3] = self.vtxCoordTop[(i+1)%slices,:]
            self.vertices[4*i+2, 0:3] = self.vtxCoordBot[(i+0)%slices,:]
            self.vertices[4*i+3, 0:3] = self.vtxCoordBot[(i+1)%slices,:]

            self.vertices[4*i+0, 3:6] = [math.cos(theta), math.sin(theta), 0]
            self.vertices[4*i+1, 3:6] = [math.cos(theta), math.sin(theta), 0]
            self.vertices[4*i+2, 3:6] = [math.cos(theta), math.sin(theta), 0]
            self.vertices[4*i+3, 3:6] = [math.cos(theta), math.sin(theta), 0]

            self.vertices[4*i+0, 6:9] = [*color]
            self.vertices[4*i+1, 6:9] = [*color]
            self.vertices[4*i+2, 6:9] = [*color]
            self.vertices[4*i+3, 6:9] = [*color]

            self.indices[2*i+0] = [4*i+0,4*i+1,4*i+2]
            self.indices[2*i+1] = [4*i+1,4*i+2,4*i+3]
        #caps
        for i in range(slices):
            self.vertices[6*i+0+(4*slices), 0:3] = self.vtxCoordTop[(i+0)%slices,:]
            self.vertices[6*i+1+(4*slices), 0:3] = self.vtxCoordTop[(i+1)%slices,:]
            self.vertices[6*i+2+(4*slices), 0:3] = self.vtxCoordTop[slices,:]
            
            self.vertices[6*i+3+(4*slices), 0:3] = self.vtxCoordBot[(i+0)%slices,:]
            self.vertices[6*i+4+(4*slices), 0:3] = self.vtxCoordBot[(i+1)%slices,:]
            self.vertices[6*i+5+(4*slices), 0:3] = self.vtxCoordBot[slices,:]

            self.vertices[6*i+0+(4*slices), 3:6] = [0, 0, 1]
            self.vertices[6*i+1+(4*slices), 3:6] = [0, 0, 1]
            self.vertices[6*i+2+(4*slices), 3:6] = [0, 0, 1]

            self.vertices[6*i+3+(4*slices), 3:6] = [0, 0, -1]
            self.vertices[6*i+4+(4*slices), 3:6] = [0, 0, -1]
            self.vertices[6*i+5+(4*slices), 3:6] = [0, 0, -1]

            self.vertices[6*i+0+(4*slices), 6:9] = [*color]
            self.vertices[6*i+1+(4*slices), 6:9] = [*color]
            self.vertices[6*i+2+(4*slices), 6:9] = [*color]

            self.vertices[6*i+3+(4*slices), 6:9] = [*color]
            self.vertices[6*i+4+(4*slices), 6:9] = [*color]
            self.vertices[6*i+5+(4*slices), 6:9] = [*color]

            self.indices[2*i+0+(2*slices)] = [6*i+0+(4*slices),6*i+1+(4*slices),6*i+2+(4*slices)]
            self.indices[2*i+1+(2*slices)] = [6*i+3+(4*slices),6*i+4+(4*slices),6*i+5+(4*slices)]
            

    def draw(self):
        self.vao.bind()
        # TODO 1.1 is at here, switch from vbo to ebo
        self.ebo.draw()
        self.vao.unbind()

    def initialize(self):
        """
        Remember to bind VAO before this initialization. If VAO is not bind, program might throw an error
        in systems that don't enable a default VAO after GLProgram compilation
        """
        self.vao.bind()
        self.vbo.setBuffer(self.vertices, 11)
        self.ebo.setBuffer(self.indices)

        self.vbo.setAttribPointer(self.shaderProg.getAttribLocation("vertexPos"),
                                  stride=11, offset=0, attribSize=3)
        self.vbo.setAttribPointer(self.shaderProg.getAttribLocation("vertexNormal"),
                                  stride=11, offset=3, attribSize=3)
        self.vbo.setAttribPointer(self.shaderProg.getAttribLocation("vertexColor"),
                                  stride=11, offset=6, attribSize=3)
        # TODO/BONUS 6.1 is at here, you need to set attribPointer for texture coordinates
        # you should check the corresponding variable name in GLProgram and set the pointer
        self.vao.unbind()


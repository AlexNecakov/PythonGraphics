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


class DisplayableSphere(Displayable):
    vao = None
    vbo = None
    ebo = None
    shaderProg = None

    vertices = None  # array to store vertices information
    indices = None  # stores triangle indices to vertices

    # stores current cube's information, read-only
    radius = None
    stacks = None
    slices = None
    color = None

    def __init__(self, shaderProg, radius=1, stacks=18, slices=36, color=ColorType.BLUE):
        super(DisplayableSphere, self).__init__()
        self.shaderProg = shaderProg
        self.shaderProg.use()

        self.vao = VAO()
        self.vbo = VBO()  # vbo can only be initiate with glProgram activated
        self.ebo = EBO()

        self.generate(radius, stacks, slices, color)

    def generate(self, radius=1, stacks=18, slices=36, color=None):
        self.radius = radius
        self.stacks = stacks
        self.slices = slices
        self.color = color
        pi = math.pi

        self.vertices = np.zeros([6*(slices)*(stacks-1), 11])
        self.vtxCoord = np.zeros([stacks,slices,3])
        for i in range(stacks):
            phi = i / (stacks - 1) * pi - pi/2
            for j in range(slices):
                theta = j / (slices) * 2 * pi
                self.vtxCoord[i,j,:] = [self.radius * math.cos(phi) * math.cos(theta),
                                        self.radius * math.cos(phi) * math.sin(theta),
                                        self.radius * math.sin(phi)]
        
        for i in range(stacks-1):
            for j in range(slices):
                gridN = i * slices + j
                self.vertices[6*gridN+0, 0:3] = self.vtxCoord[i,j,:]
                self.vertices[6*gridN+1, 0:3] = self.vtxCoord[i,(j+1)% slices,:]
                self.vertices[6*gridN+2, 0:3] = self.vtxCoord[i+1,(j+1)% slices,:]
                
                self.vertices[6*gridN+3, 0:3] = self.vtxCoord[i,j,:]
                self.vertices[6*gridN+4, 0:3] = self.vtxCoord[i+1,(j+1)% slices,:]
                self.vertices[6*gridN+5, 0:3] = self.vtxCoord[i+1,j,:]

                self.vertices[6*gridN+0:6*gridN+6, 6:9] = [*color]
                self.vertices[6*gridN+2, 6:9] = [*color]
                self.vertices[6*gridN+5, 6:9] = [*color]
        
        self.indices = np.array([
            [0,1,2],
            [0,2,3],

            [4,5,6],
            [4,6,7],
            
            [8,9,10],
            [8,10,11],

            [12,13,14],
            [12,14,15],

            [16,17,18],
            [16,18,19],

            [20,21,22],
            [20,22,23]
        ])

    def draw(self):
        self.vao.bind()
        # TODO 1.1 is at here, switch from vbo to ebo
        self.vbo.draw()
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


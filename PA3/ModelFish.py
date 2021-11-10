"""
Model our creature and wrap it in one class
First version at 09/28/2021

:author: micou(Zezhou Sun)
:version: 2021.2.1
"""
import random

from Component import Component
from Point import Point
import ColorType as Ct
from Displayable import Displayable
from Animation import Animation
from EnvironmentObject import EnvironmentObject
from Vivarium import Tank

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


class ModelFish(Component):
    """
    Define our fish model
    """

    components = None
    contextParent = None

    def __init__(self, parent, position, color, linkageLength=0.5, display_obj=None):
        super().__init__(position, display_obj)
        self.components = []
        self.contextParent = parent

        body = Component(Point((0, 0, 0)),
            DisplayableSphere(self.contextParent, 1, [linkageLength,linkageLength/2,linkageLength]))
        body.setDefaultColor(color)
        tailUpper = Component(Point((linkageLength/4, 0, 0)),
            DisplayableSphere(self.contextParent, 1, [linkageLength/2,linkageLength/4,linkageLength]))
        tailUpper.setDefaultColor(color)
        tailUpper.setDefaultAngle(tailUpper.vAxis, -120)
        tailLower = Component(Point((linkageLength/4, 0, 0)),
            DisplayableSphere(self.contextParent, 1, [linkageLength/2,linkageLength/4,linkageLength]))
        tailLower.setDefaultColor(color)
        tailLower.setDefaultAngle(tailLower.vAxis, 120)
        

        self.addChild(body)
        body.addChild(tailUpper)
        body.addChild(tailLower)

        self.components = [body, tailUpper, tailLower]

class DisplayableSphere(Displayable):
    """
    Create a enclosed cylinder whose one end is at z=0 and it grows along z coordinates
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

        # v_l = [
        #     [-self.edgeLength / 2, -self.edgeLength / 2, -self.edgeLength / 2],
        #     [self.edgeLength / 2, -self.edgeLength / 2, -self.edgeLength / 2],
        #     [self.edgeLength / 2, self.edgeLength / 2, -self.edgeLength / 2],
        #     [- self.edgeLength / 2, self.edgeLength / 2, -self.edgeLength / 2],
        #     [- self.edgeLength / 2, -self.edgeLength / 2, self.edgeLength / 2],
        #     [self.edgeLength / 2, -self.edgeLength / 2, self.edgeLength / 2],
        #     [self.edgeLength / 2, self.edgeLength / 2, self.edgeLength / 2],
        #     [- self.edgeLength / 2, self.edgeLength / 2, self.edgeLength / 2],
        # ]

        gl.glNewList(self.callListHandle, gl.GL_COMPILE)
        gl.glPushMatrix()

        gl.glScale(*self.scale)
        gl.glTranslate(0, 0, self.edgeLength / 2)

        glu.gluSphere(self.qd,1.0,30,30)
        # a primitive cube
        # gl.glBegin(gl.GL_QUADS)
        # gl.glVertex3f(*v_l[1])
        # gl.glVertex3f(*v_l[0])
        # gl.glVertex3f(*v_l[3])
        # gl.glVertex3f(*v_l[2])

        # gl.glVertex3f(*v_l[4])
        # gl.glVertex3f(*v_l[5])
        # gl.glVertex3f(*v_l[6])
        # gl.glVertex3f(*v_l[7])

        # gl.glVertex3f(*v_l[0])
        # gl.glVertex3f(*v_l[4])
        # gl.glVertex3f(*v_l[7])
        # gl.glVertex3f(*v_l[3])

        # gl.glVertex3f(*v_l[7])
        # gl.glVertex3f(*v_l[6])
        # gl.glVertex3f(*v_l[2])
        # gl.glVertex3f(*v_l[3])

        # gl.glVertex3f(*v_l[5])
        # gl.glVertex3f(*v_l[1])
        # gl.glVertex3f(*v_l[2])
        # gl.glVertex3f(*v_l[6])

        # gl.glVertex3f(*v_l[0])
        # gl.glVertex3f(*v_l[1])
        # gl.glVertex3f(*v_l[5])
        # gl.glVertex3f(*v_l[4])

        # gl.glEnd()

        gl.glPopMatrix()
        gl.glEndList()

class DisplayableCube(Displayable):
    """
    Create a enclosed cylinder whose one end is at z=0 and it grows along z coordinates
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

        v_l = [
            [-self.edgeLength / 2, -self.edgeLength / 2, -self.edgeLength / 2],
            [self.edgeLength / 2, -self.edgeLength / 2, -self.edgeLength / 2],
            [self.edgeLength / 2, self.edgeLength / 2, -self.edgeLength / 2],
            [- self.edgeLength / 2, self.edgeLength / 2, -self.edgeLength / 2],
            [- self.edgeLength / 2, -self.edgeLength / 2, self.edgeLength / 2],
            [self.edgeLength / 2, -self.edgeLength / 2, self.edgeLength / 2],
            [self.edgeLength / 2, self.edgeLength / 2, self.edgeLength / 2],
            [- self.edgeLength / 2, self.edgeLength / 2, self.edgeLength / 2],
        ]

        gl.glNewList(self.callListHandle, gl.GL_COMPILE)
        gl.glPushMatrix()

        gl.glScale(*self.scale)
        gl.glTranslate(0, 0, self.edgeLength / 2)

        # a primitive cube
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex3f(*v_l[1])
        gl.glVertex3f(*v_l[0])
        gl.glVertex3f(*v_l[3])
        gl.glVertex3f(*v_l[2])

        gl.glVertex3f(*v_l[4])
        gl.glVertex3f(*v_l[5])
        gl.glVertex3f(*v_l[6])
        gl.glVertex3f(*v_l[7])

        gl.glVertex3f(*v_l[0])
        gl.glVertex3f(*v_l[4])
        gl.glVertex3f(*v_l[7])
        gl.glVertex3f(*v_l[3])

        gl.glVertex3f(*v_l[7])
        gl.glVertex3f(*v_l[6])
        gl.glVertex3f(*v_l[2])
        gl.glVertex3f(*v_l[3])

        gl.glVertex3f(*v_l[5])
        gl.glVertex3f(*v_l[1])
        gl.glVertex3f(*v_l[2])
        gl.glVertex3f(*v_l[6])

        gl.glVertex3f(*v_l[0])
        gl.glVertex3f(*v_l[1])
        gl.glVertex3f(*v_l[5])
        gl.glVertex3f(*v_l[4])

        gl.glEnd()

        gl.glPopMatrix()
        gl.glEndList()

class Fish(Component, Animation, EnvironmentObject):
    """
    A Linkage with animation enabled and is defined as an object in environment
    """
    components = None
    contextParent = None
    rotation_speed = None
    translation_speed = None

    def __init__(self, parent, position,color):
        super(Fish, self).__init__(position)
        base = ModelFish(parent, Point((0, 0, 0)), color, .1)

        self.components = base.components
        self.contextParent = parent
        
        self.addChild(base)

        self.rotation_speed = []
        
        self.rotation_speed.append([0, 0, 0])

        self.components[1].setRotateExtent(self.components[1].uAxis, -40, 40)
        self.components[1].setRotateExtent(self.components[1].vAxis, -125, -115)
        self.components[1].setRotateExtent(self.components[1].wAxis, -5, 5)
        self.rotation_speed.append([1, 0, 0])

        self.components[2].setRotateExtent(self.components[2].uAxis, -40, 40)
        self.components[2].setRotateExtent(self.components[2].vAxis, 115, 125)
        self.components[2].setRotateExtent(self.components[2].wAxis, -5, 5)
        self.rotation_speed.append([1, 0, 0])

        self.translation_speed = Point([random.random()-0.5 for _ in range(3)]).normalize() * 0.05
        self.bound_center = Point((0, 0, 0))
        self.bound_radius = .1
        self.species_id = 1

    def animationUpdate(self):
        # animation cycle
        for i, comp in enumerate(self.components):
            comp.rotate(self.rotation_speed[i][0], comp.uAxis)
            comp.rotate(self.rotation_speed[i][1], comp.vAxis)
            comp.rotate(self.rotation_speed[i][2], comp.wAxis)
            if comp.uAngle in comp.uRange:  # rotation reached the limit
                self.rotation_speed[i][0] *= -1
            if comp.vAngle in comp.vRange:
                self.rotation_speed[i][1] *= -1
            if comp.wAngle in comp.wRange:
                self.rotation_speed[i][2] *= -1

        position = self.current_position
        coords = position.coords
        x = coords[0]
        y = coords[1]
        z = coords[2]
        
        # other object collision / influence
        for i, envObj in enumerate(self.env_obj_list):
            envPos = envObj.current_position
            envCoords = envPos.coords
            envX = envCoords[0]
            envY = envCoords[1]
            envZ = envCoords[2]
            if ((position.dist(envPos) < self.bound_radius + envObj.bound_radius) & (position.dist(envPos) > 0)):
                if(envObj.species_id == self.species_id):
                    self.translation_speed.setCoords((-self.translation_speed[0],-self.translation_speed[1],-self.translation_speed[2]))
                elif(envObj.species_id > self.species_id):
                    self.deleteFlag = True
            if(envObj.species_id > self.species_id):
                newX = 1/(((x - envX)**2)+0.0000001)
                newY = 1/(((y - envY)**2)+0.0000001)
                newZ = 1/(((z - envZ)**2)+0.0000001)
                self.translation_speed.setCoords((newX+random.random()-0.5, newY+random.random()-0.5, newZ+random.random()-0.5))
                self.translation_speed = self.translation_speed.normalize()* 0.05
        
        # tank wall collision
        if abs(x) + self.bound_radius >= 2:
            self.translation_speed.setCoords((-self.translation_speed[0]*4,self.translation_speed[1],self.translation_speed[2]))
            self.translation_speed = self.translation_speed.normalize()* 0.05
            # if(x >= 2):
            #     x -= self.bound_radius
            # if(x <= -2):
            #     x += self.bound_radius
        if abs(y) + self.bound_radius >= 2:
            self.translation_speed.setCoords((self.translation_speed[0],-self.translation_speed[1]*4,self.translation_speed[2]))
            self.translation_speed = self.translation_speed.normalize()* 0.05
            # if(y >= 2):
            #     y -= self.bound_radius
            # if(y <= -2):
            #     y += self.bound_radius
        if abs(z) + self.bound_radius >= 2:
            self.translation_speed.setCoords((self.translation_speed[0],self.translation_speed[1],-self.translation_speed[2]*4))
            self.translation_speed = self.translation_speed.normalize()* 0.05
            # if(z >= 2):
            #     z -= self.bound_radius
            # if(z <= -2):
            #     z += self.bound_radius
                 
        x += self.translation_speed[0]
        y += self.translation_speed[1]
        z += self.translation_speed[2]

        self.setCurrentPosition(Point((x,y,z)))

        ##### TODO 4: Eyes on the road!
        # Requirements:
        #   1. Creatures should face in the direction they are moving. For instance, a fish should be facing the
        #   direction in which it swims. Remember that we require your creatures to be movable in 3 dimensions,
        #   so they should be able to face any direction in 3D space.


        self.update()

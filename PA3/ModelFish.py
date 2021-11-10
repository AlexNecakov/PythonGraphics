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

##### TODO 1: Construct your two different creatures
# Requirements:
#   1. For the basic parts of your creatures, feel free to use routines provided with the previous assignment.
#   You are also free to create your own basic parts, but they must be polyhedral (solid).
#   2. The creatures you design should have moving linkages of the basic parts: legs, arms, wings, antennae,
#   fins, tentacles, etc.
#   3. Model requirements:
#         1. Predator: At least one (1) creature. Should have at least two moving parts in addition to the main body
#         2. Prey: At least two (2) creatures. The two prey can be instances of the same design. Should have at
#         least one moving part.
#         3. The predator and prey should have distinguishable different colors.
#         4. You are welcome to reuse your PA2 creature in this assignment.

class Fish(Component, Animation, EnvironmentObject):
    """
    A Linkage with animation enabled and is defined as an object in environment
    """
    components = None
    rotation_speed = None
    translation_speed = None

    def __init__(self, parent, position,color):
        super(Fish, self).__init__(position)
        base = ModelFish(parent, Point((0, 0, 0)), color, .75)

        self.components = base.components
        
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

        self.translation_speed = Point([random.random()-0.5 for _ in range(3)]).normalize() * 0.01
        self.bound_center = Point((0, 0, 0))
        self.bound_radius = 0.1 * 4
        self.species_id = 1

    def animationUpdate(self):
        ##### TODO 2: Animate your creature!
        # Requirements:
        #   1. Set reasonable joints limit for your creature
        #   2. The linkages should move back and forth in a periodic motion, as the creatures move about the vivarium.
        #   3. Your creatures should be able to move in 3 dimensions, not only on a plane.
        # create period animation for creature joints
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

        position = self.components[0].current_position
        coords = position.coords
        x = coords[0]
        y = coords[1]
        z = coords[2]
        
        x += self.translation_speed[0]
        y += self.translation_speed[1]
        z += self.translation_speed[2]

        

        self.components[0].setCurrentPosition(Point((x,y,z)))

        ##### TODO 3: Interact with the environment
        # Requirements:
        #   1. Your creatures should always stay within the fixed size 3D "tank". You should do collision detection
        #   between it and tank walls. When it hits with tank walls, it should turn and change direction to stay
        #   within the tank.
        #   2. Your creatures should have a prey/predator relationship. For example, you could have a bug being chased
        #   by a spider, or a fish eluding a shark. This means your creature should react to other creatures in the tank
        #       1. Use potential functions to change its direction based on other creatures’ location, their
        #       inter-creature distances, and their current configuration.
        #       2. You should detect collisions between creatures.
        #           1. Predator-prey collision: The prey should disappear (get eaten) from the tank.
        #           2. Collision between the same species: They should bounce apart from each other. You can use a
        #           reflection vector about a plane to decide the after-collision direction.
        #       3. You are welcome to use bounding spheres for collision detection.
        


        ##### TODO 4: Eyes on the road!
        # Requirements:
        #   1. CCreatures should face in the direction they are moving. For instance, a fish should be facing the
        #   direction in which it swims. Remember that we require your creatures to be movable in 3 dimensions,
        #   so they should be able to face any direction in 3D space.


        self.update()

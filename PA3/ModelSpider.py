"""
Model our creature and wrap it in one class
First version at 09/28/2021

:author: Alex Necakov
:version: 2021.10.6
"""

from Component import Component
from Point import Point
import ColorType as Ct
from DisplayableCube import DisplayableCube
from DisplayableCylinder import DisplayableCylinder
from DisplayableSphere import DisplayableSphere
from ModelLeg import ModelLeg
from Animation import Animation
from EnvironmentObject import EnvironmentObject
from Vivarium import Tank


class ModelSpider(Component):
    """
    Define our spider model
    """

    components = None
    contextParent = None

    def __init__(self, parent, position, color, linkageLength=0.5, display_obj=None):
        super().__init__(position, display_obj)
        self.components = []
        self.contextParent = parent

        thoraxLength = 0.5
        legHeight = thoraxLength/2

        #rotation limits not really needed on parent component
        thoraxMinUAngle = -180
        thoraxMaxUAngle = 180
        thoraxMinVAngle = -180
        thoraxMaxVAngle = 180
        thoraxMinWAngle = -180
        thoraxMaxWAngle = 180
        
        abdomenMinUAngle = -20
        abdomenMaxUAngle = 20
        abdomenMinVAngle = -5
        abdomenMaxVAngle = 5
        abdomenMinWAngle = -10
        abdomenMaxWAngle = 30

        mandLegPos = -thoraxLength/2
        mandLegAngle = -60
        mandLegMinUAngle = -30
        secondLegPos = 0
        secondLegAngle = -30
        thirdLegPos = 0
        thirdLegAngle = 20
        hindLegPos = thoraxLength/2
        hindLegAngle = 50

        thorax = Component(Point((0, 0, 0)), DisplayableSphere(self.contextParent, 1, [2*thoraxLength, thoraxLength, thoraxLength]))
        thorax.setDefaultColor(Ct.NAVY)
        thorax.setRotateExtent(thorax.uAxis, thoraxMinUAngle, thoraxMaxUAngle)
        thorax.setRotateExtent(thorax.vAxis, thoraxMinVAngle, thoraxMaxVAngle)
        thorax.setRotateExtent(thorax.wAxis, thoraxMinWAngle, thoraxMaxWAngle)

        abdomen = Component(Point((thoraxLength*2.5, 0, 0)), DisplayableSphere(self.contextParent, 1, [thoraxLength*1.75, thoraxLength, thoraxLength]))
        abdomen.setDefaultAngle(15, abdomen.wAxis)
        abdomen.setDefaultColor(Ct.NAVY)
        abdomen.setRotateExtent(abdomen.uAxis, abdomenMinUAngle, abdomenMaxUAngle)
        abdomen.setRotateExtent(abdomen.vAxis, abdomenMinVAngle, abdomenMaxVAngle)
        abdomen.setRotateExtent(abdomen.wAxis, abdomenMinWAngle, abdomenMaxWAngle)
        
        legMandL = ModelLeg(self.contextParent, Point((mandLegPos, 0, legHeight)))
        legMandL.setDefaultAngle(mandLegAngle, legMandL.vAxis)
        legMandR = ModelLeg(self.contextParent, Point((mandLegPos, 0, legHeight)))
        #do this for mirrored control
        #user can't change actual leg comp position, just the subcomponents so this will work properly
        legMandR.setDefaultScale([-1,-1,-1])
        legMandR.setDefaultAngle(180, legMandR.uAxis)
        legMandR.setDefaultAngle(180+mandLegAngle, legMandR.vAxis)
        
        legSecondL = ModelLeg(self.contextParent, Point((secondLegPos, 0, legHeight)))
        legSecondL.setDefaultAngle(secondLegAngle, legSecondL.vAxis)
        legSecondR = ModelLeg(self.contextParent, Point((secondLegPos, 0, legHeight)))
        legSecondR.setDefaultScale([-1,-1,-1])
        legSecondR.setDefaultAngle(180, legSecondR.uAxis)
        legSecondR.setDefaultAngle(180+secondLegAngle, legSecondR.vAxis)
        
        legThirdL = ModelLeg(self.contextParent, Point((thirdLegPos, 0, legHeight)))
        legThirdL.setDefaultAngle(thirdLegAngle, legThirdL.vAxis)
        legThirdR = ModelLeg(self.contextParent, Point((thirdLegPos, 0, legHeight)))
        legThirdR.setDefaultScale([-1,-1,-1])
        legThirdR.setDefaultAngle(180, legThirdR.uAxis)
        legThirdR.setDefaultAngle(180+thirdLegAngle, legThirdR.vAxis)
        
        legHindL = ModelLeg(self.contextParent, Point((hindLegPos, 0, legHeight)))
        legHindL.setDefaultAngle(hindLegAngle, legHindL.vAxis)
        legHindR = ModelLeg(self.contextParent, Point((hindLegPos, 0, legHeight)))
        legHindR.setDefaultScale([-1,-1,-1])
        legHindR.setDefaultAngle(180, legHindR.uAxis)
        legHindR.setDefaultAngle(180+hindLegAngle, legHindR.vAxis)

        self.addChild(thorax)
        thorax.addChild(abdomen)
        thorax.addChild(legMandL)
        thorax.addChild(legMandR)
        thorax.addChild(legSecondL)
        thorax.addChild(legSecondR)
        thorax.addChild(legThirdL)
        thorax.addChild(legThirdR)
        thorax.addChild(legHindL)
        thorax.addChild(legHindR)

        self.components = [thorax, abdomen, 
        legMandL.components[0], legMandL.components[1], legMandL.components[2],
        legMandR.components[0], legMandR.components[1], legMandR.components[2],
        legSecondL.components[0], legSecondL.components[1], legSecondL.components[2],
        legSecondR.components[0], legSecondR.components[1], legSecondR.components[2],
        legThirdL.components[0], legThirdL.components[1], legThirdL.components[2],
        legThirdR.components[0], legThirdR.components[1], legThirdR.components[2],
        legHindL.components[0], legHindL.components[1], legHindL.components[2],
        legHindR.components[0], legHindR.components[1], legHindR.components[2]]

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

class Spider(Component, Animation, EnvironmentObject):
    """
    A Linkage with animation enabled and is defined as an object in environment
    """
    components = None
    rotation_speed = None
    translation_speed = None

    def __init__(self, parent, position,color):
        super(Spider, self).__init__(position)
        main = ModelSpider(parent, Point((0, 0, 0)),color, 0.1)
        # arm2 = ModelLinkage(parent, Point((0, 0, 0)), 0.1)
        # arm2.setDefaultAngle(arm2.vAxis, 120)
        # arm3 = ModelLinkage(parent, Point((0, 0, 0)), 0.1)
        # arm3.setDefaultAngle(arm3.vAxis, 240)

        self.components = main.components

        self.addChild(arm1)
        
        # self.rotation_speed = []
        #     self.rotation_speed.append([1, 0, 0])

        # self.translation_speed = Point([random.random()-0.5 for _ in range(3)]).normalize() * 0.01

        self.bound_center = Point((0, 0, 0))
        self.bound_radius = 0.1 * 4
        self.species_id = 1

    def animationUpdate(self):
        ##### TODO 2: Animate your creature!
        # Requirements:
        #   1. Set reasonable joints limit for your creature
        #   2. The linkages should move back and forth in a periodic motion, as the creatures move about the vivarium.
        #   3. Your creatures should be able to move in 3 dimensions, not only on a plane.
        for comp in self.components:
            comp.uAngle+=5
        # create period animation for creature joints
        # for i, comp in enumerate(self.components):
        #     comp.rotate(self.rotation_speed[i][0], comp.uAxis)
        #     comp.rotate(self.rotation_speed[i][1], comp.vAxis)
        #     comp.rotate(self.rotation_speed[i][2], comp.wAxis)
        #     if comp.uAngle in comp.uRange:  # rotation reached the limit
        #         self.rotation_speed[i][0] *= -1
        #     if comp.vAngle in comp.vRange:
        #         self.rotation_speed[i][1] *= -1
        #     if comp.wAngle in comp.wRange:
        #         self.rotation_speed[i][2] *= -1
        # self.vAngle = (self.vAngle + 5) % 360

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

        ##### BONUS 6: Group behaviors
        # Requirements:
        #   1. Add at least 5 creatures to the vivarium and make it possible for creatures to engage in group behaviors,
        #   for instance flocking together. This can be achieved by implementing the
        #   [Boids animation algorithms](http://www.red3d.com/cwr/boids/) of Craig Reynolds.

        self.update()

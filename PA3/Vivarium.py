"""
All creatures should be added to Vivarium. Some help functions to add/remove creature are defined here.
Created on 20181028

:author: micou(Zezhou Sun)
:version: 2021.1.1
"""
import random


from Point import Point
from Component import Component
from Animation import Animation
from ModelTank import Tank
from ModelLinkage import Linkage
from ModelEgg import Egg
from ModelSpider import Spider
import ColorType as Ct
from EnvironmentObject import EnvironmentObject


class Vivarium(Component, Animation):
    """
    The Vivarium for our animation
    """
    components = None  # List
    parent = None  # class that have current context
    tank = None
    tank_dimensions = None

    ##### BONUS 5(TODO 5 for CS680 Students): Feed your creature
    # Requirements:
    #   Add chunks of food to the vivarium which can be eaten by your creatures.
    #     * When ‘f’ is pressed, have a food particle be generated at random within the vivarium.
    #     * Be sure to draw the food on the screen with an additional model. It should drop slowly to the bottom of
    #     the vivarium and remain there within the tank until eaten.
    #     * The food should disappear once it has been eaten. Food is eaten by the first creature that touches it.

    def __init__(self, parent):
        self.parent = parent

        self.tank_dimensions = [4, 4, 4]
        tank = Tank(parent, self.tank_dimensions)
        super(Vivarium, self).__init__(Point((0, 0, 0)))

        # Build relationship
        self.addChild(tank)
        self.tank = tank

        # Store all components in one list, for us to access them later
        self.components = [tank]

        # self.addNewObjInTank(Linkage(parent, Point((0, 0, 0))))
        self.addNewObjInTank(Egg(parent, Point((0.8, 0, 0)),Ct.YELLOW))
        self.addNewObjInTank(Egg(parent, Point((-0.8, 0, 0)),Ct.PINK))
        self.addNewObjInTank(Spider(parent, Point((-0.8, 0, 0)),Ct.PINK))

    def animationUpdate(self):
        """
        Update all creatures in vivarium
        """
        for c in self.components[::-1]:
            if isinstance(c, Animation):
                c.animationUpdate()

        for idx,c in enumerate(self.components[1:]):
            position = c.current_position
            coords = position.coords
            x = coords[0]
            y = coords[1]
            z = coords[2]

            if(idx%2==0): 
                x+=0.01
            else:
                x-=0.01

            c.setCurrentPosition(Point((x,y,z)))


    def delObjInTank(self, obj):
        if isinstance(obj, Component):
            self.tank.children.remove(obj)
            self.components.remove(obj)
            del obj

    def addNewObjInTank(self, newComponent):
        if isinstance(newComponent, Component):
            self.tank.addChild(newComponent)
            self.components.append(newComponent)
        if isinstance(newComponent, EnvironmentObject):
            # add environment components list reference to this new object's
            newComponent.env_obj_list = self.components

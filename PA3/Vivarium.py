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
from ModelFish import Fish
from ModelShark import Shark
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

        self.addNewObjInTank(Fish(parent, Point((random.random(), random.random(), random.random())),Ct.DARKORANGE1))
        random.seed()
        self.addNewObjInTank(Fish(parent, Point((random.random(), random.random(), random.random())),Ct.BLUE))
        random.seed()
        self.addNewObjInTank(Shark(parent, Point((random.random(), random.random(), random.random())),Ct.SILVER))
        
    def animationUpdate(self):
        """
        Update all creatures in vivarium
        """
        for c in self.components[::-1]:
            if isinstance(c, Animation):
                c.animationUpdate()
                if (c.deleteFlag == True):
                    self.delObjInTank(c)
                    self.update()
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
            for comp in self.components:
                comp.env_obj_list = self.components[1:]

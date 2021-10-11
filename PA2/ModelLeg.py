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


class ModelLeg(Component):
    """
    Define our spider model
    """

    components = None
    contextParent = None

    def __init__(self, parent, position, display_obj=None):
        super().__init__(position, display_obj)
        self.components = []
        self.contextParent = parent

        jointLength = .8
        jointRadius = .05
        topJoint = Component(Point((0, 0, 0)), DisplayableCylinder(self.contextParent, 1, [jointRadius, jointRadius, jointLength]))
        topJoint.setDefaultColor(Ct.RED)
        topJoint.setDefaultAngle(-15, topJoint.uAxis)
        midJoint = Component(Point((0, jointRadius*2, jointLength)), DisplayableCylinder(self.contextParent, 1, [jointRadius, jointRadius, jointLength]))
        midJoint.setDefaultColor(Ct.GREEN)
        midJoint.setDefaultAngle(15, midJoint.uAxis)
        botJoint = Component(Point((0, jointRadius*2, jointLength)), DisplayableCylinder(self.contextParent, 1, [jointRadius, jointRadius, jointLength]))
        botJoint.setDefaultColor(Ct.BLUE)
        botJoint.setDefaultAngle(15, botJoint.uAxis)
        foot = Component(Point((0, 0, jointLength*1.5)), DisplayableSphere(self.contextParent, jointRadius))
        foot.setDefaultColor(Ct.DARKORANGE4)

        self.addChild(topJoint)
        topJoint.addChild(midJoint)
        midJoint.addChild(botJoint)
        botJoint.addChild(foot)

        self.components = [topJoint, midJoint, botJoint, foot]


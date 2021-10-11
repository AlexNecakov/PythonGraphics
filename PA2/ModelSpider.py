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


class ModelSpider(Component):
    """
    Define our spider model
    """

    components = None
    contextParent = None

    def __init__(self, parent, position, display_obj=None):
        super().__init__(position, display_obj)
        self.components = []
        self.contextParent = parent

        linkageLength = 0.5
        thorax = Component(Point((0, 0, 0)), DisplayableSphere(self.contextParent, 1, [2*linkageLength, linkageLength, linkageLength]))
        thorax.setDefaultColor(Ct.PURPLE)
        thorax.setDefaultAngle(90, thorax.vAxis)
        abdomen = Component(Point((1, 0, 0)), DisplayableSphere(self.contextParent, 1, [2*linkageLength, linkageLength, linkageLength]))
        abdomen.setDefaultColor(Ct.SILVER)
        legTest = ModelLeg(self.contextParent, Point((0, 0, linkageLength)))
        # link4 = Component(Point((0, 0, linkageLength)), DisplayableCube(self.contextParent, 1, [0.2, 0.2, linkageLength]))
        # link4.setDefaultColor(Ct.DARKORANGE4)

        self.addChild(thorax)
        thorax.addChild(abdomen)
        thorax.addChild(legTest)

        self.components = [thorax, abdomen, legTest]


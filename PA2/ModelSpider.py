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
        abdomen = Component(Point((linkageLength*2, 0, 0)), DisplayableSphere(self.contextParent, 1, [linkageLength*1.8, linkageLength, linkageLength]))
        abdomen.setDefaultAngle(15, abdomen.wAxis)
        abdomen.setDefaultColor(Ct.SILVER)
        legMandL = ModelLeg(self.contextParent, Point((-linkageLength, 0, linkageLength/2)))
        legMandL.setDefaultAngle(-50, legMandL.vAxis)
        legMandR = ModelLeg(self.contextParent, Point((-linkageLength, 0, linkageLength/2)))
        legMandR.setDefaultAngle(50, legMandR.vAxis)
        legMandR.setCurrentScale([1,1,-1])
        legSecondL = ModelLeg(self.contextParent, Point((-linkageLength/2, 0, linkageLength/2)))
        legSecondR = ModelLeg(self.contextParent, Point((-linkageLength/2, 0, linkageLength/2)))
        legSecondR.setCurrentScale([1,1,-1])
        legThirdL = ModelLeg(self.contextParent, Point((0, 0, linkageLength/2)))
        legThirdR = ModelLeg(self.contextParent, Point((0, 0, linkageLength/2)))
        legThirdR.setCurrentScale([1,1,-1])
        legHindL = ModelLeg(self.contextParent, Point((linkageLength/2, 0, linkageLength/2)))
        legHindR = ModelLeg(self.contextParent, Point((linkageLength/2, 0, linkageLength/2)))
        legHindR.setCurrentScale([1,1,-1])

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

        self.components = [thorax, abdomen, legMandL, legMandR, legSecondL, legSecondR, legThirdL, legThirdR, legHindL, legHindR]


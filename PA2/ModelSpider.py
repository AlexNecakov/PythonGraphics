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

        thoraxLength = 0.5
        legHeight = thoraxLength/2
        mandLegPos = -thoraxLength/2
        secondLegPos = 0
        thirdLegPos = 0
        hindLegPos = thoraxLength/2

        thorax = Component(Point((0, 0, 0)), DisplayableSphere(self.contextParent, 1, [2*thoraxLength, thoraxLength, thoraxLength]))
        thorax.setDefaultColor(Ct.PURPLE)
        thorax.setDefaultAngle(90, thorax.vAxis)
        abdomen = Component(Point((thoraxLength*2.5, 0, 0)), DisplayableSphere(self.contextParent, 1, [thoraxLength*1.75, thoraxLength, thoraxLength]))
        abdomen.setDefaultAngle(15, abdomen.wAxis)
        abdomen.setDefaultColor(Ct.SILVER)
        
        legMandL = ModelLeg(self.contextParent, Point((mandLegPos, 0, legHeight)))
        legMandL.setDefaultAngle(-60, legMandL.vAxis)
        legMandR = ModelLeg(self.contextParent, Point((mandLegPos, 0, legHeight)))
        legMandR.setDefaultAngle(60, legMandR.vAxis)
        legMandR.setCurrentScale([1,1,-1])
        
        legSecondL = ModelLeg(self.contextParent, Point((secondLegPos, 0, legHeight)))
        legSecondL.setDefaultAngle(-30, legSecondL.vAxis)
        legSecondR = ModelLeg(self.contextParent, Point((secondLegPos, 0, legHeight)))
        legSecondR.setDefaultAngle(30, legSecondR.vAxis)
        legSecondR.setCurrentScale([1,1,-1])
        
        legThirdL = ModelLeg(self.contextParent, Point((thirdLegPos, 0, legHeight)))
        legThirdL.setDefaultAngle(20, legThirdL.vAxis)
        legThirdR = ModelLeg(self.contextParent, Point((thirdLegPos, 0, legHeight)))
        legThirdR.setDefaultAngle(-20, legThirdR.vAxis)
        legThirdR.setCurrentScale([1,1,-1])
        
        legHindL = ModelLeg(self.contextParent, Point((hindLegPos, 0, legHeight)))
        legHindL.setDefaultAngle(50, legHindL.vAxis)
        legHindR = ModelLeg(self.contextParent, Point((hindLegPos, 0, legHeight)))
        legHindR.setDefaultAngle(-50, legHindR.vAxis)
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


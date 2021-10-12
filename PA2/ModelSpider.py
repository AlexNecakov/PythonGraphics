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
        mandLegMaxUAngle = 30
        mandLegMinVAngle = -90
        mandLegMaxVAngle = -30
        mandLegMinWAngle = -80
        mandLegMaxWAngle = 60

        secondLegPos = 0
        secondLegAngle = -30
        secondLegMinUAngle = -30
        secondLegMaxUAngle = 30
        secondLegMinVAngle = -60
        secondLegMaxVAngle = 0
        secondLegMinWAngle = -80
        secondLegMaxWAngle = 60

        thirdLegPos = 0
        thirdLegAngle = 20
        thirdLegMinUAngle = -30
        thirdLegMaxUAngle = 30
        thirdLegMinVAngle = -10
        thirdLegMaxVAngle = 50
        thirdLegMinWAngle = -80
        thirdLegMaxWAngle = 60

        hindLegPos = thoraxLength/2
        hindLegAngle = 50
        hindLegMinUAngle = -30
        hindLegMaxUAngle = 30
        hindLegMinVAngle = 20
        hindLegMaxVAngle = 80
        hindLegMinWAngle = -80
        hindLegMaxWAngle = 60

        thorax = Component(Point((0, 0, 0)), DisplayableSphere(self.contextParent, 1, [2*thoraxLength, thoraxLength, thoraxLength]))
        thorax.setDefaultColor(Ct.PURPLE)
        thorax.setRotateExtent(thorax.uAxis, thoraxMinUAngle, thoraxMaxUAngle)
        thorax.setRotateExtent(thorax.vAxis, thoraxMinVAngle, thoraxMaxVAngle)
        thorax.setRotateExtent(thorax.wAxis, thoraxMinWAngle, thoraxMaxWAngle)

        abdomen = Component(Point((thoraxLength*2.5, 0, 0)), DisplayableSphere(self.contextParent, 1, [thoraxLength*1.75, thoraxLength, thoraxLength]))
        abdomen.setDefaultAngle(15, abdomen.wAxis)
        abdomen.setDefaultColor(Ct.SILVER)
        abdomen.setRotateExtent(abdomen.uAxis, abdomenMinUAngle, abdomenMaxUAngle)
        abdomen.setRotateExtent(abdomen.vAxis, abdomenMinVAngle, abdomenMaxVAngle)
        abdomen.setRotateExtent(abdomen.wAxis, abdomenMinWAngle, abdomenMaxWAngle)
        
        legMandL = ModelLeg(self.contextParent, Point((mandLegPos, 0, legHeight)))
        legMandL.setDefaultAngle(mandLegAngle, legMandL.vAxis)
        legMandL.setRotateExtent(legMandL.uAxis, mandLegMinUAngle, mandLegMaxUAngle)
        legMandL.setRotateExtent(legMandL.vAxis, mandLegMinVAngle, mandLegMaxVAngle)
        legMandL.setRotateExtent(legMandL.wAxis, mandLegMinWAngle, mandLegMaxWAngle)
        legMandR = ModelLeg(self.contextParent, Point((mandLegPos, 0, legHeight)))
        legMandR.setDefaultAngle(180, legMandR.uAxis)
        legMandR.setDefaultAngle(mandLegAngle, legMandR.vAxis)
        legMandR.setDefaultAngle(180, legMandR.wAxis)
        legMandR.setRotateExtent(legMandR.uAxis, mandLegMinUAngle, mandLegMaxUAngle)
        legMandR.setRotateExtent(legMandR.vAxis, mandLegMinVAngle, mandLegMaxVAngle)
        legMandR.setRotateExtent(legMandR.wAxis, mandLegMinWAngle, mandLegMaxWAngle)
        
        legSecondL = ModelLeg(self.contextParent, Point((secondLegPos, 0, legHeight)))
        legSecondL.setDefaultAngle(secondLegAngle, legSecondL.vAxis)
        legSecondL.setRotateExtent(legSecondL.uAxis, secondLegMinUAngle, secondLegMaxUAngle)
        legSecondL.setRotateExtent(legSecondL.vAxis, secondLegMinVAngle, secondLegMaxVAngle)
        legSecondL.setRotateExtent(legSecondL.wAxis, secondLegMinWAngle, secondLegMaxWAngle)
        legSecondR = ModelLeg(self.contextParent, Point((secondLegPos, 0, legHeight)))
        legSecondR.setDefaultAngle(180, legSecondR.uAxis)
        legSecondR.setDefaultAngle(secondLegAngle, legSecondR.vAxis)
        legSecondR.setDefaultAngle(180, legSecondR.wAxis)
        legSecondR.setRotateExtent(legSecondR.uAxis, secondLegMinUAngle, secondLegMaxUAngle)
        legSecondR.setRotateExtent(legSecondR.vAxis, secondLegMinVAngle, secondLegMaxVAngle)
        legSecondR.setRotateExtent(legSecondR.wAxis, secondLegMinWAngle, secondLegMaxWAngle)
        
        legThirdL = ModelLeg(self.contextParent, Point((thirdLegPos, 0, legHeight)))
        legThirdL.setDefaultAngle(thirdLegAngle, legThirdL.vAxis)
        legThirdL.setRotateExtent(legThirdL.uAxis, thirdLegMinUAngle, thirdLegMaxUAngle)
        legThirdL.setRotateExtent(legThirdL.vAxis, thirdLegMinVAngle, thirdLegMaxVAngle)
        legThirdL.setRotateExtent(legThirdL.wAxis, thirdLegMinWAngle, thirdLegMaxWAngle)
        legThirdR = ModelLeg(self.contextParent, Point((thirdLegPos, 0, legHeight)))
        legThirdR.setDefaultAngle(180, legThirdR.uAxis)
        legThirdR.setDefaultAngle(thirdLegAngle, legThirdR.vAxis)
        legThirdR.setDefaultAngle(180, legThirdR.wAxis)
        legThirdR.setRotateExtent(legThirdR.uAxis, thirdLegMinUAngle, thirdLegMaxUAngle)
        legThirdR.setRotateExtent(legThirdR.vAxis, thirdLegMinVAngle, thirdLegMaxVAngle)
        legThirdR.setRotateExtent(legThirdR.wAxis, thirdLegMinWAngle, thirdLegMaxWAngle)
        
        legHindL = ModelLeg(self.contextParent, Point((hindLegPos, 0, legHeight)))
        legHindL.setDefaultAngle(hindLegAngle, legHindL.vAxis)
        legHindL.setRotateExtent(legHindL.uAxis, hindLegMinUAngle, hindLegMaxUAngle)
        legHindL.setRotateExtent(legHindL.vAxis, hindLegMinVAngle, hindLegMaxVAngle)
        legHindL.setRotateExtent(legHindL.wAxis, hindLegMinWAngle, hindLegMaxWAngle)
        legHindR = ModelLeg(self.contextParent, Point((hindLegPos, 0, legHeight)))
        legHindR.setDefaultAngle(180, legHindR.uAxis)
        legHindR.setDefaultAngle(hindLegAngle, legHindR.vAxis)
        legHindR.setDefaultAngle(180, legHindR.wAxis)
        legHindR.setRotateExtent(legHindR.uAxis, hindLegMinUAngle, hindLegMaxUAngle)
        legHindR.setRotateExtent(legHindR.vAxis, hindLegMinVAngle, hindLegMaxVAngle)
        legHindR.setRotateExtent(legHindR.wAxis, hindLegMinWAngle, hindLegMaxWAngle)

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


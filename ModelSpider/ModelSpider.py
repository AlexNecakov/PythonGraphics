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


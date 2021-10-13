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

        jointLength = 1.6
        jointRadius = .08

        topJointAngle = -15
        topJointMinUAngle = -45
        topJointMaxUAngle = 45
        topJointMinVAngle = -10
        topJointMaxVAngle = 10
        topJointMinWAngle = -20
        topJointMaxWAngle = 20

        midJointAngle = 25
        midJointMinUAngle = 0
        midJointMaxUAngle = 90
        midJointMinVAngle = -10
        midJointMaxVAngle = 10
        midJointMinWAngle = -10
        midJointMaxWAngle = 10
        
        botJointAngle = 15
        botJointMinUAngle = 0
        botJointMaxUAngle = 90
        botJointMinVAngle = -10
        botJointMaxVAngle = 10
        botJointMinWAngle = -10
        botJointMaxWAngle = 10

        topJoint = Component(Point((0, 0, 0)), DisplayableCylinder(self.contextParent, 1, [jointRadius, jointRadius, jointLength]))
        topJoint.setDefaultColor(Ct.RED)
        topJoint.setDefaultAngle(topJointAngle, topJoint.uAxis)
        topJoint.setRotateExtent(topJoint.uAxis, topJointMinUAngle, topJointMaxUAngle)
        topJoint.setRotateExtent(topJoint.vAxis, topJointMinVAngle, topJointMaxVAngle)
        topJoint.setRotateExtent(topJoint.wAxis, topJointMinWAngle, topJointMaxWAngle)

        #no rotation on kneeUpper ball
        kneeUpper = Component(Point((0, 0, jointLength)), DisplayableSphere(self.contextParent, jointRadius))
        kneeUpper.setDefaultColor(Ct.DARKORANGE4)
        kneeUpper.setRotateExtent(kneeUpper.uAxis, 0, 0)
        kneeUpper.setRotateExtent(kneeUpper.vAxis, 0, 0)
        kneeUpper.setRotateExtent(kneeUpper.wAxis, 0, 0)
        
        midJoint = Component(Point((0, 0, 0)), DisplayableCylinder(self.contextParent, 1, [jointRadius, jointRadius, jointLength]))
        midJoint.setDefaultColor(Ct.GREEN)
        midJoint.setDefaultAngle(midJointAngle, midJoint.uAxis)
        midJoint.setRotateExtent(midJoint.uAxis, midJointMinUAngle, midJointMaxUAngle)
        midJoint.setRotateExtent(midJoint.vAxis, midJointMinVAngle, midJointMaxVAngle)
        midJoint.setRotateExtent(midJoint.wAxis, midJointMinWAngle, midJointMaxWAngle)
        
        #no rotation on kneeLower ball
        kneeLower = Component(Point((0, 0, jointLength)), DisplayableSphere(self.contextParent, jointRadius))
        kneeLower.setDefaultColor(Ct.DARKORANGE4)
        kneeLower.setRotateExtent(kneeLower.uAxis, 0, 0)
        kneeLower.setRotateExtent(kneeLower.vAxis, 0, 0)
        kneeLower.setRotateExtent(kneeLower.wAxis, 0, 0)
        
        botJoint = Component(Point((0, 0, 0)), DisplayableCylinder(self.contextParent, 1, [jointRadius, jointRadius, jointLength]))
        botJoint.setDefaultColor(Ct.BLUE)
        botJoint.setDefaultAngle(botJointAngle, botJoint.uAxis)
        botJoint.setRotateExtent(botJoint.uAxis, botJointMinUAngle, botJointMaxUAngle)
        botJoint.setRotateExtent(botJoint.vAxis, botJointMinVAngle, botJointMaxVAngle)
        botJoint.setRotateExtent(botJoint.wAxis, botJointMinWAngle, botJointMaxWAngle)
        
        #no rotation on foot ball
        foot = Component(Point((0, 0, jointLength)), DisplayableSphere(self.contextParent, jointRadius))
        foot.setDefaultColor(Ct.DARKORANGE4)
        foot.setRotateExtent(foot.uAxis, 0, 0)
        foot.setRotateExtent(foot.vAxis, 0, 0)
        foot.setRotateExtent(foot.wAxis, 0, 0)

        self.addChild(topJoint)
        topJoint.addChild(kneeUpper)
        kneeUpper.addChild(midJoint)
        midJoint.addChild(kneeLower)
        kneeLower.addChild(botJoint)
        botJoint.addChild(foot)

        self.components = [topJoint, midJoint, botJoint, kneeUpper, kneeLower, foot]


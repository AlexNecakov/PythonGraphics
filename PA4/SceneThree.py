"""
Define a fixed scene with rotating lights
First version in 11/08/2021

:author: micou(Zezhou Sun)
:version: 2021.1.1
"""
import math

import numpy as np

import ColorType
from Animation import Animation
from Component import Component
from Light import Light
from Material import Material
from Point import Point
import GLUtility

from DisplayableCube import DisplayableCube
from DisplayableTorus import DisplayableTorus
from DisplayableSphere import DisplayableSphere
from DisplayableCylinder import DisplayableCylinder

class SceneThree(Component):
    shaderProg = None
    glutility = None

    lights = None
    lightCubes = None

    def __init__(self, shaderProg):
        super().__init__(Point((0, 0, 0)))
        self.shaderProg = shaderProg
        self.glutility = GLUtility.GLUtility()

        sphere = Component(Point((-1, 0, 0)), DisplayableSphere(shaderProg, 1.0, 10, 6))
        m1 = Material(np.array((0.1, 0.1, 0.1, 0.1)), np.array((0.2, 0.2, 0.2, 1)),
                      np.array((0.4, 0.4, 0.4, 0.1)), 64)
        sphere.setMaterial(m1)
        sphere.renderingRouting = "lighting"
        self.addChild(sphere)

        cylinder = Component(Point((1, 0, 0)), DisplayableCylinder(shaderProg, 0.25, 0.5, 20))
        m2 = Material(np.array((0.31, 0.31, 0.31, 0.31)), np.array((0.52, 0.52, 0.52, 1)),
                      np.array((0.84, 0.84, 0.84, 0.81)), 64)
        cylinder.setMaterial(m2)
        cylinder.renderingRouting = "lighting"
        self.addChild(cylinder)

        torus = Component(Point((2, 0, 0)), DisplayableTorus(shaderProg, 0.5, 0.25, 40, 10))
        m3 = Material(np.array((0.51, 0.51, 0.51, 0.51)), np.array((0.12, 0.12, 0.12, 1)),
                      np.array((0.34, 0.34, 0.34, 0.31)), 64)
        torus.setMaterial(m3)
        torus.renderingRouting = "lighting"
        self.addChild(torus)

        l0 = Light(Point([0.0,-1.25,0.0]),
                   np.array((*ColorType.SOFTRED, 1.0)), np.array((1,0,0)), None, None, 0, 1)
        l1 = Light(Point([0.0,-1.25,0.0]),
                   np.array((*ColorType.SOFTBLUE, 1.0)))
        l2 = Light(Point([0.0,-1.25,0.0]),
                   np.array((*ColorType.SOFTGREEN, 1.0)))
        l3 = Light(Point([0.0,-1.25,0.0]),
                   np.array((*ColorType.GREEN, 1.0)), None, np.array((0,1,0)), np.array((0.2,0.2,0.2)), 10, 1)

        self.lights = [l0, l1, l2, l3]

    def initialize(self):
        self.shaderProg.clearAllLights()
        for i, v in enumerate(self.lights):
            self.shaderProg.setLight(i, v)
        super().initialize()
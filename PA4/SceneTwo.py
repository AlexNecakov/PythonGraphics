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


class SceneTwo(Component):
    shaderProg = None
    glutility = None

    lights = None
    lightCubes = None

    def __init__(self, shaderProg):
        super().__init__(Point((0, 0, 0)))
        self.shaderProg = shaderProg
        self.glutility = GLUtility.GLUtility()

        sphere = Component(Point((0, 0, 0)), DisplayableSphere(shaderProg, 1.0, 64, 64))
        m1 = Material(np.array((0.1, 0.1, 0.1, 0.1)), np.array((0.2, 0.2, 0.2, 1)),
                      np.array((0.4, 0.4, 0.4, 0.1)), 64)
        sphere.setMaterial(m1)
        sphere.renderingRouting = "lighting"
        self.addChild(sphere)

        torus = Component(Point((2, 0, 0)), DisplayableTorus(shaderProg, 0.5, 0.2, 64, 64))
        m2 = Material(np.array((0.31, 0.51, 0.1, 0.61)), np.array((0.8, 0.25, 0.23, 1)),
                      np.array((0.1, 0.4, 0.6, 0.8)), 64)
        torus.setMaterial(m2)
        torus.renderingRouting = "lighting"
        self.addChild(torus)

        cube = Component(Point((0, 0, 2)), DisplayableCube(shaderProg, 0.5, 0.4, 0.3))
        m3 = Material(np.array((0.14, 0.61, 0.71, 0.31)), np.array((0.32, 0.22, 0.121, 1)),
                      np.array((0.14, 0.44, 0.74, 0.91)), 64)
        cube.setMaterial(m3)
        cube.renderingRouting = "lighting"
        self.addChild(cube)

        l0 = Light(Point([0.0, 1.5, 0.0]),
                   np.array((*ColorType.WHITE, 1.0)), None, None, None, 0, 1)
        lightCube0 = Component(Point((0.0, 1.5, 0.0)), DisplayableCube(shaderProg, 0.1, 0.1, 0.1, ColorType.WHITE))
        lightCube0.renderingRouting = "vertex"
        l1 = Light(None,
                   np.array((*ColorType.RED, 1.0)), np.array((1,0,0)), None, None, 0, 1)
        l2 = Light(Point([0.0,-1.25,0.0]),
                   np.array((*ColorType.GREEN, 1.0)), None, np.array((0,1,0)), np.array((0.2,0.2,0.2)), 10, 1)

        self.addChild(lightCube0)
        self.lights = [l0,l1,l2 ]
        self.lightCubes = [lightCube0, ]

    def initialize(self):
        self.shaderProg.clearAllLights()
        for i, v in enumerate(self.lights):
            self.shaderProg.setLight(i, v)
        super().initialize()

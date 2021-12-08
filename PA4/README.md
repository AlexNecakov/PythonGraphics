# Programming Assignment 04: Shaded Rendering


## 1. Overview

In this assignment you will use OpenGL Shading Language(GLSL) to write your own vertex and fragment shaders to compute illumination and shading of meshes.


### Basic Requirements




4. **Set up lights (TODO 4):** Set up lights:
   
    2. In the Sketch file Interrupt_keyboard method, bind keyboard interfaces that allow the user to toggle on/off specular, diffuse, and ambient with keys S, D, A.
5. **Create your scenes (TODO 5):**

    3. Provide a keyboard interface that allows the user to toggle on/off each of the lights in your scene model: Hit 1, 2, 3, 4, etc. to identify which light to toggle.


### Programming Style

9. For any modified or newly added source file, you should include a brief explanation about what you did in this file at the file heading and add your name to the author list. Your code should be readable with sufficient comments. You should use consistent variable naming and keep reasonable indentation. In python, we prefer to use reStructuredText format docstring, for more details about this format, please check **[here](https://devguide.python.org/documenting/)**.


## 2. Resources


### 2.1 Start code

A Python Program skeleton, which includes basic classes, methods, and main pipeline, is provided for you. You are expected to complete the parts marked with TODO. There are comments in the skeleton code that will help guide you in writing your own subroutines.


### 2.2 Environment Setup

Installing the appropriate programming environment should be covered in a lab session. For more step-by-step instructions, please check the environment set up on Blackboard.


### 2.3 User Interface

The user interface to the program is provided through mouse buttons and keyboard keys.

**Left Mouse Dragging**: Rotate the camera\
**Middle Mouse Dragging**: Translate the camera\
**A**: Toggle Ambient Light\
**D**: Toggle Diffuse Light\
**S**: Toggle Specular Light\
**Left Arrow**: Go back to last scene\
**Right Arrow**: Next Scene\
**1,2,3, ...**: Toggle lights in current scene


### 2.4 Video Demo

We prepared a video demo for you, hope this can help you better understand your tasks and speed up your debugging process. Please check it on the Blackboard.


## 3. Submission (due by midnight, Tuesday, 12/7)


### 3.1 Source Code

Your program's source files are to be submitted electronically on Gradescope. The code you submit should conform to the program assignment guidelines.


### 3.2 Demo

Part of your grade for this programming assignment will be based on your giving a short demo (5 minutes) during the CS480/680 scheduled labs following the assignment due date. You will be expected to talk about how your program works.


## 4. Grading

| Requirements                                                           | CS680 Credits |
| :--------------------------------------------------------------------- | :------------ |
| Generate Triangle Meshes: Ellipsoid, Torus, and Cylinder with end caps | 15            |
| Implement EBO for defining your meshes                                 | 10            |
| Generate normals for your meshes, and implement normal visualization   | 5             |
| Illuminate your meshes with diffuse, specular, and ambient components  | 20            |
| Support 3 different light types (point, infinite, spotlight)           | 15            |
| Create 3 different scenes                                              | 15            |
| Texture mapping                                                        | 10            |
| Normal mapping                                                         | 10(extra)     |
| Artist Rendering                                                       | 10(extra)     |
| Programming Style                                                      | 10            |



## 5. Code Distribution Policy

You acknowledge this code is only for the course learning purpose. You should never distribute any part of this assignment, especially the completed version, to any publicly accessible website or open repository without our permission. Keeping the code in your local computer or private repository is allowed. You should never share, sell, gift, or copy the code in any format with any other person without our permission.

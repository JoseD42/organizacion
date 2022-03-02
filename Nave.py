#La nomenclatura indica que la primera letra del nombre de una clase va en mayusculas
from OpenGL.GL import *
from glew_wish import *
import glfw

class Nave:
    posicion_x = 0.0
    posicion_y = 0.0
    posicion_z = 0.0
    velocidad = 1.2
    angulo = 0.0
    velocidad_rotacion = 270.0
    fase = 90.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glRotatef(self.angulo, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.3, 0.0, 1.0)
        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0.0,0.05,0)
        glVertex3f(0.05,-0.05,0)

        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05, -0.05, 0)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05, 0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()
from OpenGL.GL import *
from OpenGL.GLU import *

def render_object_quads(object_3d):
        glBegin(GL_QUADS)
        for objectFace in object_3d.faces:
            x = 0
            for objectVertices in objectFace:
                x+=1
                if x < len(object_3d.colors):
                    if object_3d.rgba:
                        glColor4fv(object_3d.colors[x])
                    else:
                        glColor3fv(object_3d.colors[x])
                    
                glVertex3fv(object_3d.vertices[objectVertices])
        glEnd()

def render_object_lines(object_3d):
    glBegin(GL_LINES)
    for objectFace in object_3d.faces:
        for objectVertices in objectFace:
            glVertex3fv(object_3d.vertices[objectVertices])
    glEnd()

def render_object_triangles(object_3d):
    glBegin(GL_TRIANGLES)
    for objectFace in object_3d.faces:
        x = 0
        for objectVertices in objectFace:
            x+=1
            if x < len(object_3d.colors):
                if object_3d.rgba:
                    glColor4fv(object_3d.colors[x])
                else:
                    glColor3fv(object_3d.colors[x])
                
            glVertex3fv(object_3d.vertices[objectVertices])
    glEnd()

def render_object_polygon(object_3d):
    glBegin(GL_POLYGON)
    for objectFace in object_3d.faces:
        x = 0
        for objectVertices in objectFace:
            x+=1
            if x < len(object_3d.colors):
                if object_3d.rgba:
                    glColor4fv(object_3d.colors[x])
                else:
                    glColor3fv(object_3d.colors[x])
                
            glVertex3fv(object_3d.vertices[objectVertices])
    glEnd()
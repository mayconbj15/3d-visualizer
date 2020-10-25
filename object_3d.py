from OpenGL.GL import *
from OpenGL.GLU import *

class Object:
    def __init__(self, filepath):
        self.filepath = filepath
        self.vertices = []
        self.faces = []

        self.read_file(filepath)

    def read_file(self, filepath):
        #todo: ignorar os comments do começo do arquivo
        #todo: tratar espaço entre os parametros. ex: hdodec.off
        #todo: pegar as cores do .off
        off = open(filepath, 'r')

        lines = off.readlines()

        file_type = lines[0]

        if file_type != 'OFF\n':
            print('not a .off file')
            return 
        
        file_info = lines[1]

        file_info = normalize(file_info)

        infos = file_info.split(' ')

        n_vertices = int(infos[0])
        n_faces = int(infos[1])
        n_edges = int(infos[2])

        vertices_lines = lines[2:(2+n_vertices)]

        for vertice_line in vertices_lines:
            vertice_line = normalize(vertice_line)
            vertice = vertice_line.split(' ')
            self.vertices.append((float(vertice[0]), float(vertice[1]), float(vertice[2])))

        faces_lines = lines[(2+n_vertices):(2+n_vertices+n_faces)]

        for face_line in faces_lines:
            face_line = normalize(face_line)

            face = face_line.split(' ')

            tuples = []
            for f in face[1:int(face[0])+1]:
                tuples.append(int(f))
                
            self.faces.append(tuple(tuples))

    def render_object_quads(self):
        glBegin(GL_QUADS)
        for objectFace in self.faces:
            for objectVertices in objectFace:
                glVertex3fv(self.vertices[objectVertices])
        glEnd()

    def render_object_lines(self):
        glBegin(GL_LINES)
        for objectFace in self.faces:
            for objectVertices in objectFace:
                glVertex3fv(self.vertices[objectVertices])
        glEnd()

def normalize(old_string):
    #todo: retirar espaços do fim

    old_string = lstrip(old_string)
    old_string = old_string.replace('\t', ' ')

    new_string = ''
    cont_space = 0
    for s in old_string:
        if s != ' ' and s != '\n' and s != '\t':
            cont_space = 0
            new_string = new_string + s
        elif s == ' ' and cont_space == 0:
            new_string = new_string + s
            cont_space = cont_space + 1

    return new_string

def lstrip(old_string):
    i = 0
    for s in old_string:
        if s == ' ':
            i = i + 1
        else:
            return old_string[i:len(old_string)]


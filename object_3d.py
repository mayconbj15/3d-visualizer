class Object:
    def __init__(self, filepath):
        self.filepath = filepath
        self.vertices = []
        self.faces = []
        self.colors = []
        self.rgba = False
        self.primitive = 'POLYGON'

        self.read_file(filepath)

    def read_file(self, filepath):
        #todo: ignorar os comments do começo do arquivo
        #todo: tratar espaço entre os parametros. ex: hdodec.off
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

        self.set_primitive(n_faces, n_edges)

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

            faces_length = int(face[0])+1
            color_length = len(face) - faces_length
            
            if color_length == 4:
                self.rgba = True

            if len(face) > faces_length:
                #get colors
                face_colors = face[faces_length:len(face)]
                colors = []
                for c in face_colors:
                    colors.append(float(c))
                
                self.colors.append(tuple(colors))
        
    def set_primitive(self, n_faces, n_edges):
        if n_edges != 0:
            primitive = n_edges % n_faces 
            if primitive == 0:
                self.primitive = 'QUADS'  
        
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


import os

class NoteMapper(object):
    def __init__(self):
        self.map = []
        
        with open(os.path.join('RythmGame', 'beatmap.txt'), 'r') as file:
            line = file.readline()
            while line:
                line = file.readline()
                if not line:
                    break
                self.map.append((int(line[0]), line[1:7]))



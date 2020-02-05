# class for 3D points in an image frame 
class Point(object):
    # class constructor
    def __init__(self, img_map, location):
        self.point = location
        self.frames = []
        self.idx = []
        self.id = len(img_map.points)
        img_map.points.append(self)

    # class method to add a frame and index from video
    # feed to the Point object
    def add_observation(self, frame, index):
        frame.pts[index] = self
        self.frames.append(frame)
        self.idx.append(index)



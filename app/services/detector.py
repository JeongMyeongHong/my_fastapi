from app.models.detector import Detector

class DetectorService(object):
    def __init__(self):
        self.detector = Detector()

    def detect(self, path):
        return self.detector.detect(path)


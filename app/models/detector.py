import torch
import cv2
import numpy as np
import requests

class Detector(object):
    def __init__(self):
        self.results = None
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='app/models/weight/best.pt')
        self.path = None
        self.names = None

    def detect(self, path):
        self.path = path
        results = self.model(path)
        df = results.pandas().xyxy[0]
        self.results = df.loc[df['name'] != 'plate']
        print(self.results['name'].tolist())
        print(type(self.results))
        self.draw_rectangle()
        return self.results.to_json(orient='records')

    def get_xy(self):
        return [[round(self.results.iat[x, y]) for y in range(0, 4)] for x in range(len(self.results))]

    def draw_rectangle(self):
        image_nparray = np.asarray(bytearray(requests.get(self.path).content), dtype=np.uint8)
        image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        [cv2.rectangle(image, (x, y), (w, h), (0, 0, 255), 2) for (x, y, w, h) in self.get_xy()]
        resize_img = cv2.resize(image, (800, 650))
        cv2.imshow('',resize_img)
        cv2.waitKey()
        cv2.imwrite('./save/tmc/' + format(self.get_file_name()), image)

    def get_file_name(self):
        return self.path.split('/')[-1]

if __name__ == '__main__':
    img = 'https://i0.wp.com/rchaan365.com/wp-content/uploads/2020/08/rchaan20200811_1.jpg'
    tmc = Detector()
    result_list = tmc.detect(img)


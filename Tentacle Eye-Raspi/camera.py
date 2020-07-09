from threading import Thread, Lock
import cv2
import time

import os
import shutil






class CameraStream(object):
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)


        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        

        (self.grabbed, self.frame) = self.stream.read()
        

        
        self.started = False
        self.read_lock = Lock()

    def start(self):
        if self.started:
            print("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):
        while self.started:
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self):
        self.read_lock.acquire()
        frame = self.frame.copy()
        self.read_lock.release()

        frame = cv2.flip(frame, 0)
        

        cv2.putText(frame, text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), org=(30, 450), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,255,0), thickness=2)
        
        return frame

    def stop(self):
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stream.release()

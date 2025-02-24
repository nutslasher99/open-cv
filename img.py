#OPENCV BASICS
import cv2
#READING IMAGE USING CLASSES AND METHODS
class Media():
    def __init__(self, img_path=None, vid_path=None):
        self.img_path = img_path
        self.vid_path = vid_path
        self.img=cv2.imread(img_path) if img_path else None
        self.vid=cv2.VideoCapture(vid_path) if vid_path else None

#READING IMAGES
class Image(Media):
    def show(self):
        if self.img is None:
            print("No Photos in directory")
            return
        
        cv2.imshow("Image", self.img)
        cv2.waitKey(0)

#READING VIDEO
class Video(Media):
    def play(self):
        if not self.vid.isOpened():
            print("theres no video found")
            return
        
        while True: 
            ret, frame = self.vid.read()
            if not ret:
                break
#PRESS 'd' TO EXIT
            cv2.imshow("Zild", frame)
            if cv2.waitKey(20) & 0xFF == ord('d'):
                break
        self.vid.release()
        cv2.destroyAllWindows()

img1=Image(img_path='C:\\Users\\Lyzann\\Desktop\\open cv\\img\\1.JPG')
img1.show()
vid1=Video(vid_path='C:\\Users\\Lyzann\\Desktop\\open cv\\vids\\Zild - I.N.A.S. (Official Video).mp4')
vid1.play()
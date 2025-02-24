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
#RESCALING AND RESIZING 
    def rescale(self, scale=2):
        if self.img is None:
            print("no photo")
            return
        
        width=int(self.img.shape[1] * scale)        
        height=int(self.img.shape[1] * scale) 
        dimension=(width, height) 

        resized_img = cv2.resize(self.img, dimension, interpolation=cv2.INTER_AREA)
        
        # Show resized image
        cv2.imshow("CUTE", resized_img)
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
#RESCALING AND RESIZING 
    def rescale(self, scale=2):
        if self.img is None:
            print("no photo")
            return
        
        width=int(self.img.shape[1] * scale)        
        height=int(self.img.shape[1] * scale) 
        dimension=(width, height) 

        resized_img = cv2.resize(self.img, dimension, interpolation=cv2.INTER_AREA)
        
        # Show resized image
        cv2.imshow("CUTE", resized_img)
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
#KAPANTAY DAPAT SI WHILE PARA DI MAGEXIT AGAD SI VIDEO
         self.vid.release()
         cv2.destroyAllWindows()


img1=Image(img_path='C:\\Users\\Lyzann\\Desktop\\open cv\\img\\1.JPG')
img1.show()
img1.rescale()

vid1=Video(vid_path='C:\\Users\\Lyzann\\Desktop\\open cv\\vids\\Zild - I.N.A.S. (Official Video).mp4')
vid1.play()


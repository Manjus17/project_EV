import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QDialog, QLabel
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QThread
import cv2

# VideoWidget is responsible for displaying the webcam feed in a QLabel.
class VideoWidget(QWidget):
    def __init__(self):
        super(VideoWidget, self).__init__()

        # Open the default camera (camera index 0).
        self.video_capture = cv2.VideoCapture(0)
        
        # Create a QLabel to display the video frames.
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Create a vertical layout to place the QLabel.
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        # Set up a QTimer to update the video frames at a specific rate (30 FPS).
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 // 30)  # 30 FPS

    def update_frame(self):
        # Read a frame from the camera.
        ret, frame = self.video_capture.read()
        if ret:
            # Convert the BGR image to RGB format.
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = image.shape

            # Create a QImage from the OpenCV image data.
            bytes_per_line = ch * w
            qt_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            
            # Create a QPixmap from the QImage and set it in the QLabel for display.
            pixmap = QPixmap.fromImage(qt_image)
            self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        # Release the camera and stop the timer when the window is closed.
        self.video_capture.release()
        self.timer.stop()

# CameraWindow is a dialog that contains the VideoWidget.
class CameraWindow(QDialog):
    def __init__(self):
        super(CameraWindow, self).__init__()

        # Create an instance of VideoWidget to display the camera feed.
        self.video_widget = VideoWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.video_widget)

# MaincamWindow is the main application window.
class MaincamWindow(QMainWindow):
    def open_camera_window(self):
        # Open the CameraWindow dialog when the "Open Camera" button is clicked.
        camera_window = CameraWindow()
        camera_window.exec_()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    
    # Create an instance of MaincamWindow and show the main application window.
    main_window = MaincamWindow()
    main_window.show()
    
    # Start the PyQt application event loop.
    sys.exit(App.exec_())

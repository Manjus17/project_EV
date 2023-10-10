import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView  # Import QtWebEngineWidgets here

######################################################################################
# DISPLAY MAP WINDOW
#######################################################################################
class ViewMapWindow(QMainWindow):
    print("in view map")
    def open_map_window(self, x, y, locations):
        map_dialog = ViewMapDialog(x, y, locations)
        map_dialog.exec_()



######################################################################################
# CREATE MAP WINDOW
#######################################################################################
class ViewMapDialog(QDialog):
    def center_on_screen(self):
        # Get the screen geometry
        screen_geometry = QApplication.desktop().screenGeometry()

        # Calculate the center point of the screen
        center_point = screen_geometry.center()

        # Calculate the new position for the window
        new_x = int(center_point.x() - self.width() / 2)
        new_y = int(center_point.y() - self.height() / 2)

        # Set the window position
        self.move(new_x, new_y)

    def __init__(self, x, y, locations):
        super().__init__()
        # set window settings
        self.setWindowTitle("All Managed stations")
        self.setGeometry(200, 200, 800, 600)
        self.center_on_screen()  # Center the window on the screen

        import folium

        m = folium.Map(location=[x, y], zoom_start=12)

        # Add markers using a for loop
        for location in locations:
            folium.Marker(
                location=[location["lat"], location["lon"]],
                tooltip=location["name"],
                popup=location["popup"],
                icon=folium.Icon(color='blue',prefix='fa',icon='car'),
            ).add_to(m)
        map_html = m._repr_html_()

        # creates an instance of the QWebEngineView class, which is a widget provided 
        # by PyQt5 for displaying web content using the Chromium-based QtWebEngine framework
        self.map_view = QWebEngineView()

        # sets the HTML content to be displayed in the QWebEngineView widget. 
        self.map_view.setHtml(map_html)

        # set layout
        layout = QVBoxLayout()
        # add map as widget
        layout.addWidget(self.map_view)

        self.setLayout(layout)

if __name__ == "__main__":
    # Set the attribute before creating a QApplication instance
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)

    locations = [
        {"name": "Station 1", "lat": 40.7128, "lon": -74.0060, "popup": "Malaviya National Institute of Technology, jaipur"},
        {"name": "Marker 2", "lat": 34.0522, "lon": -118.2437, "popup": "Patrika Gate, Jaipur"}
    ]
    
    app = QApplication(sys.argv)
    window = ViewMapWindow()
    window.show()
    sys.exit(app.exec_())


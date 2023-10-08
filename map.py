
# import sys
# import io
# import folium # pip install folium
# from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
# from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine



# class Map_in_App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Folium in PyQt Example')
#         self.window_width, self.window_height = 1600, 1200
#         self.setMinimumSize(self.window_width, self.window_height)

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         coordinate = (26.9124, 75.7873)
#         m = folium.Map(
#         	# tiles='Stamen Terrain',
#         	zoom_start=13,
#         	location=coordinate
#         )

        # folium.Marker(
        #     location=[26.9124, 75.7873],
        #     tooltip="Station 1",
        #     popup="Jaipur",
        #     icon=folium.Icon(color='blue',prefix='fa',icon='car'),
        # ).add_to(m)


#         # save map data to data object
#         data = io.BytesIO()
#         m.save(data, close_file=False)

#         webView = QWebEngineView()
#         webView.setHtml(data.getvalue().decode())
#         layout.addWidget(webView)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     app.setStyleSheet('''
#         QWidget {
#             font-size: 35px;
#         }
#     ''')
    
#     myApp = Map_in_App()
#     myApp.show()

#     try:
#         sys.exit(app.exec_())
#     except SystemExit:
#         print('Closing Window...')

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView  # Import QtWebEngineWidgets here

class MapWindow(QMainWindow):
    # def __init__(self):
    #     super().__init__()
    #     self.setWindowTitle("Qt Application with Folium Map")
    #     self.setGeometry(100, 100, 400, 200)

    #     layout = QVBoxLayout()

    #     button = QPushButton("Open Map")
    #     button.clicked.connect(self.open_map_window)

    #     layout.addWidget(button)

    #     central_widget = QWidget()
    #     central_widget.setLayout(layout)
    #     self.setCentralWidget(central_widget)

    def open_map_window(self, x, y, station, loction):
        map_dialog = MapDialog(x, y, station, loction)
        map_dialog.exec_()

class MapDialog(QDialog):
    def __init__(self, x, y, station, loction):
        super().__init__()
        self.setWindowTitle("Folium Map")
        self.setGeometry(200, 200, 800, 600)

        # Create a Folium map and display it in a QWebView
        import folium
        # 51.5074, -0.1278

        m = folium.Map(location=[x, y], zoom_start=22)
        folium.Marker(
            location=[x, y],
            tooltip=station,
            popup=loction,
            icon=folium.Icon(color='blue',prefix='fa',icon='car'),
        ).add_to(m)
        map_html = m._repr_html_()

        

        self.map_view = QWebEngineView()
        self.map_view.setHtml(map_html)

        layout = QVBoxLayout()
        layout.addWidget(self.map_view)

        self.setLayout(layout)

if __name__ == "__main__":
    # Set the attribute before creating a QApplication instance
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)
    
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())


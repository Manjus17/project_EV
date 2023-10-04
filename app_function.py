##########################################################################################################
# IMPORT APP_MAIN
##########################################################################################################
from app_main import *



class UIFunctions(MainWindow):
    ##########################################################################################################
    # HOME PAGE
    ##########################################################################################################
    def home_page_fun(self):
        # link with the stacked widget page
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

        # style the colour of selected menu and change color of other all to non selected color
        self.ui.home.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "background-color: rgb(50, 162, 244);\n"
        "border: none;\n"
        "border-radius: 10;\n"
        "padding: 3px 5px;")
        self.ui.stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.my_account.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.report.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.settings.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")


    ##########################################################################################################
    # STATIONS PAGE
    ##########################################################################################################
    def stations_page_fun(self):
        # link with the stacked widget page
        self.ui.stackedWidget.setCurrentWidget(self.ui.stations_page)

        # style the colour of selected menu and change color of other all to non selected color
        self.ui.stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "background-color: rgb(50, 162, 244);\n"
        "border: none;\n"
        "border-radius: 10;\n"
        "padding: 3px 5px;")
        self.ui.home.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.my_account.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.report.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.settings.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")




    ##########################################################################################################
    # REPORT PAGE
    ##########################################################################################################
    def report_page_fun(self):
        # link with the stacked widget page
        self.ui.stackedWidget.setCurrentWidget(self.ui.report_page)

        # style the colour of selected menu and change color of other all to non selected color
        self.ui.report.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "background-color: rgb(50, 162, 244);\n"
        "border: none;\n"
        "border-radius: 10;\n"
        "padding: 3px 5px;")
        self.ui.home.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.my_account.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.settings.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")

    

    ##########################################################################################################
    # MY ACCOUNTS PAGE
    ##########################################################################################################
    def account_page_fun(self):
        # link with the stacked widget page
        self.ui.stackedWidget.setCurrentWidget(self.ui.account_page_2)

        # style the colour of selected menu and change color of other all to non selected color
        self.ui.my_account.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "background-color: rgb(50, 162, 244);\n"
        "border: none;\n"
        "border-radius: 10;\n"
        "padding: 3px 5px;")
        self.ui.home.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.report.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.settings.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")


    

    ##########################################################################################################
    # SETTINGS PAGE
    ##########################################################################################################
    def settings_page_fun(self):
        # link with the stacked widget page
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page_2)

        # style the colour of selected menu and change color of other all to non selected color
        self.ui.settings.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "background-color: rgb(50, 162, 244);\n"
        "border: none;\n"
        "border-radius: 10;\n"
        "padding: 3px 5px;")
        self.ui.home.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.my_account.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.report.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")




    ##########################################################################################################
    # ABOUT PAGE
    ##########################################################################################################
    def about_page_fun(self):
        # link with the stacked widget page
        self.ui.stackedWidget.setCurrentWidget(self.ui.about_page_2)

        # style the colour of selected menu and change color of other all to non selected color
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "background-color: rgb(50, 162, 244);\n"
        "border: none;\n"
        "border-radius: 10;\n"
        "padding: 3px 5px;")
        self.ui.home.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.my_account.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.report.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.settings.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
   


    ##########################################################################################################
    # PROGRESS BAR ALGO
    ##########################################################################################################
    def progress_bar_value(a, b):
        if a == 0:
            return 0
        else:
            ans = (a/b)*100
            return ans
        


    ##########################################################################################################
    # AVAILABLR CHARGERS 
    ##########################################################################################################
    def available(a, b):
        return a-b

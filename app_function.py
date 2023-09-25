from app_main import *

class UIFunctions(MainWindow):

    # HOME PAGE
    def home_page_fun(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
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
        self.ui.security.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")


    # STATIONS PAGE
    def stations_page_fun(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stations_page)
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
        self.ui.security.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")


    # REPORT PAGE
    def report_page_fun(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.report_page)
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
        self.ui.security.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")


    # SECURITY PAGE
    # def security_page_fun(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.security_page)
    #     self.ui.security.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    #     "font: 14pt \"Consolas\";\n"
    #     "background-color: rgb(50, 162, 244);\n"
    #     "border: none;\n"
    #     "border-radius: 10;\n"
    #     "padding: 3px 5px;")
    #     self.ui.home.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    #     "font: 14pt \"Consolas\";\n"
    #     "padding: 3px 5px;")
    #     self.ui.my_account.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    #     "font: 14pt \"Consolas\";\n"
    #     "padding: 3px 5px;")
    #     self.ui.stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    #     "font: 14pt \"Consolas\";\n"
    #     "padding: 3px 5px;")
    #     self.ui.settings.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    #     "font: 14pt \"Consolas\";\n"
    #     "padding: 3px 5px;")
    #     self.ui.report.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    #     "font: 14pt \"Consolas\";\n"
    #     "padding: 3px 5px;")
    #     self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
    #     "font: 14pt \"Consolas\";\n"
    #     "padding: 3px 5px;")


    # MY_ACCOUNT PAGE
    def account_page_fun(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.account_page_2)
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
        self.ui.security.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")


    # SETTING PAGE 
    def settings_page_fun(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page_2)
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
        self.ui.security.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.About.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")


    # ABOUT PAGE
    def about_page_fun(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.about_page_2)
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
        self.ui.security.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
        self.ui.stations.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "font: 14pt \"Consolas\";\n"
        "padding: 3px 5px;")
   
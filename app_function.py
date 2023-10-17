##########################################################################################################
# IMPORT APP_MAIN
##########################################################################################################
from app_main import *
from datetime import datetime, timedelta



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
        not_in_use = 0
        tot_in_use = 0
        for val in a:
            tot_in_use += val["power_use"]*val["percentage"]/100
        
        for val in b:
            not_in_use += val["power_use"]*val["percentage"]/100

        ans = tot_in_use/(tot_in_use + not_in_use)*100
        return ans




    ##########################################################################################################
    # AVAILABLR CHARGERS 
    ##########################################################################################################
    def available(a, b):
        return a-b
    



    ##########################################################################################################
    # EXPECTED RETURN TIME CALCULATION
    ##########################################################################################################
    def calculate_charging_end_time(start_time, current_soc, ev_capacity, charging_rate):
        # Convert the start_time to a datetime object
        start_time = datetime.strptime(start_time, '%H:%M')
        
        # Calculate the energy required to charge the EV to its full capacity
        energy_required = ev_capacity - current_soc
        
        # Calculate the time required for charging in hours
        charging_time_hours = energy_required / charging_rate
        
        # Calculate the expected charging end time
        end_time = start_time + timedelta(hours=charging_time_hours)
        
        # Format the end_time as a string in HH:MM format
        end_time_str = end_time.strftime('%H:%M')
        return end_time_str
    


    

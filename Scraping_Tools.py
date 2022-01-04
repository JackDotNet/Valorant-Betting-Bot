from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import pprint
import re

def convert_perc_to_float(perc_str):
            return round(float(perc_str.replace("%", "")) / 100, 4)


class webdriver_tools:

    def __init__(self, link):
        self.link = link
        self.driver = self.open_browser()
 
    def open_browser(self):
        link = self.link
        options = Options()
        options.binary_location = r'C:/Program Files/Google/Chrome/Application/chrome.exe'
        driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe', chrome_options=options)
        driver.get(link)
        return driver
    
    def return_driver_instance(self):
        return self.driver

    def turn_page(self):
        self.driver.find_element_by_class_name("pagination-next").click()
    
    def find_all_element_with_xpath(self, xpath):
        link = self.link
        driver = self.driver
        elements = driver.find_elements_by_xpath(xpath)
        return elements
    
    def find_single_element_by_xpath(self, xpath):
        link = self.link
        driver = self.driver
        elements = driver.find_element_by_xpath(xpath)
        return elements

    def find_element_by_class(self, class_name):
        driver = self.driver
        element = driver.find_element_by_class_name(class_name)
        return element

    def find_element_by_css(self, css_selector):
        driver = self.driver
        element = driver.find_element_by_css_selector(css_selector)
        return element

    def click_button(self, selenium_element_obj):
        selenium_element_obj.click()

    def return_page_source(self):
        driver = self.driver
        return driver.page_source

class Esports_Leetify_Scraping:

    def __init__(self, html_doc):
        self.html_doc = html_doc
        self.soup = BeautifulSoup(html_doc, 'html.parser')
    
    def get_player_containers(self):
        list = self.soup.find_all('tr')
        try:
            list.pop(0)
        except:
            print(self.html_doc)
        return list
    
    def get_children_player_container(self, container_instance):
        return container_instance.find_all('td')

    def turn_page(self, driver):
        driver.find_element_by_class_name("pagination-next").click()
    
    def return_all_player_names(self):
        player_containers = self.get_player_containers()
        player_names = []
        for container in player_containers:
            player_names.append(container.find(class_="p-2").text.replace(" ", ""))
        # print(player_names)
        return player_names
    
    def return_all_player_teams(self):
        team_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            # print(children)
            team_list.append(children[1].text)
        return team_list

    def return_all_HLTV_Rating(self):
        HLTV_Rating_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            HLTV_Rating_list.append(float(children[2].text))
        return HLTV_Rating_list

    def return_all_ADR(self):
        ADR_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            ADR_list.append(float(children[3].text))
        return ADR_list

    def return_all_mean_KD(self):
        KD_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            KD_list.append(float(children[4].text))
        return KD_list

    def return_all_KPR(self):
        KPR_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            KPR_list.append(float(children[5].text))
        return KPR_list

    def return_all_DPR(self):
        DPR_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            DPR_list.append(float(children[6].text))
        return DPR_list
    
    def return_all_Rounds_Survived(self):
        RS_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            RS_list.append(float(children[7].text.replace("%", ""))/100)
        return RS_list
    
    def generate_general_stats_array(self):
        general_stats_array = [self.return_all_player_names(),
        self.return_all_HLTV_Rating(),
        self.return_all_ADR(),
        self.return_all_mean_KD(),
        self.return_all_KPR(),
        self.return_all_DPR(),
        self.return_all_Rounds_Survived()]
        return general_stats_array
        

    # ALL FUNCTIONS BEYOND THIS POINT MUST BE USED IN THE "AIM" CATEGORY ON THE SITE
    # THESE FUNCTIONS WILL RETURN THE WRONG VALUES IF NOT IN CORRECT CATEGORY 

    def return_all_HS_Perc(self):
        HS_Perc_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            HS_Perc_list.append(round((float(children[2].text.replace(" %", ""))/100), 4))
        return HS_Perc_list
    
    def return_all_Accuracy_On_Spot(self):
        ACCU_Spot_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            ACCU_Spot_list.append(round((float(children[3].text.replace(" %", ""))/100), 4))
        return ACCU_Spot_list

    def return_all_Accuracy_On_All(self):
        ACCU_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            ACCU_list.append(round((float(children[4].text.replace(" %", ""))/100), 4))
        return ACCU_list
    
    def return_all_Spray_Accuracy(self):
        SA_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            SA_list.append(round((float(children[5].text.replace(" %", ""))/100), 4))
        return SA_list
    
    def return_all_Counter_Strafe(self):
        CS_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            CS_list.append(round((float(children[6].text.replace(" %", ""))/100), 4))
        return CS_list

    def return_all_Crosshair_Placement(self):
        CP_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            CP_list.append(round((float(children[7].text.replace(" °", ""))/100), 4))
        return CP_list
    
    def return_all_TTD(self):
        # TTD(Time To Damage)
        TTD_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            TTD_list.append(int(children[8].text.replace(" ms", "")))
        return TTD_list

    def generate_aim_stats_array(self):
        return [self.return_all_HS_Perc(),
        self.return_all_Accuracy_On_Spot(),
        self.return_all_Accuracy_On_All(),
        self.return_all_Spray_Accuracy(),
        self.return_all_Counter_Strafe(),
        self.return_all_Crosshair_Placement(),
        self.return_all_TTD()]

    # ALL FUNCTIONS BEYOND THIS POINT MUST BE USED IN THE "UTILITY" CATEGORY ON THE SITE
    # THESE FUNCTIONS WILL RETURN THE WRONG VALUES IF NOT IN CORRECT CATEGORY 

    def return_all_Flash_Assists(self):
        FA_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            FA_list.append(float(children[2].text.replace(" ", "")))
        return FA_list
    
    def return_all_Flashed(self):
        Flashed_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            Flashed_list.append(float(children[3].text.replace(" ", "")))
        return Flashed_list
    
    def return_all_Flashed_Teamates(self):
        FlashedT_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            FlashedT_list.append(float(children[4].text.replace(" ", "")))
        return FlashedT_list
    
    def return_all_DPG(self):
        # DPG(Damage Per Granade)
        DPG_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            DPG_list.append(float(children[5].text.replace(" ", "")))
        return DPG_list

    def return_all_DPG_Friendly(self):
        DPGF_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            DPGF_list.append(float(children[6].text.replace(" ", "")))
        return DPGF_list

    def return_all_Unused_Util(self):
        Unused_Util_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            Unused_Util_list.append(int(children[7].text.replace(" $", "")))
        return Unused_Util_list

    def return_all_Smoke_Efficiency(self):
        SE_list = []
        for container in self.get_player_containers():
            children = self.get_children_player_container(container)
            SE_list.append(round(float(children[8].text.replace(" %", ""))/100, 4))
        return SE_list

    def generate_utility_stats_array(self):
        return [self.return_all_Flash_Assists(), 
        self.return_all_Flashed(), 
        self.return_all_Flashed_Teamates(), 
        self.return_all_DPG(), 
        self.return_all_DPG_Friendly(),
        self.return_all_Unused_Util(), 
        self.return_all_Smoke_Efficiency()]

class HLTV_Scraping:
    
    def __init__(self, html_docs_array, player_name):
        self.html_docs_array = html_docs_array
        self.player_name = player_name

    def return_scraper_instances(self):
        html_docs_array = self.html_docs_array
        return [
            self.Individual_Scraping(html_docs_array[1], self.player_name), 
            self.Match_Scraping(html_docs_array[2]),
            self.Career_Scraping(html_docs_array[4]),
            self.Weapons_Scraping(html_docs_array[5]),
            self.Clutch_Scraping(html_docs_array[6]),
            # self.Opponent_Scraping(html_docs_array[7])
        ]

    class Individual_Scraping:

        def __init__(self, html_doc, player_name):
            self.player_name = player_name
            self.html_doc = html_doc
            self.soup = BeautifulSoup(html_doc, 'html.parser')

        def return_stat_row(self):
            soup = self.soup
            stat_rows = soup.find_all(class_="stats-row")
            return stat_rows

        def return_stat_headlines(self):
            soup = self.soup
            stat_headlines = soup.find_all("standard-headline")
            return stat_headlines

        def return_column_stat_row(self):
            soup = self.soup
            column_stat_rows = soup.find_all(class_="col stats-rows")
            return column_stat_rows

        def generate_individual_stat_dict(self, timespan_str):
            player_name = self.player_name
            stat_rows = self.return_stat_row()
            stat_head_lines = self.return_stat_headlines()
            column_stat_rows = self.return_column_stat_row()
            joiner = "_"
            final_dict_name = player_name + "_stats"
            final_dict = {final_dict_name : {timespan_str : {"individual_stats" : {}}}}
            final_dict_loc = final_dict[final_dict_name][timespan_str]["individual_stats"]
            for col in column_stat_rows:
                children = col.find_all('div', recursive=False)
                array = [[children[0], children[1]], [children[3], children[4]]]
                for stats_array in array:
                    
                    stat_headline = stats_array[0].find('span').text.split(" ")
                    subdict_name = joiner.join(stat_headline).lower()
                    stat_rows = stats_array[1].find_all(class_='stats-row')
                    subdict = {subdict_name : {}}
                    subdict_loc = subdict[subdict_name]
                    for stat_row in stat_rows:
                        tags = stat_row.find_all('span')
                        tag_name = tags[0].text
                        tag_stat = tags[-1].text
                        if "%" in tag_stat:
                            tag_stat = convert_perc_to_float(tag_stat)
                        c_pass1 = tag_name.replace("/", "")
                        c_pass2 = c_pass1.replace("-", "")
                        pass1 = c_pass2.split(" ")
                        pass2 = "".join(pass1).split("-")   
                        pass3 = "".join(pass2).split("/")
                        stat_name = joiner.join(pass1).lower()
                        subdict_loc.update({stat_name : float(tag_stat)})
                    final_dict_loc.update(subdict)
            return final_dict
                        



    class Match_Scraping:
        def __init__(self, html_doc):
            pass
    
    class Career_Scraping:
        def __init__(self, html_doc):
            pass
    
    class Weapons_Scraping:
        def __init__(self, html_doc):
            pass
    
    class Clutch_Scraping:
        def __init__(self, html_doc):
            pass
    
    class Opponent_Scraping:
        def __init__(self, html_doc):
            pass



# with open("html_docs_database.json", "r") as json_file:
#     obj = json.load(json_file)
#     obj_keys = list(obj.keys())
# for key in obj_keys:
#     html_docs = obj[key]
#     print(len(html_docs))
#     hltv_inst = HLTV_Scraping(html_docs, key.replace("_docs", ""))
#     indiv_inst = hltv_inst.return_scraper_instances()[0]
#     dict = indiv_inst.generate_individual_stat_dict()
#     with open("test_db.json", "w", newline="") as file:
#         json.dump(dict, file, indent=4)

# print(obj["ZywOo_docs"][0])
# with open("test.txt", "w", newline="") as txt:
#     txt.write(obj["ZywOo_docs"][0])




# print(HLTV_Scraping(["yup", "yup", "yup", "yup", "yup", "yup", "yup", "yup"]).return_scraper_instances())

        




# wt = webdriver_tools("https://www.hltv.org/stats/players")
# driver = wt.return_driver_instance()

# class_ = webdriver_tools("https://esports.leetify.com/stats")

# driver = class_.return_driver_instance()
# driver.implicitly_wait(10)
# general_selections = class_.find_all_element_with_xpath("//div[@class='mb-2']")
# stats_selections = general_selections[0]
# timespan_selections = general_selections[1]
# generals = stats_selections.find_elements_by_tag_name('button')
# timespans = timespan_selections.find_elements_by_tag_name('button')
# class_.click_button(generals[2])
# driver.find_element_by_class_name("pagination-next").click()
# html_doc = driver.page_source
# inst = Esports_Leetify_Scraping(html_doc)


# pprint.pprint(inst.generate_general_stats_array())

# wt = webdriver_tools("https://www.hltv.org/stats/players")

# driver = wt.return_driver_instance()
# driver.implicitly_wait(10)
# table_rows = driver.find_elements_by_class_name('playerCol')
# element_list = []
# href_list = []
# for tr in table_rows:
#     try:
#         href_list.append(tr.find_element_by_tag_name('a').get_attribute('href'))
#     except:
#         print("first lol")







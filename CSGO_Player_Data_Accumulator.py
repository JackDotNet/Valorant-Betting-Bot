from Scraping_Tools import webdriver_tools as wt
from Scraping_Tools import Esports_Leetify_Scraping
from Scraping_Tools import HLTV_Scraping
from bs4 import BeautifulSoup
import pprint
from collections import OrderedDict
import json
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
import selenium





class Data_Accumulation_Routine_ELS:

    def __init__(self, link, db_file_name):
        self.wt_inst = wt(link)
        self.db_file_name = db_file_name
        self.driver = self.wt_inst.return_driver_instance()

    def generate_html_docs(self):
        wt_inst = self.wt_inst
        driver = self.driver
        driver.implicitly_wait(10)
        general_selections = wt_inst.find_all_element_with_xpath("//div[@class='mb-2']")
        stats_selections = general_selections[0]
        timespan_selections = general_selections[1]
        generals = stats_selections.find_elements_by_tag_name('button')
        timespans = timespan_selections.find_elements_by_tag_name('button')
        page_number = int(driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").text)
        html_docs = []
        for timespan in timespans:
            timespan.click()
            for general_selection in generals:
                general_selection.click()
                page_number = int(driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").text)
                driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").click()
                for page in range(page_number-1):
                    html_docs.append(driver.page_source)
                    # print(driver.page_source)
                    driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[1]/a").click()
                html_docs.append(driver.page_source)

        return html_docs

    def generate_html_docs_one_year(self):
        wt_inst = self.wt_inst
        driver = self.driver
        driver.implicitly_wait(10)
        general_selections = wt_inst.find_all_element_with_xpath("//div[@class='mb-2']")
        stats_selections = general_selections[0]
        timespan_selections = general_selections[1]
        generals = stats_selections.find_elements_by_tag_name('button')
        timespan_selections.find_elements_by_tag_name('button')[3].click()
        general_list = []
        aim_list = []
        utility_list = []
        html_docs_array = [general_list, aim_list, utility_list]
        index_num = 0
        for general_selection in generals:
            list_to_append = html_docs_array[index_num]
            general_selection.click()
            page_number = int(driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").text)
            driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").click()
            for page in range(page_number-1):
                # print(driver.page_source)
                list_to_append.append(driver.page_source)
                # print(driver.page_source)
                driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[1]/a").click()
            list_to_append.append(driver.page_source)
            index_num+=1
        return html_docs_array

    # THE FOLLOWING FUNCTIONS DO NOT WORK CORRECTLY
    # FOR NOW USE THE ONE YEAR FUNCTION UNTIL ISSUE IS
    # REOSLVED

    def generate_html_docs_six_month(self):
        # To Do:
        # Figure out why this function spits out random
        # inconsistent characters that make no sense
        wt_inst = self.wt_inst
        driver = self.driver
        driver.implicitly_wait(10)
        general_selections = wt_inst.find_all_element_with_xpath("//div[@class='mb-2']")
        stats_selections = general_selections[0]
        timespan_selections = general_selections[1]
        generals = stats_selections.find_elements_by_tag_name('button')
        timespan_selections.find_elements_by_tag_name('button')[2].click()
        html_docs = []
        for general_selection in generals:
            general_selection.click()
            page_number = int(driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").text)
            driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").click()
            for page in range(page_number-1):
                html_docs.append(driver.page_source)
                # print(driver.page_source)
                driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[1]/a").click()
        return html_docs

    def generate_html_docs_three_month(self):
        # To Do:
        # Figure out why this function spits out random
        # inconsistent characters that make no sense
        wt_inst = self.wt_inst
        driver = self.driver
        driver.implicitly_wait(10)
        general_selections = wt_inst.find_all_element_with_xpath("//div[@class='mb-2']")
        stats_selections = general_selections[0]
        timespan_selections = general_selections[1]
        generals = stats_selections.find_elements_by_tag_name('button')
        timespan_selections.find_elements_by_tag_name('button')[1].click()
        html_docs = []
        for general_selection in generals:
            general_selection.click()
            page_number = int(driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").text)
            driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").click()
            for page in range(page_number-1):
                html_docs.append(driver.page_source)
                # print(driver.page_source)
                driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[1]/a").click()
        return html_docs

    def generate_html_docs_one_month(self):
        # To Do:
        # Figure out why this function spits out random
        # inconsistent characters that make no sense
        wt_inst = self.wt_inst
        driver = self.driver
        driver.implicitly_wait(10)
        general_selections = wt_inst.find_all_element_with_xpath("//div[@class='mb-2']")
        stats_selections = general_selections[0]
        timespan_selections = general_selections[1]
        generals = stats_selections.find_elements_by_tag_name('button')
        timespan_selections.find_elements_by_tag_name('button')[0].click()
        html_docs = []
        for general_selection in generals:
            driver.implicitly_wait(10)
            general_selection.click()
            page_number = int(driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").text)
            driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[9]/a/span[2]").click()
            for page in range(page_number-1):
                driver.implicitly_wait(10)
                html_docs.append(driver.page_source)
                # print(driver.page_source)
                driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[1]/a").click()
        return html_docs

    def generate_player_name_set(self):
        html_docs = self.generate_html_docs()
        player_names = []
        for html_doc in html_docs:
            ELS_inst = Esports_Leetify_Scraping(html_doc)
            player_names.extend(ELS_inst.return_all_player_names())
        return list(set(player_names))

    def generate_player_dicts_and_dump(self, file_name):
        player_names = self.generate_player_name_set()
        print(len(player_names))
        all_player_stats_dict = {}
        player_index_num = 0
        for player_name in player_names:
            player_stats_dict = {
                "player_"+player_name : {
                    "player_name": player_name ,player_name + "_stats" : {
                        "one_year_stats_dict" : {
                            "general_dict" : {},
                            "aim_dict" : {},
                            "utility_dict" : {}
                        },
                        "six_month_stats_dict" : {
                            "general_dict" : {},
                            "aim_dict" : {},
                            "utility_dict" : {}
                        },
                        "three_month_stats_dict" : {
                            "general_dict" : {},
                            "aim_dict" : {},
                            "utility_dict" : {}
                        },
                        "one_month_stats_dict" : {
                            "general_dict" : {},
                            "aim_dict" : {},
                            "utility_dict" : {}
                        }
                    }
                }
            }
            all_player_stats_dict.update(player_stats_dict)
            player_index_num += 1
        with open(file_name, 'w', newline="") as json_file:
            json.dump(OrderedDict(all_player_stats_dict), json_file, indent=4)
        return OrderedDict(all_player_stats_dict)
    
    def generate_general_stats_dicts_and_dump(self, html_docs_array, dict_timespan_index_str):
        player_dicts = json.load(open(self.db_file_name))
        # print(html_docs_array[0])
        print(len(html_docs_array[0]), len(html_docs_array[1]), len(html_docs_array[2]))
        for doc in html_docs_array[0]:
            
            ELS_inst = Esports_Leetify_Scraping(doc)
            player_list = ELS_inst.return_all_player_names()
            general_stats_array = ELS_inst.generate_general_stats_array()
            index_num = 0
            for player in player_list:
                one_year_general_stats_dict = None
                try:
                    one_year_general_stats_dict = {
                        "general_dict" : {
                            "hltv_rating" : general_stats_array[1][index_num],
                            "adr" : general_stats_array[2][index_num],
                            "average_kd" : general_stats_array[3][index_num],
                            "kpr" : general_stats_array[4][index_num],
                            "dpr" : general_stats_array[5][index_num],
                            "rounds_survived" : general_stats_array[6][index_num]
                        }
                    }
                    
                    indexed_player_dict = player_dicts["player_" + str(player)][str(player) +  "_stats"][dict_timespan_index_str]
                    indexed_player_dict.update(one_year_general_stats_dict)

                except:
                    "Skipped Generating Dict"

                
                index_num+=1 
        with open(self.db_file_name, 'w', newline="") as json_file:
            json.dump(player_dicts, json_file, indent=4)
        return player_dicts

    def generate_aim_stats_dicts_and_dump(self, html_docs_array, dict_timespan_index_str):
        player_dicts = json.load(open(self.db_file_name))
        # print(html_docs_array[1])
        for doc in html_docs_array[1]:
            
            ELS_inst = Esports_Leetify_Scraping(doc)
            player_list = ELS_inst.return_all_player_names()
            aim_stats_array = ELS_inst.generate_aim_stats_array()
            index_num = 0
            for player in player_list:
                one_year_general_stats_dict = None
                try:
                    one_year_general_stats_dict = {
                        "aim_dict" : {
                            "hs_percentage" : aim_stats_array[0][index_num],
                            "accuracy_on_spot" : aim_stats_array[1][index_num],
                            "accuracy_on_all" : aim_stats_array[2][index_num],
                            "spray_accuracy" : aim_stats_array[3][index_num],
                            "counter_strafe" : aim_stats_array[4][index_num],
                            "crosshair_placement" : aim_stats_array[5][index_num],
                            "time_to_damage" : aim_stats_array[6][index_num]

                        }
                        
                    }
                    
                    indexed_player_dict = player_dicts["player_" + str(player)][str(player) +  "_stats"][dict_timespan_index_str]
                    indexed_player_dict.update(one_year_general_stats_dict)

                except:
                    "Skipped Generating Dict"

                
                index_num+=1 
        with open(self.db_file_name, 'w', newline="") as json_file:
            json.dump(player_dicts, json_file, indent=4)
        return player_dicts
    
    def generate_utility_stats_dicts_and_dump(self, html_docs_array, dict_timespan_index_str):
        player_dicts = json.load(open(self.db_file_name))
        # print(html_docs_array[2])
        for doc in html_docs_array[2]:
            
            ELS_inst = Esports_Leetify_Scraping(doc)
            player_list = ELS_inst.return_all_player_names()
            utility_stats_array = ELS_inst.generate_utility_stats_array()
            index_num = 0
            for player in player_list:
                one_year_general_stats_dict = None
                try:
                    one_year_general_stats_dict = {
                        "utility_dict" : {
                            "flash_assists" : utility_stats_array[0][index_num],
                            "flashed_per_flash" : utility_stats_array[1][index_num],
                            "flashed_per_flash_friendly" : utility_stats_array[2][index_num],
                            "damage_per_grenade" : utility_stats_array[3][index_num],
                            "damage_per_grenade_friendly" : utility_stats_array[4][index_num],
                            "unused_utility" : utility_stats_array[5][index_num],
                            "smoke_efficiency" : utility_stats_array[6][index_num]

                        }
                        
                    }
                    
                    indexed_player_dict = player_dicts["player_" + str(player)][str(player) +  "_stats"][dict_timespan_index_str]
                    indexed_player_dict.update(one_year_general_stats_dict)

                except:
                    "Skipped Generating Dict"

                
                index_num+=1 
        with open(self.db_file_name, 'w', newline="") as json_file:
            json.dump(player_dicts, json_file, indent=4)
        return player_dicts
    
    def generate_and_dump_all_player_dicts(self, time_span_string):
        html_docs = self.generate_html_docs_one_year()
        self.generate_player_dicts_and_dump(self.db_file_name)
        self.generate_general_stats_dicts_and_dump(html_docs, time_span_string)
        self.generate_aim_stats_dicts_and_dump(html_docs, time_span_string)
        self.generate_utility_stats_dicts_and_dump(html_docs, time_span_string)

class Data_Accumulation_Routine_HLTV:

    def __init__(self, player_list_link, player_data_links, html_doc_database, player_stat_database):
        self.player_list_link = player_list_link
        self.player_stat_database = player_stat_database
        self.player_data_links = player_data_links
        self.html_doc_database = html_doc_database
        self.wt_inst = wt(player_list_link)

    def initialize_player_stat_db(self, name):
        self.wt_inst.return_driver_instance().quit()
        with open(self.player_stat_database, "w", newline="") as json_file:
            json.dump({"player_data_base" : name,
            "date_created" : time.time(),
            "database" : {}}, json_file)

    def accumulate_player_data_links_loop(self):

        wt_inst = self.wt_inst

        driver = wt_inst.return_driver_instance()
        driver.implicitly_wait(10)
        table_rows = driver.find_elements_by_class_name('playerCol')
        element_list = []
        href_list = []
        for tr in table_rows:
            try:
                href = tr.find_element_by_tag_name('a').get_attribute('href')
                href_list.append(href)
                yield href
            except:
                print("href does not exist")
        driver.quit()

    def accumulate_player_html_docs_loop(self):
        # returns an array of lists for each players stats tabs

        # this function is supa dupa jank rn, I might fix it later but 
        # we all know that isn't happening 

        # gets all the player stat links



        self.wt_inst.return_driver_instance().quit()
        with open(self.player_data_links, "r") as text_file:
            player_href_list = self.get_rid_of_newline_str(text_file.readlines())
        for player_link in player_href_list:
            temp_player_stats_docs = []
            wt_inst = wt(player_link)
            driver = wt_inst.return_driver_instance()
            driver.implicitly_wait(2)
            try:
                selections_to_make = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/div").find_elements_by_tag_name('a')
            except:
                selections_to_make = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div").find_elements_by_tag_name('a')

            base_xpath = "/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div/a"
            alternate_xpath = "/html/body/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/div/a"
  
            index_num = 2
            for i_num in range(len(selections_to_make)-1):
                try:
                    xpath = base_xpath + "[" + str(index_num) + "]"
                    alt_xpath = alternate_xpath + "[" + str(index_num) + "]"
                    html_doc = driver.find_element_by_class_name("contentCol").get_attribute("innerHTML")
                    temp_player_stats_docs.append(html_doc)
                    try:
                        
                        driver.find_element_by_xpath(xpath).click()
                    except:
                        driver.find_element_by_xpath(alt_xpath).click()
                except:
                    print("critical error when accumulating html docs, could not find xpaths\nxpath: " + xpath + "\nalt_xpath: " + alt_xpath)
            
                
                index_num+=1

            
            temp_player_stats_docs.append(driver.find_element_by_class_name("contentCol").get_attribute("innerHTML"))
            driver.quit()
            yield temp_player_stats_docs
            

    
    def dump_player_data_links(self):
        for player_data_link in self.accumulate_player_data_links_loop():
            with open(self.player_data_links, "a", newline="") as text_file:
                text_file.write(player_data_link + "\n")

    def dump_player_stat_dicts(self):
        # this function assumes a self.initialize_player_stat_db has already been ran
        self.wt_inst.return_driver_instance().quit()
        player_stat_json_obj = json.load(open(self.player_stat_database))
        database_loc = player_stat_json_obj["database"]
        html_docs_json_obj = json.load(open(self.html_doc_database))
        html_doc_keys = list(html_docs_json_obj.keys())
        for key in html_doc_keys:
            html_doc_array = html_docs_json_obj[key]
            player_name = key.split("_")[0]
            HlTV_inst = HLTV_Scraping(html_doc_array, player_name)
            Scraper_ints_array = HlTV_inst.return_scraper_instances()
            Indiv_inst = Scraper_ints_array[0]
            Indiv_dict = Indiv_inst.generate_individual_stat_dict("one_year")
            database_loc.update(Indiv_dict)
            with open(self.player_stat_database, "w", newline="") as json_file:
                json.dump(player_stat_json_obj, json_file, indent=4)



    def dump_player_data_html_docs(self):
    # To Do:
    # rework the html doc dict frame work to create a new file for each dict
    # accessing one json file with as much data as we collect, is to much for
    # the gui controller to handle, simply requesting data from the json file
    # alone freezes up the gui controller


        for html_docs in self.accumulate_player_html_docs_loop():
            soup = BeautifulSoup(html_docs[0], 'html.parser')
            player_name = soup.find(class_="summaryNickname text-ellipsis").text
            doc_dict = {player_name + "_docs" : html_docs}
            current_obj = json.load(open(self.html_doc_database)) 
            current_obj.update(doc_dict)
            with open(self.html_doc_database, "w") as json_database:
                json.dump(current_obj, json_database, indent=4)
    
    def clear_player_data_link_db(self):
        with open(self.player_data_links, "w") as text_file:
            text_file.write("")

    def get_rid_of_newline_str(self, list_of_lines):
        new_list = []
        for line in list_of_lines:
            new_list.append(line.replace("\n", ""))
        return new_list






        



# DAR_HLTV = Data_Accumulation_Routine_HLTV("https://www.hltv.org/stats/players", "test_text_file.txt", "html_docs_database.json", "Player_Data_Archive.json")
# DAR_HLTV.clear_player_data_link_db("test_text_file.txt")
# DAR_HLTV.initialize_player_stat_db("Player Data Archive")
# DAR_HLTV.dump_player_stat_dicts()

# with open("test_text_file.txt", "r") as text_file:
#     print(DAR_HLTV.get_rid_of_newlin_str(text_file.readlines()))


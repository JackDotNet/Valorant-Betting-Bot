from vlrgg_scraper import Player
from vlrgg_scraper import VLRGG_Scraping
import requests
import pprint

html_doc = requests.get("https://www.vlr.gg/stats").content


Scraping_instance = VLRGG_Scraping(html_doc)
player_names = Scraping_instance.get_all_player_name()
player_teams = Scraping_instance.get_all_player_teams()
rounds_played = Scraping_instance.get_all_rounds_played()
avergae_combat_scores = Scraping_instance.get_all_ACS()
player_KDs = Scraping_instance.get_all_players_KD()
average_damage_round = Scraping_instance.get_all_players_ADR()
kills_round = Scraping_instance.get_all_players_KPR()
assists_round = Scraping_instance.get_all_players_APR()
first_kills_round = Scraping_instance.get_all_players_FKPR()
first_death_round = Scraping_instance.get_all_players_First_Deaths()
hs_percentage = Scraping_instance.get_all_players_HS_Perc()
cl_percentage = Scraping_instance.get_all_players_Clutch_Percentage()
max_kills = Scraping_instance.get_all_players_KMax()
kills = Scraping_instance.get_all_players_Total_Kills()
deaths = Scraping_instance.get_all_players_Total_Deaths()
assists = Scraping_instance.get_all_players_Total_Assists()
first_kills = Scraping_instance.get_all_players_First_Kills()
first_deaths = Scraping_instance.get_all_players_First_Deaths()
index_num = 0
player_stats_obj_list = []

for player in player_names:
    player_name = player_names[index_num]
    player_team = player_teams[index_num]
    player_rounds_played = rounds_played[index_num]
    player_ACS = avergae_combat_scores[index_num]
    player_KD = player_KDs[index_num]
    player_ADR = average_damage_round[index_num]
    player_KPR = kills_round[index_num]
    player_APR = assists_round[index_num]
    player_FKPR = first_kills_round[index_num]
    player_FDPR = first_death_round[index_num]
    player_HS_Perc = hs_percentage[index_num]
    player_CL_Perc = cl_percentage[index_num]
    player_KMAX = max_kills[index_num]
    player_kills = kills[index_num]
    player_deaths = deaths[index_num]
    player_assists = assists[index_num]
    player_FK = first_kills[index_num]
    player_FD = first_deaths[index_num]


    New_Player = Player(player_name, player_team, player_rounds_played=player_rounds_played,
    player_ACS=player_ACS, player_KD=player_KD, player_ADR=player_ADR, player_KPR=player_KPR,
    player_APR=player_APR, player_FKPR=player_FKPR, player_FDPR=player_FDPR, player_HS_Perc=player_HS_Perc,
    player_CL_Perc=player_CL_Perc, player_KMAX=player_KMAX, player_kills=player_kills, player_deaths=player_deaths,
    player_assists=player_assists, player_FK=player_FK, player_FD=player_FD)


    player_stats_obj_list.append(New_Player)
    index_num+=1

# print(player_stats_obj_list)\


for player_obj in player_stats_obj_list:
    stats_dict = player_obj.generate_stats_dict()
    pprint.pprint(stats_dict)

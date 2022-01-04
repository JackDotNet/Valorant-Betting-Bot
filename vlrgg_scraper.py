from bs4 import BeautifulSoup
import requests
import math




class Player:

    def __init__(self, name, team, **stats):
        self.name = name
        self.team = team
        self.stats = stats
    
    def get_name(self):
        return self.name

    def get_team(self):
        return self.team
    
    def generate_stats_dict(self):
        stats = self.stats
        keys = list(self.stats.keys())
        init_dict = {
        "name" : self.get_name(), 
        "team" : self.get_team(),
        "stats" : {}
        }
        for key in keys:
            init_dict["stats"].update({key : stats[key]}) 
        return init_dict


class VLRGG_Scraping:
    # class used to scrape vlr.gg
    # it is intended to be used to accumulate 
    # alot of player data really fast and to
    # be orginized late, so you can't get a single
    # players' stats, only get all at once. It is 
    # faster to index that data once you have it in 
    # memory and don't have to use an html parser


    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def get_all_player_containers(self):
        rows = self.soup.find_all('tr')

        # theres a blank table row that shows where each stat is so we remove it
        rows.pop(0)
        return rows

    def get_children_for_player_instance(self, player_instance):
        return player_instance.find_all('td')


    def get_all_player_name(self):
        player_containers = self.get_all_player_containers()
        player_name_list = []
        for player in player_containers:
            player_name_list.append(player.find(class_="text-of").text)
        return player_name_list

    def get_all_player_teams(self):
        player_containers = self.get_all_player_containers()
        player_team_list = []
        for player in player_containers:
            player_team_list.append(player.find(class_="stats-player-country").text)
        return player_team_list

    def get_all_rounds_played(self):
        player_containers = self.get_all_player_containers()
        rounds_played_list = []
        for player in player_containers:
            rounds_played_list.append(int(player.find(class_="mod-rnd").text))
        return rounds_played_list
    
    def get_all_ACS(self):
        # ACS (Average Combat Score)
        player_containers = self.get_all_player_containers()  
        ACS_list = []
        for player in player_containers:
            ACS_list.append(float(player.find(class_="mod-color-sq mod-acs").find('span').text))
        return ACS_list

    def get_all_players_KD(self):
        player_containers = self.get_all_player_containers() 
        KD_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            KD_list.append(float(children[4].find('span').text))
        return KD_list

    def get_all_players_ADR(self):
        # ADR(Average Damage per Round)
        player_containers = self.get_all_player_containers() 
        ADR_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            ADR_list.append(float(children[5].find('span').text))
        return ADR_list
    
    def get_all_players_KPR(self):
        # KPR(Kills Per Round)
        player_containers = self.get_all_player_containers() 
        KPR_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            KPR_list.append(float(children[6].find('span').text))
        return KPR_list

    def get_all_players_APR(self):
        # APR(Assists per Round)
        player_containers = self.get_all_player_containers() 
        APR_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            APR_list.append(float(children[7].find('span').text))
        return APR_list

    def get_all_players_FKPR(self):
        # FKPR(First Kills per Round)
        player_containers = self.get_all_player_containers() 
        FKPR_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            FKPR_list.append(float(children[8].find('span').text))
        return FKPR_list

    def get_all_players_FDPR(self):
        # FDPR(First Death per Round)
        player_containers = self.get_all_player_containers() 
        FDPR_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            FDPR_list.append(float(children[9].find('span').text))
        return FDPR_list
    
    def get_all_players_HS_Perc(self):

        # returns a ratio of how many headshots a player gets per kill
        # headshot percentage

        player_containers = self.get_all_player_containers() 
        HS_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            raw_output = float(children[10].find('span').text.split("%")[0])
            final_output = raw_output/100
            HS_list.append(final_output)
        return HS_list

    def get_all_players_Clutch_Percentage(self):
        player_containers = self.get_all_player_containers() 
        CL_Perc_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            try:
                raw_output = float(children[11].find('span').text.split("%")[0])            
                final_output = raw_output/100
            except ValueError:
                final_output = 0
            CL_Perc_list.append(final_output)
        return CL_Perc_list
    
    def get_all_players_KMax(self):
        player_containers = self.get_all_player_containers() 
        KMax_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            KMax_list.append(int(children[13].find('a').text.replace(" ", "")))
        return KMax_list
    
    def get_all_players_Total_Kills(self):
        player_containers = self.get_all_player_containers() 
        TKills_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            TKills_list.append(int(children[14].text))
        return TKills_list
    
    def get_all_players_Total_Deaths(self):
        player_containers = self.get_all_player_containers() 
        TDeaths_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            TDeaths_list.append(int(children[15].text))
        return TDeaths_list
    
    def get_all_players_Total_Assists(self):
        player_containers = self.get_all_player_containers() 
        TAssists_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            TAssists_list.append(int(children[16].text))
        return TAssists_list
    
    def get_all_players_First_Kills(self):
        player_containers = self.get_all_player_containers() 
        FK_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            FK_list.append(int(children[17].text))
        return FK_list

    def get_all_players_First_Deaths(self):
        player_containers = self.get_all_player_containers() 
        FD_list = []

        for player in player_containers:
            children = self.get_children_for_player_instance(player)
            FD_list.append(int(children[18].text))
        return FD_list

class THESPIKEGG_Scraping:

    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def get_all_player_containers(self):
        soup = self.soup
        player_containers = soup.find_all('tr')
        player_containers.pop(0)
        return player_containers

    def get_children_of_player_cont_inst(self, player_cont_instance):

        return player_cont_instance.findChildren()

    def get_all_player_names(self):
        soup = self.soup
        player_containers = self.get_all_player_containers()
        player_name_list = []
        for player_cont in player_containers:
            player_name_list.append(player_cont.find(class_="player-info").text)
        return player_name_list
    
    def get_all_player_rounds_played(self):
        rounds_played_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            rounds_played_list.append(int(children[5].text))

        return rounds_played_list

    def get_all_players_ACS(self):
        # ACS(Average Combat Score)
        ACS_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            ACS_list.append(float(children[7].text))
        return ACS_list
    
    def get_all_players_KD(self):
        # KD(Kill Death Ratio)
        KD_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            KD_list.append(float(children[8].text))
        return KD_list

    def get_all_players_ADR(self):
        # ADR(Average Damage per Round)
        ADR_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            ADR_list.append(float(children[9].text))
        return ADR_list
    
    def get_all_players_KPR(self):
        # KPR(Kill Per Round)
        KPR_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            KPR_list.append(float(children[10].text))
        return KPR_list
    
    def get_all_players_DPR(self):
        # DPR(Deaths Per Round)
        DPR_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            DPR_list.append(float(children[11].text))
        return DPR_list

    def get_all_players_APR(self):
        # APR(Assists Per Round)
        APR_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            APR_list.append(float(children[12].text))
        return APR_list

    def get_all_players_FBPR(self):
        # FBPR(First Bloods Per Round)
        FBPR_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            FBPR_list.append(float(children[13].text))
        return FBPR_list
            
    def get_all_players_FDPR(self):
        # FDPR(First Deaths Per Round)
        FDPR_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            FDPR_list.append(float(children[14].text))
        return FDPR_list
    
    def get_all_players_HS_Percentage(self):
        HS_Perc_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            HS_Perc_list.append(float(children[16].text.split("%")[0])/100)
        return HS_Perc_list
    
    def get_all_players_ESR(self):
        # ESR(Entry Success Rate)
        ESR_Perc_list = []
        for player_cont in self.get_all_player_containers():
            children = self.get_children_of_player_cont_inst(player_cont)
            ESR_Perc_list.append(float(children[16].text.split("%")[0])/100)
        return ESR_Perc_list

html_doc = requests.get("https://www.thespike.gg/stats/players?rounds=0300&region=all&date=90&map=all&agent=all&team_rank=all").content

print(THESPIKEGG_Scraping(html_doc).get_all_players_ESR())
import json
import pprint


json_file = "PLayer_Data_Archive.json"
link = "https://esports.leetify.com/stats"
json_obj = json.load(open(json_file))

class player_data_indexer:

    def __init__(self, json_obj):
        self.json_obj = json_obj

    def return_json_obj(self):
        return self.json_obj

    def get_player_data(self, player_name):
        # returns a dict with player data
        json_obj = self.json_obj
        # print(json_obj["player_" + player_name])
        return json_obj["player_" + player_name]

    def return_general_dict_loc(self, player_name, timespan_dict_str):
        return self.get_player_data(player_name)[player_name + str("_stats")][timespan_dict_str]['general_dict']
    
    def return_aim_dict_loc(self, player_name, timespan_dict_str):
        return self.get_player_data(player_name)[player_name + str("_stats")][timespan_dict_str]['aim_dict']
    
    def return_utility_dict_loc(self, player_name, timespan_dict_str):
        return self.get_player_data(player_name)[player_name + str("_stats")][timespan_dict_str]['utility_dict']

    def return_subset_dict(self, player_name, timespan_dict_str, stats_dict_str):
        return self.get_player_data(player_name)[player_name + str("_stats")][timespan_dict_str][stats_dict_str]
    
    def get_player_stat(self, player_name, timespan_dict_str, stats_dict_str, stats_str):
        return {stats_str : self.return_subset_dict(player_name, timespan_dict_str, stats_dict_str)[stats_str]}
    
    def get_player_data_per_timespan(self, player_name, timespan_dict_str):
        json_obj = self.get_player_data(player_name)
        return json_obj[player_name+"_stats"][timespan_dict_str]

    def return_player_data_dict_array(self, player_name, timespan_dict_str):
        # json_obj = self.get_player_data_per_timespan(player_name, timespan_dict_str)
        json_obj = json.load(open("Player_Data_Archive.json"))
        player_dict = json_obj["database"][player_name + "_stats"]["one_year"]["individual_stats"]
        subset_dict_keys = list(player_dict.keys())
        data_dict_array = []
        for key in list(subset_dict_keys):
            dict_loc = player_dict[key]
            lower_subset_keys = dict_loc.keys()
            lower_stat_list = []
            for lower_key in list(lower_subset_keys):
                lower_stat_list.append({lower_key : dict_loc[lower_key]})
            data_dict_array.append({key : lower_stat_list})

        return data_dict_array


    # def return_averaged_team_stat(self, stat, timespan_dict_str, *player_names):
        
    
    def return_get_team_stats(self, team_name, timespan_dict_str, *player_names):

        # The most complicated function by far, what a fucking headache
        # a lot of disguisting code that I'm to lazy to fix if I'm honest
        # i will now explain


        # we must first get all the player_data_dict_arrays and put them in a list
        player_data_dict_arrays = []
        for player in player_names:
            # if you would like to see what the output of this function looks like, visit the "return_player_data_dict_array" function
            try:
                player_data_dict_arrays.append(self.return_player_data_dict_array(player, timespan_dict_str))
            except KeyError:
                print("player does not exist in player database.")

        # we declare what the final dict will look like
        final_dict = {"team_name" : team_name,
        team_name + "_stats" : {}}

        # making it easier to update the "team_name_stats" dict
        team_stats_loc = final_dict[team_name + "_stats"]

        # template dict we can use to get keys from to use in final dict
        array = player_data_dict_arrays[0]

        for x in range(len(array)):
            # get the current player_data_dict_array from the list
            current_subset_dict = array[x]
            # get the keys of that dict
            current_subset_dict_key = list(current_subset_dict.keys())[0]
            # get the stat list of that subset dict
            stat_list = current_subset_dict[current_subset_dict_key]

            # declaring the stat_key_list for creating the final dict
            stat_key_list = []

            # get the current subset key name so we can add it to the final dict
            team_stats_loc_key = list(array[x].keys())[0]
            # adding it to the final dict with a blank dict
            team_stats_loc.update({ team_stats_loc_key : {}})
            # setting the current final dict location to the one we just updated
            subset_dict_loc = team_stats_loc[team_stats_loc_key]


            for y in range(len(stat_list)):
                # adding the current key to the "stat_key_list" to index "player_stat_dict_array" values
                stat_key_list.append(list(stat_list[y].keys())[0])

                # creating a temp list that accumulates the indexed stat list value
                stat_array = []

                for player_data_dict_array in player_data_dict_arrays:
                    # appending the values to the list
                    stat_array.append(player_data_dict_array[x][current_subset_dict_key][y][stat_key_list[y]])

                # updating the final dict to add the average values
                subset_dict_loc.update({stat_key_list[y] : round(sum(stat_array) / len(stat_array), 4)})

        return final_dict               



                
                


            # for player_data_dict in player_data_dict_arrays:
            #     current_dict = player_data_dict[i]
            #     current_dict_key = list(current_dict.keys())[0]
            #     stat_list = current_dict[current_dict_key]
            #     for n in range(len(stat_list)):
            #         print(stat_list[n])



                

            
            
        

    



# pprint.pprint(player_data_indexer(json_obj).return_get_team_stats("wut", "one_year", "ZywOo", "s1mple", "sh1ro", "Kaze", "degster"), indent=4)
# pprint.pprint(player_data_indexer(json_obj).return_get_team_stats("forZe", "one_year_stats_dict", "xsepower", "Jerry", "FL1T", "facecrack", "almazer"), indent=4)

        

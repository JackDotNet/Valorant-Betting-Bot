from CSGO_Player_Data_Accumulator import Data_Accumulation_Routine_ELS as DAR
from CSGO_Player_Data_Accumulator import Data_Accumulation_Routine_HLTV as DAR_HLTV

link = "https://esports.leetify.com/stats"
db_file_name = "player_database.json"

DAR_Inst = DAR_HLTV("https://www.hltv.org/stats/players", "test_text_file.txt", "html_docs_database.json", "Player_Data_Archive.json")
DAR_Inst.dump_player_stat_dicts()

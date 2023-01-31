from datetime import date, datetime

class NintendoSwitchGame:
    def __init__(self, name, release_date, publisher, developer, single_player_and_cat = None, multiplayer_type = None, age_rating = None):
        self.name = name #String
        #This is a list. The first element in the list is the North American release date. Second element should be Japan
        self.release_date = release_date
        self.publisher = publisher #String
        self.developer = developer #This should be a list as there are multiple developers some times.
        self.single_player_and_cat = single_player_and_cat #This is a list, will return True if there's anything in it.
        self.multiplayer_type = multiplayer_type #This is a list, will return True if there's anything in it.
        self.age_rating = age_rating
    
    def __repr__(self):
        return self.name

    def NA_release_date(self):
        dt = datetime(*self.release_date[0])
        return dt.strftime("%d %B %Y")
        # return date(*self.release_date[0])

    def JP_release_date(self):
        dt = datetime(*self.release_date[1])
        return dt.strftime("%d %B %Y")

    def is_single_player(self):
        return bool(self.single_player_and_cat)

    def is_multi_player(self):
        return bool(self.multiplayer_type)

    def type_of_game(self):
        #3 lists are declared. One for all the categories, another for single player/genres and last one for type of multiplayer game/mode.
        categories_list = []
        categories_singleP = []
        categories_multiP = []
        if self.is_single_player():
            categories_list.append("Single Player")
            for each in self.single_player_and_cat:
                categories_list.append(each)
                categories_singleP.append(each)
        if self.is_multi_player():
            categories_list.append("Multiplayer")
            for each in self.multiplayer_type:
                categories_list.append(each)
                categories_multiP.append(each)
        return categories_list, categories_singleP, categories_multiP




if __name__ == "__main__":
    game_00001 = NintendoSwitchGame("The Legend of Zelda: Breath of the Wild", [[2017, 3, 3]],"Nintendo" ,"Nintendo EPD", ["Action-Adventure"])
    game_00002 = NintendoSwitchGame("Mario Kart 8 Deluxe", [[2017, 4, 28]],"Nintendo" ,"Nintendo EPD", ["Kart racing"], ["Split Screen", "Online"])
    game_00003 = NintendoSwitchGame("ARMS", [[2017, 6, 16]],"Nintendo" ,"Nintendo EPD", ["Fighting", "Sports"], ["Split Screen"])
    game_00004 = NintendoSwitchGame("Astral Chain", [[2019, 8, 30]],"Nintendo" ,"PlatinumGames", ["Action-adventure", "hack and slash"], ["Co-Op"])
    game_00005 = NintendoSwitchGame("Daemon X Machina", [[2019, 9, 13]],"Nintendo" ,"Marvelous First Studio", ["Action", "Third-person shooter"], ["PvP", "Online"])
    game_00006 = NintendoSwitchGame("Fire Emblem: Three Houses", [[2019, 7, 29]],"Nintendo" ,"Intelligent Systems", ["Tactical role-playing"])
    game_00007 = NintendoSwitchGame("Fire Emblem Warriors: Three Hopes", [[2022, 6, 24]],"Nintendo" ,"Omega Force", ["Hack and slash", "Action role-playing", "Real-time tactics"], ["Split Screen", "Co-Op"])
    game_00008 = NintendoSwitchGame("Hyrule Warriors: Age of Calamity", [[2020, 11, 20]],"Nintendo" ,"Omega Force", ["Hack and slash", "Action role-playing"], ["Split Screen", "Co-Op"])
    game_00009 = NintendoSwitchGame("Kirby and the Forgotten Land", [[2022, 3, 25]],"Nintendo" ,"HAL Laboratory", ["Platform"], ["Co-Op"])
    print(game_00007.type_of_game())
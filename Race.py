class Race:
    RAGIL = "ragil"
    SPRINT = "sprint"
    def __init__(self, type, ranking, fastest_driver, name):
        self.type = type
        self.ranking = ranking
        self.fastest_driver = fastest_driver
        self.name = name

    def __str__(self):
        return f"{self.type}, {self.ranking}, {self.fastest_driver}, {self.name}"


# def add_race(list_of_all_races):
#     while True:
#         race_type = input("enter: ragil or sprint?")
#         if race_type == "ragil":
#             enter_standing = input("enter list of all drivers from first to tenth and than the fastest driver")
#             split_ranking = enter_standing.split(", ")
#             if len(split_ranking) != 11:
#                 print("you have to enter exactly 11 names. let's try again")
#                 continue
#             # for i in split_ranking:
#             #     if split_ranking[i] not in Driver.all_drivers:
#             if split_ranking[0] not in Driver.all_drivers or split_ranking[1] not in Driver.all_drivers or\
#                     split_ranking[2] not in Driver.all_drivers or split_ranking[3] not in Driver.all_drivers or\
#                     split_ranking[4] not in Driver.all_drivers or split_ranking[5] not in Driver.all_drivers or\
#                     split_ranking[6] not in Driver.all_drivers or split_ranking[7] not in Driver.all_drivers or\
#                     split_ranking[8] not in Driver.all_drivers or split_ranking[9] not in Driver.all_drivers or split_ranking[10] not in Driver.all_drivers:
#                     print("you can only enter drivers names. please try again")
#                     continue
#
#             if split_ranking[0] in split_ranking[1:10] or split_ranking[1] in split_ranking[2:10] or split_ranking[2] in split_ranking[3:10]\
#                     or split_ranking[3] in split_ranking[4:10] or split_ranking[4] in split_ranking[5:10] or split_ranking[5] in split_ranking[6:10]\
#                     or split_ranking[6] in split_ranking[7:10] or split_ranking[7] in split_ranking[8:10] or split_ranking[8] in split_ranking[9:10]\
#                     or split_ranking[9] in split_ranking[10]:
#                 print("every driver can be in only one place except fastest driver")
#                 continue
#             fastest_lap = "nothing"
#             race_name = input("enter race name")
#
#             new_race = Race(race_type, split_ranking, fastest_lap, race_name)
#             list_of_all_races.append(new_race)
#             return new_race
#
#
#         elif race_type == "sprint":
#             enter_standing = input("enter list of all drivers from first to eighth")
#             split_ranking = enter_standing.split(", ")
#             if len(split_ranking) != 8:
#                 print("you have to enter exactly 8 names. let's try again")
#                 continue
#             if split_ranking[0] not in Driver.all_drivers or split_ranking[1] not in Driver.all_drivers or \
#                     split_ranking[2] not in Driver.all_drivers or split_ranking[3] not in Driver.all_drivers or \
#                     split_ranking[4] not in Driver.all_drivers or split_ranking[5] not in Driver.all_drivers or \
#                     split_ranking[6] not in Driver.all_drivers or split_ranking[7] not in Driver.all_drivers:
#                 print("you can only enter drivers names. please try again")
#                 continue
#             if split_ranking[0] in split_ranking[1:7] or split_ranking[1] in split_ranking[2:7] or split_ranking[
#                 2] in split_ranking[3:7] or split_ranking[3] in split_ranking[4:7] or split_ranking[4] in split_ranking[5:7] or \
#                     split_ranking[5] in split_ranking[6:7] or split_ranking[6] in split_ranking[7]:
#                 print("every driver can be in only one place")
#                 continue
#             fastest_lap = "nothing"
#             race_name = input("enter race name")
#
#             new_race = Race(race_type, split_ranking, fastest_lap, race_name)
#             list_of_all_races.append(new_race)
#             return new_race
#
#         else:
#             print("you have to enter ragil or sprint. let's try again")




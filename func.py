import Drivers_And_Teams
from Drivers_And_Teams import Driver
from Race import Race
# from Util import save, load
from Points import ragil_dic, sprint_dic
import ipdb



def read_file():
    all_races = []
    with open("F1_Project.csv", "r") as file_open:
        file_open.readline()
        for line in file_open:
            race_line = line.split(",")
            ranking = [race_line[1], race_line[2], race_line[3], race_line[4], race_line[5], race_line[6]
                ,race_line[7], race_line[8], race_line[9],race_line[10], race_line[11]]
            race = Race(type=race_line[0], ranking=ranking, fastest_driver=race_line[11], name = race_line[12][:-1])
            all_races.append(race)
        return all_races


def get_driver_score(all_races):
        for race in all_races:
            dict_of_drivers = {}
            if race.type == "sprint":
                for race, name_of_driver in enumerate(race.ranking[0:8]):
                    driver = Driver.all_drivers[name_of_driver]
                    driver.score += sprint_dic[race]

            elif race.type == "ragil":
                for race,name_of_driver in enumerate(race.ranking):
                    driver = Driver.all_drivers[name_of_driver]
                    driver.score += ragil_dic[race]


        all_d = Driver.all_drivers
        for key in all_d:
            driver = all_d[key]
            dict_of_drivers[driver.name] = driver.score
            sorted_dict_of_drivers = {k: v for k, v in sorted(dict_of_drivers.items(), key=lambda v: v[1], reverse=True)}
        print(sorted_dict_of_drivers)
        return sorted_dict_of_drivers

def get_team_score(sorted_dict_of_drivers):
    # why not use the teams here?
    Ferrari_score = Drivers_And_Teams.sainz.score + Drivers_And_Teams.leclerc.score
    Red_Bull_score = Drivers_And_Teams.verstappen.score + Drivers_And_Teams.perez.score
    Mercedes_score = Drivers_And_Teams.hamilton.score + Drivers_And_Teams.russell.score
    Alfa_Romeo_score = Drivers_And_Teams.bottas.score + Drivers_And_Teams.zhou.score
    Mclaren_score = Drivers_And_Teams.norris.score + Drivers_And_Teams.ricciardo.score
    Alpine_score = Drivers_And_Teams.ocon.score + Drivers_And_Teams.alonso.score
    Haas_score = Drivers_And_Teams.magnussen.score + Drivers_And_Teams.schumacher.score
    Alphatauri_Score = Drivers_And_Teams.tsunoda.score + Drivers_And_Teams.gasly.score
    Aston_Martin_score = Drivers_And_Teams.stroll.score + Drivers_And_Teams.vettel.score
    Williams_score = Drivers_And_Teams.latifi.score + Drivers_And_Teams.albon.score

    dict_of_teams = {"Ferrari": Ferrari_score, "Red Bull": Red_Bull_score, "Mercedes": Mercedes_score,
                     "Alfa_romeo": Alfa_Romeo_score, "Mclaren": Mclaren_score, "Alpine": Alpine_score, "Haas": Haas_score,
                     "Alphatauri": Alphatauri_Score, "Aston_Martin": Aston_Martin_score, "Williams": Williams_score}

    sorted_dict_of_teams = {k: v for k, v in sorted(dict_of_teams.items(), key=lambda v: v[1], reverse=True)}
    print(sorted_dict_of_teams)


def number_of_wins(all_races):
    while True:
        winners = []
        for races in all_races:
            winners.append(races.ranking[0])
        who_won = input("which driver wins number do you want to know?")
        if who_won not in Driver.all_drivers:
            print("there is no such driver. try again")
            continue
        else:
            count = winners.count(who_won)
            print(who_won,"won",count, "races this season")
            break


def num_of_regular_wins(all_races):
    while True:
        regular_winners = []
        for races in all_races:
            if races.type == "ragil":
                regular_winners.append(races.ranking[0])
        regular_winnings = input("which driver regular wins number do you want to know?")
        if regular_winnings not in Driver.all_drivers:
            print("there is no such driver. try again. try again")
            continue
        else:
            count_regular = regular_winners.count(regular_winnings)
            print(regular_winnings, "won",count_regular, "regular races this season")
            break


def num_of_sprint_wins(all_races):
    while True:
        sprint_winners = []
        for races in all_races:
            if races.type == "sprint":
                sprint_winners.append(races.ranking[0])
        sprint_winnings = input("which driver sprint wins number do you want to know?")
        if sprint_winnings not in Driver.all_drivers:
            print("there is no such driver. try again. try again")
            continue
        else:
            count_sprint = sprint_winners.count(sprint_winnings)
            print(sprint_winnings, "won", count_sprint, "sprint races this season")
            break


def fastest_driver(all_races):
    while True:
        fastest_lap = []
        for races in all_races:
            if races.type == "ragil": # good. constang like "ragil" can be in race class -see what i did there
                fastest_lap.append(races.ranking[10])
        fastest_driver = input("which driver number of fastest lap winnings do you want to know?")
        if fastest_driver not in Driver.all_drivers:
            print("there is no such driver. try again")
            continue
        else:
            count_fastest = fastest_lap.count(fastest_driver)
            print(fastest_driver, "has been the fastest driver in", count_fastest, "races this season")
            break


def active_system(list_of_all_races):
    while True:
        teams_standing = input("do you want to see teams standing as well?")
        if teams_standing == "yes":
            print("teams standing:")
            get_team_score(get_driver_score)
            break
        elif teams_standing == "no":
            break
        else:
            print("something went wrong. try again")
            continue

    while True:
        question = input("do you want to do something else?")
        if question == "no":
            break
        # this is very interesting stuff - maybe it should all be 
        # in the main menu. or at least give option of DATA in main menu and
        # then display this menu
        elif question == "yes":
            choose = input("what do you want to do? your options are: \n1. find number of total wins \n2. find number of regular wins \n3. find number of sprint wins \n4. find the fastest driver \nchoose number")
            if choose == "1":
                number_of_wins(list_of_all_races)
            elif choose == "2":
                num_of_regular_wins(list_of_all_races)
            elif choose == "3":
                num_of_sprint_wins(list_of_all_races)
            elif choose == "4":
                fastest_driver(list_of_all_races)
            else:
                print("something went wrong. try again")
                continue
        else:
            print("something went wrong. try again")
            continue


#other option for add_race:
#
def add_race(list_of_all_races):
    while True:
        race_type = input("enter: ragil or sprint?")
        if race_type == "ragil":
            enter_standing = input("enter list of all drivers from first to tenth and than the fastest driver")
            split_ranking = enter_standing.split(", ")
            if len(split_ranking) != 11:
                print("you have to enter exactly 11 names. let's try again")
                continue
            # why not make this code in a loop 
            # for i in split_ranking:
            # if split_ranking[i] not in Driver.alldrivers....
            if split_ranking[0] not in Driver.all_drivers or split_ranking[1] not in Driver.all_drivers or\
                    split_ranking[2] not in Driver.all_drivers or split_ranking[3] not in Driver.all_drivers or\
                    split_ranking[4] not in Driver.all_drivers or split_ranking[5] not in Driver.all_drivers or\
                    split_ranking[6] not in Driver.all_drivers or split_ranking[7] not in Driver.all_drivers or\
                    split_ranking[8] not in Driver.all_drivers or split_ranking[9] not in Driver.all_drivers or split_ranking[10] not in Driver.all_drivers:
                print("you can only enter drivers names. please try again")
                continue
            # if you want to check double why not make a set instead of list?
            if split_ranking[0] in split_ranking[1:10] or split_ranking[1] in split_ranking[2:10] or split_ranking[2] in split_ranking[3:10]\
                    or split_ranking[3] in split_ranking[4:10] or split_ranking[4] in split_ranking[5:10] or split_ranking[5] in split_ranking[6:10]\
                    or split_ranking[6] in split_ranking[7:10] or split_ranking[7] in split_ranking[8:10] or split_ranking[8] in split_ranking[9:10]\
                    or split_ranking[9] in split_ranking[10]:
                print("every driver can be in only one place except fastest driver")
                continue
            fastest_lap = "nothing"
            race_name = input("enter race name")

            new_race = Race(race_type, split_ranking, fastest_lap, race_name)
            list_of_all_races.append(new_race)
            return new_race

        #This is quite a long function - consider splitting to 2 functions - sprint, regular
        elif race_type == "sprint":
            enter_standing = input("enter list of all drivers from first to eighth")
            split_ranking = enter_standing.split(", ")
            if len(split_ranking) != 8:
                print("you have to enter exactly 8 names. let's try again")
                continue
            # if this code is repeating - better take it out and make it a function
            if split_ranking[0] not in Driver.all_drivers or split_ranking[1] not in Driver.all_drivers or \
                    split_ranking[2] not in Driver.all_drivers or split_ranking[3] not in Driver.all_drivers or \
                    split_ranking[4] not in Driver.all_drivers or split_ranking[5] not in Driver.all_drivers or \
                    split_ranking[6] not in Driver.all_drivers or split_ranking[7] not in Driver.all_drivers:
                print("you can only enter drivers names. please try again")
                continue
            if split_ranking[0] in split_ranking[1:7] or split_ranking[1] in split_ranking[2:7] or split_ranking[
                2] in split_ranking[3:7] or split_ranking[3] in split_ranking[4:7] or split_ranking[4] in split_ranking[5:7] or \
                    split_ranking[5] in split_ranking[6:7] or split_ranking[6] in split_ranking[7]:
                print("every driver can be in only one place")
                continue
            fastest_lap = "nothing"
            race_name = input("enter race name")

            new_race = Race(race_type, split_ranking, fastest_lap, race_name)
            list_of_all_races.append(new_race)
            return new_race

        else:
            print("you have to enter ragil or sprint. let's try again")



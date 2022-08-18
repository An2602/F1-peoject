#another option of add race



# def add_race(list_of_all_races):
#     while True:
#         race_type = input("enter: ragil or sprint?")
#         if race_type == "ragil":
#             first_place = input("enter first place full name")
#             if first_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             second_place = input("enter second place full name")
#             if second_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if first_place == second_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             third_place = input("enter third place full name")
#             if third_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if third_place == first_place or third_place == second_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             fourth_place = input("enter fourth place full name")
#             if fourth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if fourth_place == first_place or fourth_place == second_place or fourth_place == third_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             fifth_place = input("enter fifth place full name")
#             if fifth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if fifth_place == first_place or fifth_place == second_place or fifth_place == third_place or fifth_place == fourth_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             sixth_place = input("enter sixth place full name")
#             if sixth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if sixth_place == first_place or sixth_place == second_place or sixth_place == third_place or sixth_place == fourth_place or sixth_place == fifth_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             seventh_place = input("enter seventh place full name")
#             if seventh_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if seventh_place == first_place or seventh_place == second_place or seventh_place == third_place or seventh_place == fourth_place or seventh_place == fifth_place or seventh_place == sixth_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             eighth_place = input("enter eighth place full name")
#             if eighth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if eighth_place == first_place or eighth_place == second_place or eighth_place == third_place or eighth_place == fourth_place or eighth_place == fifth_place or eighth_place == sixth_place or eighth_place == seventh_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             ninth_place = input("enter ninth place full name")
#             if ninth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if ninth_place == first_place or ninth_place == second_place or ninth_place == third_place or ninth_place == fourth_place or ninth_place == fifth_place or ninth_place == sixth_place or ninth_place == seventh_place or ninth_place == eighth_place:
#                 print("something went wrong. let's start again")
#                 continue
#             tenth_place = input("enter tenth place full name")
#             if tenth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if tenth_place == first_place or tenth_place == second_place or tenth_place == third_place or tenth_place == fourth_place or tenth_place == fifth_place or tenth_place == sixth_place or tenth_place == seventh_place or tenth_place == eighth_place or tenth_place == ninth_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             fastest_lap = input("enter fastest driver full name")
#             if first_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             race_name = input("enter race name")
#
#             new_race = Race(race_type, [first_place, second_place, third_place, fourth_place, fifth_place, sixth_place,
#                                         seventh_place, eighth_place, ninth_place, tenth_place, fastest_lap], fastest_lap, race_name)
#             ipdb.set_trace()
#             list_of_all_races.append(new_race)
#             return new_race
#
#
#         elif race_type == "sprint":
#             first_place = input("enter first place full name")
#             if first_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             second_place = input("enter second place full name")
#             if second_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if first_place == second_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             third_place = input("enter third place full name")
#             if third_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if third_place == first_place or third_place == second_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             fourth_place = input("enter fourth place full name")
#             if fourth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if fourth_place == first_place or fourth_place == second_place or fourth_place == third_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             fifth_place = input("enter fifth place full name")
#             if fifth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if fifth_place == first_place or fifth_place == second_place or fifth_place == third_place or fifth_place == fourth_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             sixth_place = input("enter sixth place full name")
#             if sixth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if sixth_place == first_place or sixth_place == second_place or sixth_place == third_place or sixth_place == fourth_place or sixth_place == fifth_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             seventh_place = input("enter seventh place full name")
#             if seventh_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if seventh_place == first_place or seventh_place == second_place or seventh_place == third_place or seventh_place == fourth_place or seventh_place == fifth_place or seventh_place == sixth_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             eighth_place = input("enter eighth place full name")
#             if eighth_place not in Driver.all_drivers:
#                 print("something went wrong. let's start again")
#                 continue
#             if eighth_place == first_place or eighth_place == second_place or eighth_place == third_place or eighth_place == fourth_place or eighth_place == fifth_place or eighth_place == sixth_place or eighth_place == seventh_place:
#                 print("every driver can be in only one place. try again")
#                 continue
#             another = "nothing"
#             race_name = input("enter race name")
#
#             new_race = Race(race_type, [first_place, second_place, third_place, fourth_place, fifth_place, sixth_place,
#                        seventh_place, eighth_place], another, race_name)
#             list_of_all_races.append(new_race)
#             return new_race
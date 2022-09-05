class Driver:
    all_drivers = []
    def __init__(self, name, country, number, constructor):
        self.name = name
        self.country = country
        self.number = number
        self.constructor = constructor
        self.score = 0

leclerc = Driver("Charles Leclerc", "Monaco", 16, "Ferrari")
sainz = Driver("Carlos Sainz", "Spain", 55, "Ferrari")
verstappen = Driver("Max Verstappen", "Netherlands", 1, "Red Bull")
perez = Driver("Sergio Perez", "Mexico", 11, "Red Bull")
hamilton = Driver("Lewis Hamilton", "United Kingdom", 44, "Mercedes")
russell = Driver("George Russell", "United Kingdom", 63, "Mercedes")
bottas = Driver("Valtteri Bottas", "Finland", 77, "Alfa Romeo")
zhou = Driver("Guanyu Zhou", "China", 24, "Alfa Romeo")
ricciardo = Driver("Daniel Ricciardo", "Australia", 3, "Mclaren")
norris = Driver("Lando Norris", "United Kingdom", 4, "Mclaren")
ocon = Driver("Esteban Ocon", "France", 31, "Alpine")
alonso = Driver("Fernando Alonso", "Spain", 14, "Alpine")
magnussen = Driver("Kevin Magnussen", "Denmark", 20, "Haas")
schumacher = Driver("Mick Schumacher", "Germany", 47, "Haas")
tsunoda = Driver("Yuki Tsunoda", "Japan", 22, "Alphatauri ")
gasly = Driver("Pierre Gasly", "France", 10, "Alphatauri ")
stroll = Driver("Lance Stroll", "Canada", 18, "Aston Martin ")
vettel = Driver("Sebastian Vettel", "Germany", 5, "Aston Martin ")
latifi = Driver("Nicholas Latifi", "Canada", 6, "Williams")
albon = Driver("Alexander Albon", "Thailand", 23, "Williams")

Driver.all_drivers = {leclerc.name: leclerc, sainz.name: sainz, verstappen.name: verstappen,
                      perez.name: perez, hamilton.name: hamilton, russell.name: russell,
                    bottas.name: bottas, zhou.name: zhou, ricciardo.name: ricciardo,
                      norris.name: norris, ocon.name: ocon, alonso.name: alonso,
                    magnussen.name: magnussen, schumacher.name: schumacher, tsunoda.name: tsunoda,
                    gasly.name: gasly, stroll.name: stroll, vettel.name: vettel, latifi.name: latifi,
                      albon.name: albon}


class Team:
    def __init__(self, team, drivers):
        self.team = team
        self.drivers = []
        self.team_score = 0


Ferrari = Team("Ferrari",[leclerc, sainz])
Red_Bull = Team("Red Bull", [verstappen, perez])
Mercedes = Team("Mercedes", [hamilton, russell])
Alfa_Romeo = Team("Alfa Romeo", [bottas, zhou])
Mclaren = Team("Mclaren", [ricciardo, norris])
Alpine = Team("Alpine", [ocon, alonso])
Haas = Team("Haas", [magnussen, schumacher])
Alphatauri = Team("Alphatauri", [tsunoda, gasly])
Aston_Martin = Team("Aston Martin", [stroll, vettel])
Williams = Team("Williams", [latifi, albon])

# Team.all_teams = {Ferrari.team: Ferrari, Red_Bull.team: Red_Bull, Mercedes.team: Mercedes,
#                   Alfa_Romeo.team: Alfa_Romeo, Mclaren.team: Mclaren, Alpine.team: Alpine, Haas.team: Haas,
#                   Alphatauri.team: Alphatauri, Aston_Martin.team: Aston_Martin, Williams.team: Williams}

# class DriverList:
#     def __init__(self):
#         self.my_drivers_list = []
class Bug:
    label = "Bug"
    strong = ['Grass', 'Dark', 'Psychic']
    weak = ['Fire', 'Flying', 'Rock']
    def __repr__(self):
        return "Bug"
    def __str__(self):
        return self.__repr__()

class Dark:
    label = "Dark"
    strong = ['Ghost', 'Pyschic']
    weak = ['Bug', 'Fairy', 'Ice']
    def __repr__(self):
        return "Dark"
    def __str__(self):
        return self.__repr__()

class Dragon:
    label = "Dragon"
    strong = ['Dragon']
    weak = ['Dragon', 'Fairy', 'Ice']
    def __repr__(self):
        return "Dragon"
    def __str__(self):
        return self.__repr__()

class Electric:
    label = "Electric"
    strong = ['Flying', 'Water']
    weak = ['Ground']
    def __repr__(self):
        return "Electric"
    def __str__(self):
        return self.__repr__()

class Fairy:
    label = "Fairy"
    strong = ['Fighting', 'Dark', 'Dragon']
    weak = ['Poison', 'Steel']
    def __repr__(self):
        return "Fairy"
    def __str__(self):
        return self.__repr__()

class Fighting:
    label = "Fighting"
    strong = ['Dark', 'Ice', 'Normal', 'Rock', 'Steel']
    weak = ['Fairy', 'Flying', 'Psychic']
    def __repr__(self):
        return "Fighting"
    def __str__(self):
        return self.__repr__()

class Fire:
    label = "Fire"
    strong = ['Bug', 'Grass', 'Ice', 'Steel']
    weak = ['Ground', 'Rock', 'Water']
    def __repr__(self):
        return "Fire"
    def __str__(self):
        return self.__repr__()

class Flying:
    label = "Flying"
    strong = ['Bug', 'Fighting', 'Grass']
    weak = ['Electric', 'Ice', 'Rock']
    def __repr__(self):
        return "Flying"
    def __str__(self):
        return self.__repr__()

class Ghost:
    label = "Ghost"
    strong = ['Ghost', 'Psychic']
    weak = ['Dark', 'Ghost']
    def __repr__(self):
        return "Ghost"
    def __str__(self):
        return self.__repr__()

class Grass:
    label = "Grass"
    strong = ['Ground', 'Rock', 'Water']
    weak = ['Bug', 'Fire', 'Flying', 'Ice', 'Poison']
    def __repr__(self):
        return "Grass"
    def __str__(self):
        return self.__repr__()

class Ground:
    label = "Ground"
    strong = ['Electric', 'Fire', 'Poison', 'Rock', 'Steel']
    weak = ['Grass', 'Ice', 'Water']
    def __repr__(self):
        return "Ground"
    def __str__(self):
        return self.__repr__()

class Ice:
    label = "Ice"
    strong = ['Dragon', 'Flying', 'Grass', 'Ground']
    weak = ['Fighting', 'Fire', 'Rock', 'Steel']
    def __repr__(self):
        return "Ice"
    def __str__(self):
        return self.__repr__()

class Normal:
    label = "Normal"
    strong = []
    weak = ['Fighting']
    def __repr__(self):
        return "Normal"
    def __str__(self):
        return self.__repr__()

class Poison:
    label = "Poison"
    strong = ['Fairy', 'Grass']
    weak = ['Ground', 'Psychic']
    def __repr__(self):
        return "Poison"
    def __str__(self):
        return self.__repr__()

class Psychic:
    label = "Psychic"
    strong = ['Fighting', 'Poison']
    weak = ['Bug', 'Dark', 'Ghost']
    def __repr__(self):
        return "Psychic"
    def __str__(self):
        return self.__repr__()

class Rock:
    label = "Rock"
    strong = ['Bug', 'Fire', 'Flying', 'Ice']
    weak = ['Fighting', 'Grass', 'Ground', 'Steel', 'Water']
    def __repr__(self):
        return "Rock"
    def __str__(self):
        return self.__repr__()

class Steel:
    label = "Steel"
    strong = ['Fairy', 'Ice', 'Rock']
    weak = ['Fighting', 'Fire', 'Ground']
    def __repr__(self):
        return "Steel"
    def __str__(self):
        return self.__repr__()

class Water:
    label = "Water"
    strong = ['Fire', 'Ground', 'Rock']
    weak = ['Electric', 'Grass']
    def __repr__(self):
        return "Water"
    def __str__(self):
        return self.__repr__()

TYPES = {'Bug' : Bug, 'Dark' : Dark, 'Dragon': Dragon, 'Electric' : Electric, 'Fairy' : Fairy, 'Fighting' : Fighting, 'Fire': Fire, 'Flying' : Flying, 'Ghost': Ghost, 'Grass' : Grass, 'Ground' : Ground, 'Ice' : Ice, 'Normal': Normal, 'Poison' : Poison, 'Psychic': Psychic, 'Rock': Rock, 'Steel' : Steel, 'Water' : Water}

def get_type(type):
    if isinstance(type, int):
        return list(TYPES.values())[type]
    return TYPES[type]

def remove_dups(alist):
    return list(dict.fromkeys(alist))

def optimal_types():
    types = TYPES.values()
    classes = TYPES.values()
    num_types = len(types)
    teams = []
    i = 0
    while i < num_types:
        j = 0
        while j < num_types:
            k = 0
            while k < num_types:
                new_team = [i, j, k]
                new_team.sort()
                if new_team not in teams:
                    #print(new_team)
                    teams.append(new_team)
                k += 1
            j += 1
        i += 1
    teams.sort()
    #print(teams) 
    i = 0
    team_stats = []
    while i < len(teams):
        team = teams[i]
        team = [get_type(team[0]), get_type(team[1]), get_type(team[2])]
        strengths = remove_dups(team[0].strong + team[1].strong + team[2].strong)
        weaks = remove_dups(team[0].weak + team[1].weak + team[2].weak)
        vulnerable = set(weaks) - set(strengths)
        team_stats.append((team, len(strengths), vulnerable))
        i += 1
    team_stats.sort(key=lambda team: len(team[2]))
    
    print("TOP TEAMS BY LEAST VULNERABILITIES:")
    i = 0
    while i < 10:
        stat = team_stats[i]
        print((stat[0][0]).label, (stat[0][1]).label, (stat[0][2]).label)
        print("Coverage: {0}/18, Vulnerabilities: {1}".format(stat[1], stat[2]))
        print()
        i += 1

    team_stats.sort(key=lambda team: team[1], reverse=True)
    print("TOP TEAMS BY HIGHEST COVERAGE:")
    i = 0
    while i < 10:
        stat = team_stats[i]
        print((stat[0][0]).label, (stat[0][1]).label, (stat[0][2]).label)
        print("Coverage: {0}/18, Vulnerabilities: {1}".format(stat[1], stat[2]))
        print()
        i += 1

        


def main():
    optimal_types()





if __name__ == '__main__':
    main()

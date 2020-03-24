class Bug:
    strong = ['Grass', 'Dark', 'Psychic']
    weak = ['Fire', 'Flying', 'Rock']

class Dark:
    strong = ['Ghost', 'Pyschic']
    weak = ['Bug', 'Fairy', 'Ice']

class Dragon:
    strong = ['Dragon']
    weak = ['Dragon', 'Fairy', 'Ice']

class Electric:
    strong = ['Flying', 'Water']
    weak = ['Ground']

class Fairy:
    strong = ['Fighting', 'Dark', 'Dragon']
    weak = ['Poison', 'Steel']

class Fighting:
    strong = ['Dark', 'Ice', 'Normal', 'Rock', 'Steel']
    weak = ['Fairy', 'Flying', 'Psychic']

class Fire:
    strong = ['Bug', 'Grass', 'Ice', 'Steel']
    weak = ['Ground', 'Rock', 'Water']

class Flying:
    strong = ['Bug', 'Fighting', 'Grass']
    weak = ['Electric', 'Ice', 'Rock']

class Ghost:
    strong = ['Ghost', 'Psychic']
    weak = ['Dark', 'Ghost']

class Grass:
    strong = ['Ground', 'Rock', 'Water']
    weak = ['Bug', 'Fire', 'Flying', 'Ice', 'Poison']

class Ground:
    strong = ['Electric', 'Fire', 'Poison', 'Rock', 'Steel']
    weak = ['Grass', 'Ice', 'Water']

class Ice:
    strong = ['Dragon', 'Flying', 'Grass', 'Ground']
    weak = ['Fighting', 'Fire', 'Rock', 'Steel']

class Normal:
    strong = []
    weak = ['Fighting']

class Poison:
    strong = ['Fairy', 'Grass']
    weak = ['Ground', 'Psychic']

class Psychic:
    strong = ['Fighting', 'Poison']
    weak = ['Bug', 'Dark', 'Ghost']

class Rock:
    strong = ['Bug', 'Fire', 'Flying', 'Ice']
    weak = ['Fighting', 'Grass', 'Ground', 'Steel', 'Water']

class Steel:
    strong = ['Fairy', 'Ice', 'Rock']
    weak = ['Fighting', 'Fire', 'Ground']

class Water:
    strong = ['Fire', 'Ground', 'Rock']
    weak = ['Electric', 'Grass']

TYPES = {'Bug' : Bug, 'Dark' : Dark, 'Dragon': Dragon, 'Electric' : Electric, 'Fairy' : Fairy, 'Fighting' : Fighting, 'Fire': Fire, 'Flying' : Flying, 'Ghost': Ghost, 'Grass' : Grass, 'Ground' : Ground, 'Ice' : Ice, 'Normal': Normal, 'Poison' : Poison, 'Psychic': Psychic, 'Rock': Rock, 'Steel' : Steel, 'Water' : Water}

def get_type(type):
    return TYPES[type]

def remove_dups(list):
    return list(dict.fromkeys(list))



def main():
    type = get_type('Bug')
    print(type.strong)





if __name__ == '__main__':
    main()

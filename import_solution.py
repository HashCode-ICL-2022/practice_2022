from os.path import basename

def import_solution(name):
    with open('outputs/' + basename(name), 'r') as file:
        ingredients = file.readline().split(' ')[1:]
    return ingredients

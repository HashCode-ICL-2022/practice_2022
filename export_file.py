from os.path import basename

def export_file(name, ingredients):

    string = str(len(ingredients))
    for ingredient in ingredients:
        string += ' ' + ingredient

    f = open('outputs/' + basename(name), "w")
    f.writelines(string)

def export_file(name, ingredients):

    string = str(len(ingredients))
    for ingredient in ingredients:
        string += ' ' + ingredient

    f = open('outputs/' + name, "w")
    f.writelines(string)

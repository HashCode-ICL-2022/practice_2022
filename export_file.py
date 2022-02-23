def export_file(name, ingredients):
    f = open('outputs/' + name, "w")
    f.writelines([len(ingredients)].extend(ingredients))

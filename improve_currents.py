from import_solution import import_solution
from import_file import import_file, import_ingredients
from export_file import export_file


def improve_currents(fname):
    if "pruned_data" in fname:
        initial_ingredients = import_ingredients(f"pruned_data/d_intial_ingredients.txt")
    else:
        initial_ingredients = None

    likes, dislikes = import_file(fname)
    old_solution = import_solution(fname)
    print(old_solution)





if __name__ == '__main__':
    # fname = 'data/a_an_example.in.txt'
    # fname = 'data/b_basic.in.txt'
    # fname = 'data/c_coarse.in.txt'
    fname = 'pruned_data/d_difficult.in.txt'
    # fname = 'pruned_data/e_elaborate.in.txt'
    improve_currents(fname)

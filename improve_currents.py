from import_solution import import_solution
from import_file import import_file, import_ingredients
from export_file import export_file


def improve_currents(fname):
    if "pruned_data" in fname:
        initial_ingredients = import_ingredients(f"pruned_data/d_intial_ingredients.txt")
    else:
        initial_ingredients = None

    likes, dislikes = import_file(fname)
    pizza = import_solution(fname)
    not_on_pizza = set() - pizza
    score = score(pizza)
    is_score_change = True

    while is_score_change:
        for ingredient in pizza:
            test_pizza = pizza.copy()
            test_pizza -= ingredient
            tscore = score(test_pizza)
            if tscore > score:
                score = tscore
                pizza = test_pizza
                break
        for ingredient in not_on_pizza:
            test_pizza = pizza.copy()
            test_pizza += ingredient
            tscore = score(test_pizza)
            if tscore > score:
                score = tscore
                pizza = test_pizza
                break
        is_score_change = False

    export_file(fname, pizza)

if __name__ == '__main__':
    # fname = 'data/a_an_example.in.txt'
    # fname = 'data/b_basic.in.txt'
    # fname = 'data/c_coarse.in.txt'
    fname = 'pruned_data/d_difficult.in.txt'
    # fname = 'pruned_data/e_elaborate.in.txt'
    improve_currents(fname)

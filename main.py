import numpy as np

from import_file import import_file, import_ingredients
from export_file import export_file
from operator import itemgetter

ITERS = 10
DELTA = 10


def main(all_likes, all_dislikes, initial_ingredients=None):

    df, ingredients, ingredients_map = reshape_data(all_likes, all_dislikes)
    ingredients = list(ingredients)

    dislikes_flat = [i for j in all_dislikes for i in j]
    dislikes_uniques, dislikes_counts = np.unique(dislikes_flat, return_counts=True)
    dislikes_dict = {i:j for (i, j)  in zip(dislikes_uniques, dislikes_counts)}
    ingredients.sort(key=lambda x: dislikes_dict[x], reverse=True)

    while True:

        tmp_ingredients = ingredients[DELTA:]
        score = scorer(df, tmp_ingredients, ingredients_map)



def reshape_data(all_likes, all_dislikes):

    likes_flat = [i for j in all_likes for i in j]
    dislikes_flat = [i for j in all_dislikes for i in j]
    ingredients = np.unique(likes_flat + dislikes_flat)

    df = np.zeros(shape=(len(all_likes), len(ingredients)))
    for i in range(len(all_likes)):
        likes = all_likes[i]
        dislikes = all_dislikes[i]
        for j in range(len(ingredients)):
            ing = ingredients[j]
            if ing in likes:
                df[i, j] = 1
            elif ing in dislikes:
                df[i, j] = -1
    
    ingredients_map = {ing:idx for (idx, ing) in enumerate(ingredients)}

    return df, ingredients, ingredients_map


def scorer(df, ingredients, ingredients_map):

    ings_idx = [ingredients_map[ingredient] for ingredient in ingredients]


    ## [-1, 0, 1, 1]
    ## ings_idx = [1, 2]





if __name__ == "__main__":
    # fname = 'data/a_an_example.in.txt'
    # fname = 'data/b_basic.in.txt'
    # fname = 'data/c_coarse.in.txt'
    fname = 'pruned_data/d_difficult.in.txt'
    # fname = 'pruned_data/e_elaborate.in.txt'
    if "pruned_data" in fname:
        initial_ingredients = import_ingredients(f"pruned_data/d_intial_ingredients.txt")
    else:
        initial_ingredients = None

    likes, dislikes = import_file(fname)
    # main(likes, dislikes, initial_ingredients)
    df = reshape_data(likes, dislikes)


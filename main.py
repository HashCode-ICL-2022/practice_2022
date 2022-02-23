import numpy as np

from import_file import import_file, import_ingredients
from export_file import export_file
from operator import itemgetter

from tqdm import tqdm

ITERS = 10
DELTA = 10


def main(all_likes, all_dislikes, initial_ingredients=None):

    df, ingredients, ingredients_map = reshape_data(all_likes, all_dislikes)
    # df: 2D Matrix with (person, likes/dislikes)
    # ingredients: 1D int array [0, 1, 2, 3, ...]
    # ingredients_map: ["apple", "tomato", "sfjdsaf"]

    dislikes_counts = np.sum(df == -1, axis=0)
    sorted_dislikes = list(np.argsort(-dislikes_counts))
    recipe_bool = np.full(ingredients.shape, True)

    pbar = tqdm(range(len(ingredients)))
    best_score = scorer(df, recipe_bool)
    for i in pbar:
        # Remove some of bad ingredients
        remove_ingredients = sorted_dislikes[:DELTA]
        sorted_dislikes = sorted_dislikes[DELTA:]
        recipe_bool[remove_ingredients] = False

        # Score
        score = scorer(df, recipe_bool)
        pbar.set_postfix(score=score, n=np.sum(recipe_bool))
        if score < best_score:
            break


def scorer(df, recipe_bool):
    goods = np.all(df[:, recipe_bool] == 1, axis=1)
    bads = np.any(df[:, ~recipe_bool] == 1, axis=1)
    return np.sum(np.logical_and(goods, ~bads))


def reshape_data(all_likes, all_dislikes):

    likes_flat = [i for j in all_likes for i in j]
    dislikes_flat = [i for j in all_dislikes for i in j]
    ingredients = np.unique(likes_flat + dislikes_flat)

    df = np.zeros(shape=(len(all_likes), len(ingredients)))
    for i in tqdm(range(len(all_likes))):
        likes = all_likes[i]
        dislikes = all_dislikes[i]
        for j in range(len(ingredients)):
            ing = ingredients[j]
            if ing in likes:
                df[i, j] = 1
            elif ing in dislikes:
                df[i, j] = -1

    return df, np.arange(len(ingredients)), ingredients


if __name__ == "__main__":
    fname = 'data/a_an_example.in.txt'
    # fname = 'data/b_basic.in.txt'
    # fname = 'data/c_coarse.in.txt'
    fname = 'pruned_data/d_difficult.in.txt'
    # fname = 'pruned_data/e_elaborate.in.txt'
    if "pruned_data" in fname:
        initial_ingredients = import_ingredients(
            f"pruned_data/d_intial_ingredients.txt")
    else:
        initial_ingredients = None

    likes, dislikes = import_file(fname)
    main(likes, dislikes, initial_ingredients)
    # df = reshape_data(likes, dislikes)

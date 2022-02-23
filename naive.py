from import_file import import_file, import_ingredients
from export_file import export_file
from operator import itemgetter


def get_ingredients(all_likes, all_dislikes, initial_ingredients=None):

    # all_likes, all_dislikes = sort_candidates(all_likes, all_dislikes)
    score = 0

    if initial_ingredients is not None:
        ingredients = set(initial_ingredients)
    else:
        ingredients = set()

    banned_ingredients = set()


    for likes, dislikes in zip(all_likes, all_dislikes):
        bad = False
        for dislike in dislikes:
            if dislike in ingredients:
                bad = True
        for like in likes:
            if like in banned_ingredients:
                bad = True
        if bad:
            continue

        score += 1

        ingredients.update(set(likes))
        banned_ingredients.update(set(dislikes))

    return score, ingredients


def sort_candidates(all_likes, all_dislikes):
    candidates = list()

    for likes, dislikes in zip(all_likes, all_dislikes):
        candidates.append((likes, dislikes, len(likes) + len(dislikes)))

    candidates.sort(key=itemgetter(2))
    sorted_likes, sorted_dislikes, _ = zip(*candidates)

    return list(sorted_likes), list(sorted_dislikes)

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
    score, ingredients = get_ingredients(likes, dislikes, initial_ingredients)

    # print(f"score: {score}/{len(likes)}, \ningredients: {ingredients}")
    print(score)
    export_file(fname, ingredients)

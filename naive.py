from import_file import import_file
from export_file import export_file


def get_ingredients(all_likes, all_dislikes):

    score = 0
    ingredients = set()
    not_ingredients = set()
    for likes, dislikes in zip(all_likes, all_dislikes):
        bad = False
        for dislike in dislikes:
            if dislike in ingredients:
                bad = True
        for like in likes:
            if like in not_ingredients:
                bad = True
        if bad:
            continue

        score += 1
        not_ingredients.update(set(dislikes))
        ingredients.update(set(likes))


    return score, ingredients



if __name__ == "__main__":
    # fname = 'a_an_example.in.txt'
    # fname = 'b_basic.in.txt'
    fname = 'c_coarse.in.txt'
    # fname = 'd_difficult.in.txt'
    # fname = 'e_elaborate.in.txt'
    likes, dislikes = import_file(fname)
    score, ingredients = get_ingredients(likes, dislikes)
    # print(f"score: {score}/{len(likes)}, \ningredients: {ingredients}")
    print(score)
    export_file(fname, ingredients)

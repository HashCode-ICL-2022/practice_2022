from import_file import import_file


def get_ingredients(all_likes, all_dislikes):
    
    score = 0
    ingredients = set()
    for likes, dislikes in zip(all_likes, all_dislikes):
        bad = False
        for dislike in dislikes:
            if dislike in ingredients:
                bad = True
        if bad:
            continue
            
        
        score += 1
        ingredients.update(set(likes))

    return score, ingredients



if __name__ == "__main__":
    # fname = 'a_an_example.in.txt'
    # fname = 'b_basic.in.txt'
    # fname = 'c_coarse.in.txt'
    fname = 'd_difficult.in.txt'
    likes, dislikes = import_file(fname)
    score, ingredients = get_ingredients(likes, dislikes)
    print(f"score: {score}/{len(likes)}, \ningredients: {ingredients}")
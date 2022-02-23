def slow_scorer(all_likes, all_dislikes, ingredients):

    score = 0
    for likes, dislikes in zip(all_likes, all_dislikes):

        if is_good(likes, dislikes, ingredients):
            score += 1
    return score
            

def is_good(likes, dislikes, ingredients):

    for like in likes:
        if like not in ingredients:
            return False
    for dislike in dislikes:
        if dislike in ingredients:
            return False

    return True
def import_file(file_name):
    with open(file_name, 'r') as file:
        # Read first line
        N = int(file.readline())

        print(f"Loading {N} Customers")
        likes = []
        dislikes = []
        for i in range(N):
            line = file.readline().rstrip().split(" ")
            likes.append(line[1:])
            line = file.readline().rstrip().split(" ")
            dislikes.append(line[1:])

        return likes, dislikes


def import_ingredients(filepath):
    with open(filepath, 'r') as fp:
        return fp.read().strip().split(" ")

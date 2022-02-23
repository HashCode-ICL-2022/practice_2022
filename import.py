def import_file(filename):
    with open(file_name, 'r') as file:
        # Read first line
        N = int(file.readline())

        print(f"Loading {N} Customers")
        likes = []
        avg_l = []
        for i in range(N):
            line = file.readline().rstrip().split(" ")
            likes.extend(line[1:])

        dislikes = []
        for i in range(N):
            line = file.readline().rstrip().split(" ")
            dislikes.extend(line[1:])

        return likes, dislikes

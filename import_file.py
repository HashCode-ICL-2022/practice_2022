def import_file(file_name):
    with open('data/' + file_name, 'r') as file:
        # Read first line
        N = int(file.readline())

        # print(f"Loading {N} Customers")
        likes = []
        for i in range(N):
            line = file.readline().rstrip().split(" ")
            likes.extend(line[1:])

        dislikes = []
        for i in range(N):
            line = file.readline().rstrip().split(" ")
            dislikes.extend(line[1:])

        return likes, dislikes

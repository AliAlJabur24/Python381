from movies import Movies

movies = Movies('./movies.txt')

MovieNames = [x['name'].lower() for x in movies._movies]

def print_all_movie_names():
    for movie in movies._movies:
        print(movie['name'])

def search_movies_by_name():
    search_term = input("Movie Name: ").lower()
    matching_movies = [name for name in MovieNames if search_term in name.lower()]

    if matching_movies:
        print('Movies Found:')
        for movie in matching_movies:
            print(movie)
    else:
        print('No movie found.')

def search_movies_by_cast():
    search_term = input("Enter a cast member's name to search: ").lower()
    matching_movies = []

    for movie in movies._movies:
        for cast_member in movie['cast']:
            if search_term in cast_member.lower():
                matching_movies.append([cast_member, movie['name']])
                break

    if matching_movies:
        print('Movies by cast member: ')
        for entry in matching_movies:
            print(entry[1])
            print(entry[0])
    else:
        print('No movie found by cast member')

def menu():
    while True:
        print("\nMenu:")
        print("1 - Print all movie names")
        print("2 - Search movies by name")
        print("3 - Search movies by cast")
        print("q - Quit")

        choice = input("Enter your choice: ")

        if choice == 'q':
            print("existing the program")
            break
        elif choice == '1':
            print_all_movie_names()
        elif choice == '2':
            search_movies_by_name()
        elif choice == '3':
            search_movies_by_cast()
        else:
            print("Invalid input, please try again.")

            
if __name__ == "__main__":
    menu()
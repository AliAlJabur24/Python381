from movies import Movies

movies = Movies('./movies.txt')

MovieNames = [x['name'].lower() for x in movies._movies]

def print_all_movie_names():
    for movie in movies._movies:
        print(movie['name'])

def search_movies_by_name():
    pass

def search_movies_by_cast():
    pass


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
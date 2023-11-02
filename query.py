from movies import Movies

if __name__ == "__main__":
    movies = Movies('./movies.txt')
    
    while True:
        print("\nMenu:")
        print("1. List all movie names")
        print("2. Search movies by name")
        print("3. Search movies by cast")
        print("q. Quit")
        
        choice = input("Enter your choice: ")
        print("")
        if choice == '1':
            for movie in movies._movies:
                print(movie['name'])

        elif choice == '2':
            search_term = input("Enter the search term: ").lower()
            print("")
            found_movies = [movie for movie in movies._movies if search_term in movie['name'].lower()]
    
            if found_movies:
                for movie in found_movies:
                    print(movie['name'])
            else:
                print("No matching movies found.")

        elif choice == '3':
            search_term = input("Enter the search term: ").lower()
            print("")
            matching_movies = []

            for movie in movies._movies:
                matching_cast = [actor for actor in movie['cast'] if search_term in actor.lower()]
                if matching_cast:
                    matching_movies.append((movie['name'], matching_cast))

            if matching_movies:
                for movie, cast in matching_movies:
                    print(movie)
                    print(cast)
                    print("")
            else:
                print("No matching movies found.")

        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

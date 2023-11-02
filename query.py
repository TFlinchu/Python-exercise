from movies import Movies

if __name__ == "__main__":
    movies = Movies('./movies.txt')
    
    while True:
        print("\nMenu:")
        print("1. List all movie names")
        print("q. Quit")
        
        choice = input("Enter your choice: ")
        print("")
        if choice == '1':
            for movie in movies._movies:
                print(movie['name'])
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

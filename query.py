from movies import Movies

if __name__ == "__main__":
    movies = Movies('./movies.txt')
    
    while True:
        print("Menu:")
        print("q. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

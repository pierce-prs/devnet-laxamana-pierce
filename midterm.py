"""
Midterm Practical Exam — Movie Collection Manager
Student: [Laxamana, Pierce Darby A.]
"""

movie_list = []


def display_menu(): 
    print("\n=== Movie Collection Manager ===")
    print("1. Add a Movie")
    print("2. View Movies")
    print("3. Count Watched/Unwatched")
    print("4. Find a Movie")
    print("5. Exit")
    return input("Choose an Option: ").strip()


def add_movie(movie_list):
    print("\nAdd a Movie")
    print("-----------")
    title = input("Enter the movie title: ").strip()
    director = input("Enter the director's name: ").strip()
    
    
    year = int(input("Enter the release year: "))
    
        
    status = input("Enter the status (watched/unwatched): ").strip().lower()
    watched = True if status == "watched" else False
    
    movie_list.append((title, director, year, watched))
    print(f"'{title}' has been added to your collection!")


def view_movies(movie_list):
    print("\n=== Your Movie Collection ===")
    if not movie_list:
        print("No movies in the collection.")
        return
        
    for movie in movie_list:
        title, director, year, watched = movie
        status = "Watched" if watched else "Unwatched"
        print(f"Title: {title}, Director: {director}, Year: {year}, Status: {status}")


def count_watched_unwatched(movie_list):
    if not movie_list:
        print("\nEmpty")
        return
        
    watched_count = sum(1 for movie in movie_list if movie[3]) #in movie in movie_ list
    unwatched_count = len(movie_list) - watched_count   # the length of the movie_list of the watch count subtratcted from watched count
    
    print("\nCollection")
    print(f"Watched Movies: {watched_count}")
    print(f"Unwatched Movies: {unwatched_count}")


def find_movie(movie_list):

    find_title = input("\nEnter the title of the movie to find: ").strip().lower() #lowering lower case will be equal to inputs and to function other functions 
    found_movies = []
    
    for movie in movie_list:
        title, director, year, watched = movie
        if find_title in title.lower():
            found_movies.append(movie)
            
    if found_movies:
        print(f"\nFound {len(found_movies)} match(es):")
        for movie in found_movies:
            title, director, year, watched = movie
            status = "Watched" if watched else "Unwatched"
            print(f"Title: {title}, Director: {director}, Year: {year}, Status: {status}")
    else:
        print("Movie not found.")


def main():

    while True:
        choice = display_menu()
        
        if choice == "1":
            add_movie(movie_list)
        elif choice == "2":
            view_movies(movie_list)
        elif choice == "3":
            count_watched_unwatched(movie_list)
        elif choice == "4":
            find_movie(movie_list)
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice.")

if __name__ == "__main__":
    main()

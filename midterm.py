"""
Midterm Practical Exam — Movie Collection Manager
Student: [Laxamana, Pierce Darby A.]
"""

movies = []
movielist = []
movie_list = []
find_title = []



def display_menu():
    print("Movie Collection Manager")
    print("1. Add a Movie")
    print("2. View Movies")
    print("3. Count Watched/Unwatched")
    print("4. Find a Movie")
    print("5. Exit")
    pass


def add_movie(movie_list):
    print("Add a Movie")
    print("-----------")
    print("Enter the movie title:")
    title = input().strip()
    print("Enter the director's name:")
    director = input().strip()
    print("Enter the release year:")
    year = int(input())
    print("Enter the status (watched/unwatched):")
    status = input().strip().lower()
    watched = True if status == "watched" else False

    movie_list.append((title, director, year, watched))
    pass


def view_movies(movie_list):
   for movie in movie_list:
        title, director, year, watched = movie
        status = "Watched" if watched else "Unwatched"
        print(f"Title: {title}, Director: {director}, Year: {year}, Status: {status}")
    
if not movie_list:
        print("No movies in the collection.")
pass


def count_watched_unwatched(movie_list):
    watched_count = 0
    unwatched_count = 0
    for movie in movie_list:
        title, director, year, watched = movie
        if watched:
            watched_count += 1
        else:
            unwatched_count += 1
    counts = (watched_count, unwatched_count)
    return counts
    pass


def find_movie(movie_list):
  find_title = input("Enter the title of the movie to find: ").strip().lower()
  found_movies = []
for movie in movie_list:
            title, director, year, watched = movie
            if find_title in title.lower():
                found_movies.append(movie)
        if found_movies:
        for movie in found_movies:
            title, director, year, watched = movie
            status = "Watched" if watched else "Unwatched"
            print(f"Title: {title}, Director: {director}, Year: {year}, Status: {status}")           

pass


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()

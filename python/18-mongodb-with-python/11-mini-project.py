import pymongo

if __name__ == "__main__":
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
    db = mongo_client['cinema']
    collections = db['movie']

    def movie_manager():
        while True:
            print("\nMovie Manager")
            print("1. Add Movie")
            print("2. Find Movie")
            print("3. List all the Movies")
            print("4. Update Movie")
            print("5. Delete Movie")
            print("6. Exit")
            choice = input("Enter your choice (1-5): ")

            # adding the movie
            if choice == "1":
                title = input("Enter movie title: ")
                director = input("Enter director: ")
                year = int(input("Enter year: "))
                genre = input("Enter genre: ")
                rating = float(input("Enter rating: "))
                movie = {
                    "title": title,
                    "director": director,
                    "year": year,
                    "genre": genre,
                    "rating": rating
                }
                collections.insert_one(movie)
                print("Movie added successfully.")

            # finding the movie
            elif choice == "2":
                search_title = input("Enter movie title to find: ")
                movie = collections.find_one({"title": {"$regex": search_title, "$options": "i"}})
                if movie:
                    print("Movie found:", movie)
                else:
                    print("Movie not found.")
            
            # list all the available moviees
            elif choice=="3":
                list_available_movies=collections.find()
                if list_available_movies:
                    for item in list_available_movies:
                        print(item)
                else:
                    print("collection not available")

            # update the movie
            elif choice == "4":
                update_title = input("Enter movie title to update: ")
                movie = collections.find_one({"title": update_title})
                if movie:
                    print("Leave blank to keep current value.")
                    new_director = input(f"Director [{movie['director']}]: ") or movie['director']
                    new_year = input(f"Year [{movie['year']}]: ") or movie['year']
                    new_genre = input(f"Genre [{movie['genre']}]: ") or movie['genre']
                    new_rating = input(f"Rating [{movie['rating']}]: ") or movie['rating']
                    collections.update_one(
                        {"title": update_title},
                        {"$set": {
                            "director": new_director,
                            "year": int(new_year),
                            "genre": new_genre,
                            "rating": float(new_rating)
                        }}
                    )
                    print("Movie updated successfully.")
                else:
                    print("Movie not found.")

            # delete the specifc moview
            elif choice == "5":
                delete_title = input("Enter movie title to delete: ")
                result = collections.delete_one({"title": delete_title})
                if result.deleted_count:
                    print("Movie deleted successfully.")
                else:
                    print("Movie not found.")
            # To exit from movie manager 
            elif choice == "6":
                print("Exiting Movie Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

    movie_manager()


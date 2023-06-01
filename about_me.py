"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        # TODO: Put full name into data structure
        'name': 'Helin Patel',
        # TODO: Put student ID into data structure
        'student id': '19292538',
        # TODO: Put list of 3 pizza toppings into data structure
        'pizza toppings': [
            'olives',
            'green olives',
            'green peper'
        ],
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'prem ratan dhan payo',
                'genre': 'romcom'
            },
            # TODO: Add one more movie
            {
                'title': 'men in black 1',
                'genre': 'thril'
            },
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['crispy onions', 'rosted garlic'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, '50 shades of grey', 'fantacy')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
    print(f"{my_info['name']} and my student id is {my_info['student id']}. ")

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings
C:\Users\helin\AppData\Local\Temp\Temp1_Lab 2 Script Templates[1].zip\Lab 2 Script Templates\about_me.py
    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    # Print bullet list of favourite pizza toppings
    print(f"My favourite pizza toppings are: ")

    for dressings_on_pizza in my_info['pizza toppings']:
        print(f"- {dressings_on_pizza}")

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['pizza toppings'].extend(toppings)
    # Convert all pizza toppings to lowercase
    # Sort toppings list alphabetically
    for i, dressings_on_pizza in enumerate(my_info['pizza toppings']):
        my_info['pizza toppings'][i] = dressings_on_pizza.capitalize()
    
    my_info['pizza toppings'].sort()
    return add_pizza_toppings

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    one_more_movie = {
        'title' : title,
        'genre' : genre
    }
    my_info['movies'].append(one_more_movie)
    
    return add_movie

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    print(f"I like to watch", end = ' ')

    for i,movies in enumerate(my_info['movies']):
        print(movies['genre'], end =', ')

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    movie_list = [movies['title'] for movies in movie_list]
    print(f"movies.\nSome of my favourite movies are",end=" ")
    print(', '.join(movie_list), end='. ')

if __name__ == '__main__':
    main()
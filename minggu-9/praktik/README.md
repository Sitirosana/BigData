1. Dissecting the anatomy of a DataFrame
    >>> movie = pd.read_csv('data/movie.csv')
    >>> movie.head()

2. Accessing the main DataFrame components

Use the DataFrame attributes index, columns, and values to assign the index, columns, and data to their own variables
    >>> movie = pd.read_csv('data/movie.csv')
    >>> index = movie.index
    >>> columns = movie.columns
    >>> data = movie.values

Display each component's values:
    >>> index
    RangeIndex(start=0, stop=5043, step=1)

    >>> columns
    Index(['color', 'director_name', 'num_critic_for_reviews',
           ...
           'imdb_score', 'aspect_ratio', 'movie_facebook_likes'],
           dtype='object')

    >>> data
    array([['Color', 'James Cameron', 723.0, ..., 7.9, 1.78, 33000],
          ...
      
3. Understanding data types

4. Selecting a single column of data as a Series
Pass a column name as a string to the indexing operator to select a Series of data:
    >>> movie = pd.read_csv('data/movie.csv')
    >>> movie['director_name']

    Alternatively, you may use the dot notation to accomplish the same task:
    >>> movie.director_name

4. Calling Series methods
    >>> s_attr_methods = set(dir(pd.Series))
    >>> len(s_attr_methods)
    442

    >>> df_attr_methods = set(dir(pd.DataFrame))
    >>> len(df_attr_methods)
    445

    >>> len(s_attr_methods & df_attr_methods)
    376

5. Working with operators on a Series
    >>> 5 + 9   # plus operator example adds 5 and 9
    14

    >>> 4 ** 2  # exponentiation operator raises 4 to the second power
    16

    >>> a = 10  # assignment operator assigns 10 to a

    >>> 5 <= 9  # less than or equal to operator returns a boolean
    True
    
    >>> 'abcde' + 'fg' 
    'abcdefg'

    >>> not (5 <= 9)
    False

    >>> 7 in [1, 2, 6]
    False

    >>> set([1,2,3]) & set([2,3,4])
    set([2,3])
    
6. Chaining Series methods together
    >>> person.drive('store')\
          .buy('food')\
          .drive('home')\
          .prepare('food')\
          .cook('food')\
          .serve('food')\
          .eat('food')\
          .cleanup('dishes')
          
7. Making the index meaningful
    >>> movie = pd.read_csv('data/movie.csv')
    >>> movie2 = movie.set_index('movie_title')
    >>> movie2
 
8. Renaming row and column names
    >>> idx_rename = {'Avatar':'Ratava', 'Spectre': 'Ertceps'} 
    >>> col_rename = {'director_name':'Director Name', 
                  'num_critic_for_reviews': 'Critical Reviews'} 
                  
9. Creating and deleting columns
    >>> movie = pd.read_csv('data/movie.csv')
    >>> movie['has_seen'] = 0
    
10. 

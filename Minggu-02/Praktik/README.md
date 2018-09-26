2. Using the Python Interpreter
  2.1.2. Interactive Mode
  
   the_word_is_flat = True
   the_world_is_flat = True
   if the_world_is_flat:
    print("Be Careful not to fall off!")
  Be Careful not to fall off!
  
  cara menampilkan pesan dengan menggunakan print
  
3. An Informal Introduction to Python
  3.1.1. Numbers
          
         2 + 2
         4
         50 - 5*6
         20
        (50 - 5*6)/ 4
        5.0
        8 / 5
        1.6
        17 / 3
        5.666666666666667
        17 // 3
        5
        17 % 3
        2
        5 * 3 + 2
        17
        5 ** 2
        25
        2 ** 7
        128
        width = 20
        height = 5 * 9
        width * height
        900
        n
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'n' is not defined
        4 * 3.75 - 1
        14.0
        tax = 12.5 / 100
        price = 100.50
        price * tax
        12.5625
        round(_, 2)
        12.56
        
       3.1.2. Strings
              'spam eggs'
              'spam eggs'
              'doesn\'t'
              "doesn't"
              "doesn't"
              "doesn't"
              '"Yes, "they said.'
              '"Yes, "they said.'
              "\"yes,\" they said."
              '"yes," they said.'
              '"Isn\'t," they said.'
              '"Isn\'t," they said.'
              
              '"Isn\'t," they said.'
              '"Isn\'t," they said.'
              print('"Isn\'t," they said.')
              "Isn't," they said.
              s = 'First line.\nSecond line.'
              s
              'First line.\nSecond line.'
              print(s)
              First line.
              Second line.
              
              print('C:\some\name')
              C:\some
              ame
              print(r'C:\some\name')
              C:\some\name
              
              'Py' 'thon'
              'Python'
              text = ('Put several strings within parenthese to have them joined together.')
              text
              'Put several strings within parenthese to have them joined together.'
              
              prefix = 'Py'
              prefix 'thon'
              File "<stdin>", line 1
                    prefix 'thon'
                          ^
              SyntaxError: invalid syntax

            prefix + 'thon'
            'Python'
            word = 'Python'
            word[0]
            'P'
            word[5]
            'n'
            word[-1]
            'n'
            word[-2]
            'o'
            word[-6]
            'P'
            word[0:2]
            'Py'
            word[2:5]
            'tho'
            word[:2] + word[2:]
            'Python'
            word[:4] + word[4:]
            'Python'
            word[:2]
            'Py'
            word[4:]
            'on'
            word[-2:]
            'on'
            
            word[42]
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            IndexError: string index out of range
            word[4:42]
            'on'
            word[42:]
            ''
            word[0] = 'J'
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: 'str' object does not support item assignment
            word[2:] = 'py'
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            TypeError: 'str' object does not support item assignment
            
            'J' + word[1:]
            'Jython'
            word[:2] + 'py'
            'Pypy'
            
     3.1.3. Lists
            squares = [1, 4, 9, 25]
            squares
            [1, 4, 9, 25]
            squares[0]
            1
            squares[-1]
            25
            squares[-3:]
            [4, 9, 25]
            squares[:]
            [1, 4, 9, 25]
            squares + [36, 49, 64, 81, 100]
            [1, 4, 9, 25, 36, 49, 64, 81, 100]
            
            cubes = [1, 8, 27, 65, 125]
            4 ** 3
            64
            cubes[3] = 64
            cubes
            [1, 8, 27, 64, 125]
 
            cubes.append(216)
            cubes.append(7 ** 3)
            cubes
            [1, 8, 27, 64, 125, 216, 343]
            
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            letters
            ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            letters[2:5] = ['C', 'D', 'E']
            letters
            ['a', 'b', 'C', 'D', 'E', 'f', 'g']
            letters[2:5] = []
            letters
            ['a', 'b', 'f', 'g']
            letters[:] = []
            letters
            []
            
            letters =['a', 'b', 'c', 'd']
            len(letters)
            4
            a = ['a', 'b', 'c']
            n = [1, 2, 3]
            x = [a, n]
            x
            [['a', 'b', 'c'], [1, 2, 3]]
            x[0]
            ['a', 'b', 'c']
            x[0][1]
            'b'
            
      3.2. First Steps Towards Programming
            a, b = 0, 1
            while a < 10:
                   print(a)
                   a, b = b, a+b
            ...
            0
            1
            1
            2
            3
            5
            8
            
            
              i = 256*256
              print('The value of i is', i)
              The value of i is 65536
              a, b = 0, 1
              while a < 1000:
                   print(a, end=',')
                   a, b = b, a+b
                ...
                0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
                
 4. More Control Flow Tools
  4.1. if Statements
        x = int(input("Please enter an integer"))
        Please enter an integer 42
         if x < 0:
             x = 0
             print('Negative Changed to zero')
         elif x == 0:
             print('Zero')
         elif x == 1:
             print('Single')
         else:
             print('More')
        
        More
        
  4.2. for Statements
         words = ['cat','window','defenestrate']
         for w in words:
             print(w, len(w))
        
         cat 3
         window 6
         defenestrate 12
         
         for w in words[:]:
               if len(w) > 6:
                       words.insert(0, w)
          
         words
          ['defenestrate', 'cat', 'window', 'defenestrate']
          
   4.3. The range() Function
        for i in range(5):
             print(i)
        
        0
        1
        2
        3
        4
        
    4.4. break and continue Statements, and else Clauses on Loops
          for n in range(2, 10):
               for x in range(2, n):
                       if n % x == 0:
                               print(n, 'equals', x, '*', n//x)
                               break
               else:
                       print(n, 'is a prime number')
          
          2 is a prime number
          3 is a prime number
          4 equals 2 * 2
          5 is a prime number
          6 equals 2 * 3
          7 is a prime number
          8 equals 2 * 4
          9 equals 3 * 3
          
     4.5. pass Statements
           while True:
               pass
      
     4.6. Defining Functions
          ef fib(n):
               """Print a Fibonacci series up to n."""
               a, b = 0, 1
               while a < n:
                       print(a, end=' ')
                       a, b = b, a+b
               print()
         
          fib(2000)
          0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
          
      4.7. More on Defining Functions
          4.7.1. Default Argument Values
                  def ask_ok(prompt, retries=4, reminder='Please try angin!'):
                  ...     while True:
                  ...             ok = input(prompt)
                  ...             if ok in ('y', 'ye', 'yes'):
                  ...                     return True
                  ...             if ok in ('n', 'no', 'nop', 'nope'):
                  ...                     return false
                  ...             retries = retries - 1
                  ...             if retries < 0:
                  ...                     raise ValueError('invalid user response')
                  ...             print(reminder)
                  ...
                  >>>
               
           4.7.2. Keyword Arguments
                  def parrot(valtage, state='a stiff', action='voom', type='Norwegian Blue'):
                  ...     print("-- This parrot wouldn't", action, end=' ')
                  ...     print("if you put", voltage, "volts through it")
                  ...     print("-- Lovely plumage, the", type)
                  ...     print("-- It's", state, "!")
                  
           4.7.3. Arbitrary Argument Lists
                  >>> def write_multiple_item(file, separator, *args):
                  ...     file.write(separator.join(args))
                  ...
                  
           4.7.4. Unpacking Argument Lists
                  >>> list(range(3, 6))
                  [3, 4, 5]
                  >>> args = [3, 6]
                  >>> list(range(*args))
                  [3, 4, 5]
                  
           4.7.5. Lambda Expressions
                  >>> def make_incrementor(n):
                  ...     return lambda x: x + n
                  ...
                  >>> f = make_incrementor(42)
                  >>> f(0)
                  42
                  >>> f(1)
                  43
                  
          4.7.6. Documentation Strings
                  >>> def my_function():
                  ...     """Do nothing, but document it.
                  ...
                  ...     No, really, it doesn't do anything.
                  ...     """
                  ...     pass
                  ...
                  >>> print(my_function.__doc__)
                  Do nothing, but document it.

                          No, really, it doesn't do anything.
                  
           4.7.7. Function Annotations
                  >>> def f(ham: str, eggs: str = 'eggs') -> str:
                  ...     print("Annotations:", f.__annotations__)
                  ...     print("Arguments:", ham, eggs)
                  ...     return ham + ' and ' + eggs
                  ...
                  >>> f ('spam')
                  Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
                  Arguments: spam eggs
                  'spam and eggs'
           
        
                


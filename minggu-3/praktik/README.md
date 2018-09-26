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
           
        
                

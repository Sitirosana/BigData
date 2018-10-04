  6. Modules
        >>> def fib(n):
        ...     a, b = 0, 1
        ...     while a < n:
        ...             print(a, end=' ')
        ...             a, b = b, a+b
        ...     print()
        ...
        
    >>> def fib2(n):
    ...     result = []
    ...     a, b = 0, 1
    ...     while a < n:
    ...             result.append(a)
    ...             a, b = b, a+b
    ...     return result
    ...
    >>> import sys
    
    untuk mengimport modul yang sudah ada 
    >>> sys.path.append(r'D:\python')
    >>> import fibo
    >>> fibo.fib(1000)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
    
    6.1. More on Modules
        >>> from fibo import fib, fib2
        >>> fib(500)
        0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
        
        6.1.1. Executing modules as scripts
                >>> import fibo
                >>>

        6.1.2. The Module Search Path
        6.1.3. “Compiled” Python files
    6.2. Standard Modules
          >>> import sys
          >>> sys.ps1
          '>>> '
          >>> sys.ps2
          '... '
          >>> sys.ps1 = 'C> '
          C> print('Yuck!')
          Yuck!
          C>
          
    6.3. The dir() Function
          >>> import sys
          >>> sys.path.append(r'D:\python')
          >>> import fibo
          >>> import fibo, sys
          >>> dir(fibo)
          ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']
          >>> dir(sys)
          ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__'
          , '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', 
          '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'api_version',
          'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats',
          'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit',
          'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',     'get_coroutine_wrapper',
          'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding',
          'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info',
          'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
          'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth',
          'set_coroutine_wrapper', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin',
          'stdout', 'thread_info', 'version', 'version_info', 'warnoptions', 'winver']
          >>> a = [1, 2, 3, 4, 5]
          >>> import fibo
          >>> fib = fibo.fib
          >>> dir()
          ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'fib', 'fibo', 'sys']
          
     6.4. Packages
          6.4.1. Importing * From a Package
          6.4.2. Intra-package References
          6.4.3. Packages in Multiple Directories
          
7. Input and Output
    7.1. Fancier Output Formatting
        >>> year = 2016
        >>> event = 'Referendum'
        >>> f'Results of the {year} {event}'
        'Results of the 2016 Referendum'
        >>> yes_votes = 42_572_654
        >>> no_votes = 43_132_495
        >>> percentage = yes_votes / (yes_votes + no_votes)
        >>> '{:-9} YES votes {:2.2%}' .format(yes_votes, percentage)
        ' 42572654 YES votes 49.67%'
        >>> 7.1. Fancier Output Formatting
        
     7.1.1. Formatted String Literals
            >>> import math
            >>> print(f'The value of pi is approximately {math.pi:.3f}.')
            The value of pi is approximately 3.142.
            >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
            >>> for name, phone in table.items():
            ...     print(f'{name:10} ==> {phone:10d}')
            ...
            Sjoerd     ==>       4127
            Jack       ==>       4098
            Dcab       ==>       7678
            
     7.1.2. The String format() Method
            >>> print('We are the {} who say "{}!"'.format('knight', 'Ni'))
            We are the knight who say "Ni!"
            
     7.1.3. Manual String Formatting
            >>> for x in range(1, 11):
            ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
            ...     print(repr(x*x*x).rjust(4))
            ...
             1   1    1
             2   4    8
             3   9   27
             4  16   64
             5  25  125
             6  36  216
             7  49  343
             8  64  512
             9  81  729
            10 100 1000
            
     7.1.4. Old string formatting
            >>> import math
            >>> print('The value of pi is approximately %5.3f.' % math.pi)
            The value of pi is approximately 3.142.
            
7.2. Reading and Writing Files
      >>> f = open('workfile', 'w')
      >>> with open('workfile') as f:
      ...     read_data = f.read()
      ...
      >>> f.closed
      True 
      >>> f.close()
      >>> f.read()
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      ValueError: I/O operation on closed file.
      
   7.2.1. Methods of File Objects
          >>> f = open('workfile', 'rb+')
          >>> f.write(b'0123456789abcdef')
          16
          >>> f.seek(5)
          5
          >>> f.read(1)
          b'5'
          >>> f.seek(-3, 2)
          13
          >>> f.read(1)
          b'd'
          
   7.2.2. Saving structured data with json
          >>> import json
          >>> json.dumps([1, 'simple', 'list'])
          '[1, "simple", "list"]'
 
 8. Errors and Exceptions
    8.1. Syntax Errors
          >>> while True print('Hello world')
            File "<stdin>", line 1
              while True print('Hello world')
                             ^
          SyntaxError: invalid syntax
  
    8.2. Exceptions
          >>> 10 * (1/0)
          Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
          ZeroDivisionError: division by zero
          >>> 4 + spam*3
          Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
          NameError: name 'spam' is not defined
          >>> '2' + 2
          Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
          TypeError: can only concatenate str (not "int") to str
  
    8.3. Handling Exceptions
          >>> while True:
              ...     try:
              ...             x = int(input("Please enter a number: "))
              ...             break
              ...     except ValueError:
              ...             print("Oops! That was no valid number. Try again...")
              ...
              
    8.4. Raising Exceptions
          >>> raise NameError('HiThere')
          Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
          NameError: HiThere
  
    8.5. User-defined Exceptions
    8.6. Defining Clean-up Actions
          >>> try:
          ...     raise KeyboardInterrupt
          ... finally:
          ...     print('Goodbye, World!')
          ...
          Goodbye, World!
          Traceback (most recent call last):
            File "<stdin>", line 2, in <module>
          KeyboardInterrupt
  
    8.7. Predefined Clean-up Actions
 9. Classes
    9.1. A Word About Names and Objects
    9.2. Python Scopes and Namespaces
        9.2.1. Scopes and Namespaces Example
    9.3. A First Look at Classes
        9.3.1. Class Definition Syntax
        9.3.2. Class Objects
                >>> class Complex:
                ...     def __init__(self, realpart, imagpart):
                ...             self.r = realpart
                ...             self.i = imagpart
                ...
                >>> x = Complex(3.0, -4.5)
                >>> x.r, x.i
                (3.0, -4.5)
                
       9.3.3. Instance Objects
       9.3.4. Method Objects
       9.3.5. Class and Instance Variables
       
  
          
          
          
            
            
               

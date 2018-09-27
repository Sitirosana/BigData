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
          'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper',
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
               

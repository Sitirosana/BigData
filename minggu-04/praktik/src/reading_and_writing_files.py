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

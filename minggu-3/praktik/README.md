5. Data Structures
    5.1. More on Lists
          >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
          >>> fruits.count('apple')
          2
          >>> fruits.count('tangerine')
          0
          >>> fruits.index('banana')
          3
          >>> fruits.index('banana', 4)
          6
          >>> fruits.reverse()
          >>> fruits
          ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
          >>> fruits.append('grape')
          >>> fruits
          ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
          >>> fruits.sort()
          >>> fruits
          ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
          >>> fruits.pop()
          'pear'
          
          insert, remove atau sort yang hanya memodifikasi daftar tidak memiliki nilai pengembalian yang
          dicetak mereka mengembalikan default None
          
     5.1.1. Using Lists as Stack
            >>> stack = [3, 4, 5]
            >>> stack.append(6)
            >>> stack.append(7)
            >>> stack
            [3, 4, 5, 6, 7]
            >>> stack.pop()
            7
            >>> stack
            [3, 4, 5, 6]
            >>> stack.pop()
            6
            >>> stack.pop()
            5
            >>> stack
            [3, 4]
            
            elemen pertama yang diambil ("terakhir-masuk, pertama-keluar"). Untuk menambahkan item ke bagian atas tumpukan,
            gunakan tambahkan (). Untuk mengambil item dari bagian atas tumpukan, gunakan pop () tanpa indeks eksplisit.
            
     5.1.2. Using Lists as Queues
            >>> from collections import deque
            >>> queue = deque(["Eric", "John", "Michael"])
            >>> queue.append("Terry")
            >>> queue.append("Graham")
            >>> queue.popleft()
            'Eric'
            >>> queue.popleft()
            'John'
            >>> queue
            deque(['Michael', 'Terry', 'Graham'])
            
            Untuk menerapkan antrean, gunakan collections.deque yang dirancang agar memiliki penambahan cepat dan muncul dari kedua                 ujungnya
            
     5.1.3. List Comprehensions
            >>> squares = []
            >>> for x in range(10):
            ...     squares.append(x**2)
            ...
            >>> squares
            [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
            
            untuk menciptakan kelanjutan dari elemen-elemen yang memenuhi suatu kondisi tertentu.
            
     5.1.4. Nested List Comprehensions
            >>> matrix = [
            ...     [1, 2, 3, 4],
            ...     [5, 6, 7, 8],
            ...     [9, 10, 11, 12],
            ... ]
     
            matriks 3x4 yang diimplementasikan sebagai daftar 3 daftar panjang 4
            
 5.2. The del statement
      >>> a = [-1, 1, 66.25, 333, 333, 1234.5]
      >>> del a[0]
      >>> a
      [1, 66.25, 333, 333, 1234.5]
      >>> del a[2:4]
      >>> a
      [1, 66.25, 1234.5]
      >>> del a[:]
      >>> a
      []
      
      Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar 
      (yang kita lakukan sebelumnya dengan penugasan daftar kosong ke slice)
      
 5.3. Tuples and Sequences
      >>> t = 12345, 54321, 'hello!'
      >>> t[0]
      12345
      >>> t
      (12345, 54321, 'hello!')
      >>> u = t, (1, 2, 3, 4, 5)
      >>> u
      ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
      >>> t[0] = 88888
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      TypeError: 'tuple' object does not support item assignment
      >>> v = ([1, 2, 3], [3, 2, 1])
      >>> v
      ([1, 2, 3], [3, 2, 1])
 
      tipe data urutan standar  tuple.
      
 5.4. Sets
      >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
      >>> print(basket)
      {'banana', 'orange', 'apple', 'pear'}
      >>> 'orange' in basket
      True
      >>> 'crabgrass' in basket
      False
      >>> a = set('abracadabra')
      >>> b = set('alacazam')
      >>> a
      {'c', 'b', 'r', 'a', 'd'}
      >>> a - b
      {'d', 'b', 'r'}
      >>> a | b
      {'c', 'm', 'b', 'r', 'z', 'a', 'l', 'd'}
      >>> a & b
      {'a', 'c'}
      >>> a ^ b
      {'z', 'm', 'b', 'r', 'l', 'd'}
      
      digunakan untuk membuat set
      
 5.5. Dictionaries
      >>> tel = {'jack': 4098, 'sape': 4139}
      >>> tel['guido'] = 4127
      >>> tel
      {'jack': 4098, 'sape': 4139, 'guido': 4127}
      >>> tel['jack']
      4098
      >>> del tel['sape']
      >>> tel['irv'] = 4127
      >>> tel
      {'jack': 4098, 'guido': 4127, 'irv': 4127}
      >>> list(tel)
      ['jack', 'guido', 'irv']
      >>> sorted(tel)
      ['guido', 'irv', 'jack']
      >>> 'guido' in tel
      True
      >>> 'jack' not in tel
      False
      
 5.6. Looping Techniques
      >>> knights ={'gallahad': 'the pure', 'robin': 'the brave'}
      >>> for k, v in knights.items():
      ...     print(k, v)
      ...
      gallahad the pure
      robin the brave
      
      Ketika mengulang melalui kamus, kunci dan nilai yang terkait dapat diambil pada saat yang sama menggunakan metode item ().
 
 5.7. More on Conditions
      >>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
      >>> non_null = string1 or string2 or string3
      >>> non_null
      'Trondheim'
   

        
   
      

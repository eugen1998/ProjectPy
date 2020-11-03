import time
import os

str1 = """
******Заметки лесника******

Погода была пасмурной.
...
...
"""

str2 = """
******Заметки лесника******

Погода была пасмурной.
Шел дождь.
...
"""

str3 = """
******Заметки лесника******

Погода была пасмурной.
Шел дождь.
Но настроение все равно хорошее!
"""


os.system('cls')

print(str1, end='\r')
time.sleep(1)

print(str2, end='\r')
time.sleep(1)

print(str3, end='\r')
time.sleep(1)

print('Hallo, die Welt!')

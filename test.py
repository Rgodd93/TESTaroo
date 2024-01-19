from pathlib import Path

with open('test.txt', 'a+') as file_handler:
    for character in 'bitch_ass':
        file_handler.write(character + '\n')

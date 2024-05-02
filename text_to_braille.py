from gpiozero import LED
import time

Led1 = LED(14) 
Led2 = LED(15) 
Led3 = LED(18) 

Led4 = LED(23) 
Led5 = LED(24) 
Led6 = LED(25) 

def map_a_to_j(letter, add = []):

    dist = {
        1 : Led1,
        2 : Led2,
        3 : Led3,
        4 : Led4,
        5 : Led5,
        6 : Led6
    }

    if 'a' <= letter <= 'j':
        map_letters = {
            'a': [1],
            'b': [1, 2],
            'c': [1, 4],
            'd': [1, 4, 5],
            'e': [1, 5],
            'f': [1, 2, 4],
            'g': [1, 2, 4, 5],
            'h': [1, 2, 5],
            'i': [2, 4],
            'j': [2, 4, 5]
        } 
        lst = []

        for n in map_letters[letter]:
            lst.append(dist[n])

        if add: 
            for n in add:
                lst.append(dist[n])

        return lst
    elif 'j' <= letter <= 't':
        return map_a_to_j(chr(ord(letter) - 10), [3])
    else:
        return map_a_to_j(chr(ord(letter) - 20), [3, 6])



    






lst = map_a_to_j('q')
while True:
    for n in lst:
        n.on()



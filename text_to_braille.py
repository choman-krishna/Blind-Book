from gpiozero import LED
import time

# Cell 2
Led_b1 = LED(14) 
Led_b2 = LED(15) 
Led_b3 = LED(18)
Led_b4 = LED(23) 
Led_b5 = LED(24) 
Led_b6 = LED(25) 

# Cell 1 
Led_a1 = LED(26) 
Led_a2 = LED(7) 
Led_a3 = LED(1)
Led_a4 = LED(16) 
Led_a5 = LED(20) 
Led_a6 = LED(21) 



#  Dict of Cells
cells = {
    1 : [Led_a1, Led_a2, Led_a3, Led_a4, Led_a5, Led_a6],
    2 : [Led_b1, Led_b2, Led_b3, Led_b4, Led_b5, Led_b6]
}

# Text to Braille
def map_to_braille(letter, cell_no, add = []):

    dist = {
        1 : cells[cell_no][0],
        2 : cells[cell_no][1],
        3 : cells[cell_no][2],
        4 : cells[cell_no][3],
        5 : cells[cell_no][4],
        6 : cells[cell_no][5]
    }

    # a - j
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
    # k - t
    elif 'k' <= letter <= 't':
        return map_to_braille(chr(ord(letter) - 10), cell_no, [3])
    # u - z
    else:
        return map_to_braille(chr(ord(letter) - 20), cell_no, [3, 6])

# Function to ON LED
def on_led(lst):
    # Infinite Loop to keep the LED ON
    while True:
        for cell in lst:
            for led in cell:
                led.on()


cell_no = 1
lst = []

words = ["hi", "OK", "NO", "DO"]

for c in words[1]:
    lst.append(map_to_braille(c.lower(), cell_no))
    cell_no += 1

for cell in lst:
            for led in cell:
                print("Before",led)
on_led(lst)




def map_a_to_j(letter, add = []):

    dist = {
        1 : (0,0),
        2 : (1,0),
        3 : (2,0),
        4 : (0,1),
        5 : (1,1),
        6 : (2,1)
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



    



matrix = [[False] * 2 for _ in range(3)]



lst = map_a_to_j('v')
for n in lst:
    matrix[n[0]][n[1]] = True

for row in matrix:
    print(row)
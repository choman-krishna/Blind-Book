
matrix = [[False] * 2 for _ in range(3)]


#  a - j
dist = {
    1 : (0,0),
    2 : (1,0),
    3 : (2,0),
    4 : (0,1),
    5 : (1,1),
    6 : (2,1),
}

map_letters = {
    'a' : (1,),
    'b' : (1,2),
    'c' : (1,4),
    'd' : (1,4,5),
    'e' : (1,5),
    'f' : (1,2,4),
    'g' : (1,2,4,5),
    'h' : (1,2,5),
    'i' : (2,4),
    'j' : (2,4,5)
}

# k -t 


lst = []

for n in map_letters['h']:
    lst.append(dist[n])

for n in lst:
    matrix[n[0]][n[1]] = True

for row in matrix:
    print(row)
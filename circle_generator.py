import math
from copy import copy, deepcopy

while True:
    in_string = input('Please enter "e" for even-center mode or "o" for odd-center mode: ')
    if in_string.lower() == 'e':
        even_mode = True
        break
    elif in_string.lower() == 'o':
        even_mode = False
        break

while True:
    in_string = input('Please enter "d" for diameter entry mode or "r" for radius entry mode: ')
    if in_string.lower() == 'd':
        diameter_mode = True
        break
    elif in_string.lower() == 'r':
        diameter_mode = False
        break

while True:
    in_string = input('Please enter "f" for fully filled in, "c" for corners adjacent to the outside to be filled, or "n" for no fill: ')
    if in_string.lower() == 'f':
        fill_mode = 2
        break
    elif in_string.lower() == 'c':
        fill_mode = 1
        break
    elif in_string.lower() == 'n':
        fill_mode = 0
        break

while True:
    radius = 0.0
    if diameter_mode:
        in_string = input("Please input the desired diameter of the circle: ")
        radius = float(in_string) / 2
    else:
        in_string = input("Please input the desired radius of the circle: ")
        radius = float(in_string)
    if even_mode:
        int_radius = math.floor(radius - 0.5) + 1
        if math.sqrt((int_radius - 0.5) ** 2 + (0.5) ** 2) > radius:
            int_radius -= 1
    else:
        int_radius = math.floor(radius) + 1
    quadrant = [[0]*int_radius for i in range(int_radius)]
    for x in range(int_radius):
        for y in range(int_radius):
            if even_mode:
                dist = math.sqrt((x + 0.5) ** 2 + (y + 0.5) ** 2)
            else:
                dist = math.sqrt(x ** 2 + y ** 2)
            if dist <= radius:
                quadrant[x][y] = 1
    if fill_mode == 1:
        for i in range(1 - int_radius, int_radius, 1):
            x = int_radius - 1
            y = int_radius - 1
            if i < 0:
                x += i
            if i > 0:
                y -= i
            encounter = False
            while x >= 0 and y >= 0:
                if not encounter:
                    if quadrant[x][y] == 1:
                        encounter = True
                else:
                    quadrant[x][y] = 0
                x -= 1
                y -= 1
    if fill_mode == 0:
        original = deepcopy(quadrant)
        for x in range(int_radius):
            encounter = False
            for y in range(int_radius - 1, -1, -1):
                if not encounter:
                    if quadrant[x][y] == 1:
                        encounter = True
                else:
                    quadrant[x][y] = 0
        for y in range(int_radius):
            encounter = False
            for x in range(int_radius - 1, -1, -1):
                if not encounter:
                    if original[x][y] == 1:
                        encounter = True
                        quadrant[x][y] = 1
    if even_mode:
        for y in range(int_radius - 1, -1, -1):
            out_string = ' '
            for x in range(int_radius - 1, -1, -1):
                if quadrant[x][y] == 1:
                    out_string += 'O '
                else:
                    out_string += '+ '
            for x in range(int_radius):
                if quadrant[x][y] == 1:
                    out_string += 'O '
                else:
                    out_string += '+ '
            print(out_string)
        for y in range(int_radius):
            out_string = ' '
            for x in range(int_radius - 1, -1, -1):
                if quadrant[x][y] == 1:
                    out_string += 'O '
                else:
                    out_string += '+ '
            for x in range(int_radius):
                if quadrant[x][y] == 1:
                    out_string += 'O '
                else:
                    out_string += '+ '
            print(out_string)
    else:
        for y in range(int_radius - 1, 0, -1):
            out_string = ' '
            for x in range(int_radius - 1, 0, -1):
                if quadrant[x][y] == 1:
                    out_string += 'O '
                else:
                    out_string += '+ '
            for x in range(int_radius):
                if quadrant[x][y] == 1:
                    out_string += 'O '
                else:
                    out_string += '+ '
            print(out_string)
        for y in range(int_radius):
            out_string = ' '
            for x in range(int_radius - 1, 0, -1):
                if quadrant[x][y] == 1:
                    out_string += 'O '
                else:
                    out_string += '+ '
            for x in range(int_radius):
                if quadrant[x][y] == 1:
                    out_string += 'O '
                else:
                    out_string += '+ '
            print(out_string)
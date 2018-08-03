import os
import time

# █ ヸ ▓

#  __                  _   _
# / _|_   _ _ __   ___| |_(_) ___  _ __  ___
#| |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#|  _| |_| | | | | (__| |_| | (_) | | | \__ \
#|_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/


    # Rotating

def rotate_square_matrix(arr):

    rot = [[] for a in range(len(arr))];

    i = len(arr) - 1

    while ( i >= 0 ):

        for s in range(len(arr)):

            rot[s].append(arr[i][s])

        i = i -1

    return rot


    # Formatting the output

def print_tetris_object(array):

    for i in range(len(array)):
        result = str(array[i]).replace("[","").replace("]","").replace(" ","").replace(".","..").replace(",","").replace("'","").replace("..","  ")
        print(result)



#
#                 _       _     _
#__   ____ _ _ __(_) __ _| |__ | | ___  ___
#\ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
# \ V / (_| | |  | | (_| | |_) | |  __/\__ \
#  \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
#

# defining tetris shapes

shape_1 =[
           ["ヸ",".","ヸ"],  #ヸ  ヸ
           [".","ヸ","."],   #  ヸ
           [".","ヸ","."],   #  ヸ
         ]

shape_2 =[
           [".",".","."],    #
           [".","ヸ","."],   #  ヸ
           ["ヸ","ヸ","ヸ"]  #ヸヸヸ
         ]

shape_3 =[
           [".",".","ヸ"],   #    ヸ
           [".",".","ヸ"],   #    ヸ
           [".","ヸ","ヸ"]   #  ヸヸ
         ]

shape_4 =[
           [".","ヸ","ヸ"],  #  ヸヸ
           [".","ヸ","."],   #  ヸ
           ["ヸ","ヸ","."]   #ヸヸ
         ]

shape_5 =[
           ["ヸ",".","."],   #ヸ
           [".","ヸ" ,"."],  #  ヸ
           [".",".","ヸ"]    #    ヸ
         ]
shape_6 =[
           [".","ヸ","."],   #  ヸ
           [".","ヸ" ,"."],  #  ヸ
           ["ヸ","ヸ","ヸ"]  #ヸヸヸ
         ]
shape_7 =[
           [".",".","."],    #
           [".","ヸ","."],   #  ヸ
           [".",".","."]     #
         ]

shape_8 =[
           ["ヸ","ヸ","ヸ"], #ヸヸヸ
           ["ヸ","ヸ","ヸ"], #ヸヸヸ
           ["ヸ","ヸ","ヸ"]  #ヸヸヸ
         ]
shape_9 =[
           [".",".","."],    #
           [".","ヸ","ヸ"],  #  ヸヸ
           [".",".","."]     #
         ]
shape_10 =[
           ["ヸ",".","."],   #ヸ
           ["ヸ",".","."],   #ヸ
           ["ヸ","ヸ","."]   #ヸヸ
         ]
shape_11 =[
           [".",".","."],    #
           ["ヸ",".","ヸ"],  #ヸ  ヸ
           ["ヸ","ヸ","ヸ"]  #ヸヸヸ
         ]
shape_12 =[
           ["ヸ","ヸ","ヸ"], # ヸヸヸ
           ["ヸ",".","."],   # ヸ
           ["ヸ",".","."]    # ヸ
         ]
shape_13 =[
           [".","ヸ","."],   #  ヸ
           ["ヸ","ヸ","ヸ"], #ヸヸヸ
           [".","ヸ","."]    #  ヸ
         ]
#shape_8 =[
#           ["ヸ","ヸ","ヸ"],    #
#           ["ヸ","ヸ","ヸ"],    #  ヸ
#           ["ヸ","ヸ","ヸ"]     #
#         ]
#shape_8 =[
#           ["ヸ","ヸ","ヸ"],    #
#           ["ヸ","ヸ","ヸ"],    #  ヸ
#           ["ヸ","ヸ","ヸ"]     #
#         ]
#shape_8 =[
#           ["ヸ","ヸ","ヸ"],    #
#           ["ヸ","ヸ","ヸ"],    #  ヸ
#           ["ヸ","ヸ","ヸ"]     #
#         ]
#shape_8 =[
#           ["ヸ","ヸ","ヸ"],    #
#           ["ヸ","ヸ","ヸ"],    #  ヸ
#           ["ヸ","ヸ","ヸ"]     #
#         ]
#shape_8 =[
#           ["ヸ","ヸ","ヸ"],    #
#           ["ヸ","ヸ","ヸ"],    #  ヸ
#           ["ヸ","ヸ","ヸ"]     #
#         ]

#
# ____              _   _
#|  _ \ _   _ _ __ | |_(_)_ __ ___   ___
#| |_) | | | | '_ \| __| | '_ ` _ \ / _ \
#|  _ <| |_| | | | | |_| | | | | | |  __/
#|_| \_\\__,_|_| |_|\__|_|_| |_| |_|\___|
#


# ____  _     ___  ____  ______   __     _    ____    _____ _   _  ____ _  __
#/ ___|| |   / _ \|  _ \|  _ \ \ / /    / \  / ___|  |  ___| | | |/ ___| |/ /
#\___ \| |  | | | | |_) | |_) \ V /    / _ \ \___ \  | |_  | | | | |   | ' /
# ___) | |__| |_| |  __/|  __/ | |    / ___ \ ___) | |  _| | |_| | |___| . \
#|____/|_____\___/|_|   |_|    |_|   /_/   \_\____/  |_|    \___/ \____|_|\_\
#

while True:

    # rotating 90°
    #input()
    time.sleep(0.3)
    os.system("clear")
    print("shape_1\n")
    print_tetris_object(rotate_square_matrix(shape_1))
    print("shape_2\n")
    print_tetris_object(rotate_square_matrix(shape_2))
    print("shape_3\n")
    print_tetris_object(rotate_square_matrix(shape_3))
    print("shape_4\n")
    print_tetris_object(rotate_square_matrix(shape_4))
    print("shape_5\n")
    print_tetris_object(rotate_square_matrix(shape_5))
    print("shape_6\n")
    print_tetris_object(rotate_square_matrix(shape_6))
    print("shape_7\n")
    print_tetris_object(rotate_square_matrix(shape_7))
    print("shape_8\n")
    print_tetris_object(rotate_square_matrix(shape_8))
    print("shape_9\n")
    print_tetris_object(rotate_square_matrix(shape_9))
    print("shape_10\n")
    print_tetris_object(rotate_square_matrix(shape_10))
    print("shape_11\n")
    print_tetris_object(rotate_square_matrix(shape_11))
    print("shape_12\n")
    print_tetris_object(rotate_square_matrix(shape_12))
    print("shape_13\n")
    print_tetris_object(rotate_square_matrix(shape_13))

    # rotating 180°
    #input()
    time.sleep(0.3)
    os.system("clear")
    print("shape_1\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_1)))
    print("shape_2\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_2)))
    print("shape_3\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_3)))
    print("shape_4\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_4)))
    print("shape_5\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_5)))
    print("shape_6\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_6)))
    print("shape_7\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_7)))
    print("shape_8\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_8)))
    print("shape_9\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_9)))
    print("shape_10\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_10)))
    print("shape_11\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_11)))
    print("shape_12\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_12)))
    print("shape_13\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(shape_13)))

    # rotating 270°
    #input()
    time.sleep(0.3)
    os.system("clear")
    print("shape_1\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_1))))
    print("shape_2\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_2))))
    print("shape_3\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_3))))
    print("shape_4\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_4))))
    print("shape_5\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_5))))
    print("shape_6\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_6))))
    print("shape_7\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_7))))
    print("shape_8\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_8))))
    print("shape_9\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_9))))
    print("shape_10\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_10))))
    print("shape_11\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_11))))
    print("shape_12\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_12))))
    print("shape_13\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_13))))

    # rotatin 360°
    #input()
    time.sleep(0.3)
    os.system("clear")
    print("shape_1\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_1)))))
    print("shape_2\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_2)))))
    print("shape_3\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_3)))))
    print("shape_4\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_4)))))
    print("shape_5\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_5)))))
    print("shape_6\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_6)))))
    print("shape_7\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_7)))))
    print("shape_8\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_8)))))
    print("shape_9\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_9)))))
    print("shape_10\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_10)))))
    print("shape_11\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_11)))))
    print("shape_12\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_12)))))
    print("shape_13\n")
    print_tetris_object(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(rotate_square_matrix(shape_13)))))



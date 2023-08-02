from prog import seat_to_bin

seats = ["FFFF", # 0000 = 0
        "FFFB", # 0001 = 1
        "FFBF", # 0010 = 2
        "FFBB", # 0011 = 3
        "FBFF", # 0100 = 4
        "FBFB", # 0101 = 5
        "FBBF", # 0110 = 6
        "FBBB", # 0111 = 7
        "BFFF", # 1000 = 8
        "BFFB", # 1001 = 10
        "BFBF", # 1010 = 11
        "BFBB", # 1011 = 12
        "BBFF", # 1100 = 13
        "BBFB", # 1101 = 14
        "BBBF", # 1110 = 15
        "BBBB", # 1111 = 16
]

expected = list(range(17))

for v, e in zip(seats, expected):
    actual = seat_to_bin(v)
    if actual != e:
        print(v, actual, e)

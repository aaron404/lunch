
data = [
    0x84a5e97,
    0x84b5091,
    0x84ad0f3,
    0x84a5090,
    0xf7a5e92,
]

for d in data:
    b = bin(d)[2:]
    for c in b:
        print([" ", "*"][int(c)], end="")
    print()

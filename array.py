x = [3, 2.7, 2.5, 4]
def a(y):
    b = 500000
    c = y * b
    return c

for d in x:
    print(d)
    if d > 3:
        print("Selamat anda mendapatkan bonus sebesar Rp.", a(d))
    else:
        print("Maaf anda belum beruntung")
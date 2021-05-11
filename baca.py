papan = [["?" for j in range (13)] for i in range (13)]

def baca(path):
    f = open(path,"r")
    text = f.readlines()

    # baca ukuran papan
    N = int(text[0])
    
    # baca matriks
    for i in range (2*N-1):
        for j in range (2*N-1):
            papan[i][j] = text[i+1][j]
    return

def getDimension(papan):
    i = 0
    while (papan[0][i] != '?'):
        i+=1
    return i

def B(papan,N, i, j, num):
    # syarat 1: tidak boleh ada angka yang sama di kolom atau baris yang sama
    for a in range(0,N,2):
        if (int(papan[a][j]) == num and a != i):
            return False
        if (int(papan[i][a]) == num and a != j):
            return False
    # syarat 2: angka harus mematuhi tanda ketidaksamaan dan angka selisih yang ada di dekatnya jika ada
    if (i != 0):
        op = papan[i-1][j]
        com = int(papan[i-2][j])
        if (op != '-' and com != 0):
            if (op == '>' and num > com):
                return False
            elif (op == '<' and num < com):
                return False
            elif (op >= '0' and op <='6' and abs(num-com) != int(op)):
                return False
    if (i < N-1 ):
        op = papan[i+1][j]
        com = int(papan[i+2][j])
        if (op != '-' and com != 0):
            if (op == '>' and num <= com):
                return False
            elif (op == '<' and num >= com):
                return False
            elif (op >= '0' and op <='6' and abs(num - com) != int(op)):
                return False
    if (j != 0):
        op = papan[i][j-1]
        com = int(papan[i][j-2])
        if (op != '-' and com != 0):
            if (op == '>' and num > com):
                return False
            elif (op == '<' and num < com):
                return False
            elif (op >= '0' and op <='6' and abs(num - com) != int(op)):
                return False
    if (j < N-1 ):
        op = papan[i][j+1]
        com = int(papan[i][j+2])
        if (op != '-' and com != 0):
            if (op == '>' and num <= com):
                return False
            elif (op == '<' and num >= com):
                return False
            elif (op >= '0' and op <='6' and abs(num - com) != int(op)):
                return False
    # jika memenuhi kedua syarat
    return True

def solve(papan,i,j,hasil):
    N = getDimension(papan)
    for a in range (1,N//2+2):
        if (B(papan,N,i,j,a)):
            papan[i][j] = a
            if (i==N-1 and j==N-1):
                for a in range (0,N,2):
                    for b in range (0,N,2):
                        hasil.append(papan[a][b])
            else:
                if (j <= N-2):
                    solve(papan,i,j+2,hasil)
                else:
                    solve(papan,i+2,0,hasil)

baca("tes2.txt")
hasil = []
N = getDimension(papan)//2+1
solve(papan,0,0,hasil)
print("Hasil perhitungan (hanya matriks angka, diperoleh dari vektor N-tuple X):")
for i in range (N):
    for j in range (N):
        print(str(hasil[i*N+j])+" ",end="")
    print()
print("------------------------------------------------------------------------")
print("Hasil perhitungan (beserta tanda ketidaksamaan dan angka selisih):")
for i in range (getDimension(papan)):
    for j in range (getDimension(papan)):
        print(str(papan[i][j])+" ",end="")
    print() 
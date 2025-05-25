





def nhap_ma_tran(n, dong):
    print(f"nhap ma tran vuong cap {n}: ")
    for i in range(n):
        cot = []
        for j in range(n):
            x = int(input())
            cot.append(x)
        dong.append(cot)

def in_ma_tran(dong):
    print("ma tran vua nhap la: ")
    for i in range(n):
        for j in range(n):
            print(dong[i][j], end=" ")
        print()

def kiem_tra_doi_xung(n, dong):
    flag = True
    for i in range (n):
        for j in range (n):
            if dong[i][j] != dong [j][i]:
                flag = False
    if flag == True:
        print("ma tran doi xung")
    else:
        print("ma tran khong doi xung")
    
if __name__ == "__main__":
    print("nhap 1 so la cap cua ma tran: ")
    n = int(input())
    dong = []
    nhap_ma_tran(n, dong)
    in_ma_tran(dong)
    kiem_tra_doi_xung(n, dong)
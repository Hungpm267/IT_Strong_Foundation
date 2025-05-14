biensoxe = input("Nhập biển số xe: ")
while len(biensoxe) != 4 or not biensoxe.isdigit():
    print("Biển số xe không hợp lệ. Vui lòng nhập lại.")
    biensoxe = input("Nhập biển số xe: ")

biensoxe = int(biensoxe)
print("bien số xe của bạn là: ", biensoxe)

digit = 0
while biensoxe > 0:
    digit = digit + biensoxe%10
    biensoxe = biensoxe//10

print("Tổng các chữ số trong biển số xe là: ", digit)
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
if mau == 0:
    print("Mẫu số không được bằng 0!")
else:
    k = ucln(tu, mau)
    tu_rut = tu // k
    mau_rut = mau // k
    print("Phân số tối giản là:", tu_rut, "/", mau_rut)
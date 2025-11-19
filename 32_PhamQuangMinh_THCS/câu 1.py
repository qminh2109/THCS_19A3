so = int(input("Nhập một số nguyên: "))
if so >=0 :
    for i in range(int(so**0.5) + 1):
        if i*i == so:
            print("Là số chính phương")
            break
        else:
            print("Không phải số chính phương")
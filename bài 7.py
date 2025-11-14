tendangnhap = input ("Tên đăng nhập của bạn : ")
matkhau = input ("Nhập mật khẩu của bạn : ")
while tendangnhap == "admin" and matkhau != "password123" :
    print ("Mật khẩu bạn nhập không đúng , vui lòng nhập lại !")
    matkhau = input ("Nhập mật khẩu của bạn : ")    
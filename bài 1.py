gia_san_pham = float(input("Nhập giá sản phẩm (VND): "))
so_luong = int(input("Nhập số lượng mua: "))
tong_chi_phi = gia_san_pham * so_luong
thue_VAT = tong_chi_phi * 0.10
tong_tien = tong_chi_phi + thue_VAT
print(f"Tổng tiền phải trả (đã gồm VAT): {tong_tien:.2f} VND")
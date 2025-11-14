tiengui = float(input("Nhập số tiền gửi ban đầu (VND): "))
laisuatnam = float(input("Nhập lãi suất hàng năm (%): "))
laisuat = laisuatnam / 100
lai1thang = tiengui * laisuat * (1 / 12)
lai2quy = tiengui * laisuat * (6 / 12)
lai3nam = tiengui * laisuat * 3
print(f"Số tiền lãi sau 1 tháng: {lai1thang:,.0f} VND")
print(f"Số tiền lãi sau 2 quý: {lai2quy:,.0f} VND")
print(f"Số tiền lãi sau 3 năm: {lai3nam:,.0f} VND") 

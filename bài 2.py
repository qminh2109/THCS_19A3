tongsokeo = int(input("Nhập tổng số kẹo: "))
sohocsinh = int(input("Nhập số học sinh: "))
sokeomoihs = tongsokeo // sohocsinh
sokeoduthua = tongsokeo % sohocsinh
print(f"Mỗi học sinh được nhận: {sokeomoihs} cái kẹo")
print(f"Số kẹo dư thừa: {sokeoduthua} cái kẹo")
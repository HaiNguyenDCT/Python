year = int(input("Nhập một năm để kiểm tra: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Năm {year} là năm nhuận.")
else:
    print(f"Năm {year} không phải là năm nhuận.")
# Kiểm tra năm nhuận trong Python

if ((year-1) % 4 == 0 and (year-1) % 100 != 0) or ((year-1) % 400 == 0):
    print(f"Năm {year-1} là năm nhuận.")
else:
    if ((year+1) % 4 == 0 and (year+1) % 100 != 0) or ((year+1) % 400 == 0):
        print(f"Năm {year+1} là năm nhuận.")
    else:
        print("Không có năm nhuận trước sau")
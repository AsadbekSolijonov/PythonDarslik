bozorlik = ["go'sht", "lag'mon", "tuxum", "kartoshka", "un", "yog'", "piyoz"]
olindi = []
print(f"Bozorlik: {bozorlik}.")
print(F"Xarid qilindi: {olindi}.")
xarid = input('Nima xarid qilamiz?: ').lower()
if xarid in bozorlik:
    olindi.append(xarid)
    bozorlik.remove(xarid)
    print("Xarid qilindi.")
    print(f"Qoldi: {bozorlik}.")
    print(f"Xarid qilindi: {olindi}.")
else:
    print(f"{xarid} bozorlik ro'yxatida mavjud emas!\nIltimos qaytadan urinib ko'ring!")

def print_fio(fio, direct=False):
    f=fio.split()
    if direct:
        print(f"{f[0]} {f[1][0]}.{f[2][0]}.")
    else:
        print(f"{f[1][0]}.{f[2][0]}.{f[0]}")


fio="Starostenko Alelsandr Vasilievich"#input("Enter Fio:")
print_fio("Starostenko Alelsandr Vasilievich")  
print_fio("Starostenko Alelsandr Vasilievich",direct=True) 

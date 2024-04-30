string=input("enter Year:")
year = int(string)
if year >= 2020 and year<2025 :
    print("REBENOK")
elif year >= 2016 and year<2020 :
    print("PODROSTOK")
elif year >= 2010 and year<2016 :
    print("JUNOSHA")
elif year >= 1996 and year<2010 :
    print("RACVET SIL")
elif year >= 1965 and year<1996 :
    print("POJILOY")
elif year >= 1925 and year<1965 :
    print("STARIK")
else:
    print(f"{year} - Bad year")


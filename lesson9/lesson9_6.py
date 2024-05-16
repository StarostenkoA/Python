DaysTemp={"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

print(f"init - {DaysTemp}")
print(f"sorted - {sorted(DaysTemp.values(),key=lambda x:x)}")
print(f"sorted desc - {sorted(DaysTemp.values(),key=lambda x:x, reverse=True)}")

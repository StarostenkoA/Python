def printn(string):
    global CountStart
    print(f"func start {CountStart}, text - {string}")
    CountStart+=1


CountStart=1
printn("first")
printn("second")


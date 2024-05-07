def triangle(h,w, v=True):
    if v:
        print(f"v={h*w}")
    else:
        print(f"s={2*(h+w)}")


triangle(10,20)  
triangle(10,20,v=False) 

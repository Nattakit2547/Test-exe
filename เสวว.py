def get_box_area(w , l , h):
    if w < 0 or l < 0 or h < 0:
        return 0
    box_area = w * l * h
    return box_area

box1 = get_box_area(5 , -5 , 4)
box2 =get_box_area(w = 6 ,l =  7 ,h =  8)

print(box1)
color="y"
color_list=["red","green","white","black"]
while color!="x":
    color=input("enter color:x terminates...")
    if color!="x":
        color_list.append(color)
print("%s%s"%(color_list[0],color_list[-1]))
print((color_list[0],color_list[-1]))


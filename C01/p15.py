color_list1 = ["Red", "Purple", "Green", "Yellow", "Magenta"]
color_list2 = ["Red", "Purple", "Green", "Cyan", "Violet"]
only_list1 = [color for color in color_list1 if color not in color_list2 ]
print(only_list1)

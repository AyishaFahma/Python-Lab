from pack_main import circle
from pack_main.rectangle import *
import pack_main.pack_sub.cuboid
from pack_main.pack_sub import sphere

carea=circle.area_circle(5)
print("the area of the circle is : ",carea)
cperi=circle.peri_circle(5)
print("the perimeter of the circle is : ",cperi)

rarea=pack_main.rectangle.area_rect(10,5)
print("the area of the circle is : ",rarea)
rperi=pack_main.rectangle.peri_react(10,5)
print("the perimeter of the circle is : ",rperi)

print("Cuboid volume : ",pack_main.pack_sub.cuboid.volume_cuboid(10,5,7))
print("Cuboid perimeter : ",pack_main.pack_sub.cuboid.peri_cuboid(10,5,7))
print("Sphere surface area : ",sphere.surface_area_sphere(5))
print("Sphere volume : ",sphere.volume_sphere(5))

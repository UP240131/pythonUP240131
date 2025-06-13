edad=int(18)
altura=float(1.60)
complex_number = complex(1.0, 2.0)

base=int(input("ingrese la base:"))
heigth=int(input("ingresa la altura:"))
area=(0.5*base*heigth)
print("la area es de " ,area)

a=int(input("ingrese el lado a:"))
b=int(input("ingrese el lado b:"))
c=int(input("ingrese el lado c:"))
perimetro=(a+b+c)
print("el perimetro es de:" ,perimetro)

length=float(input())
width=float(input())
area_rectangule=length*width
perimeter_rec=2*(length+width)
print("area" ,area_rectangule)
print("perimetro" ,perimeter_rec)

radius=float(input())
pi=3.1416
area_circulo=pi*radius*radius
cir=2*pi*radius
print("Area" ,area_circulo)
print("Circunferenccia" ,cir)

intercepcion_x=1
intercepcion_y=-2
slope=2
print("Slope:",slope)
print("X-intercepcion:" ,intercepcion_x)
print("Y-intercepcion" ,intercepcion_y)

x1 , y1 = 2 ,2
x2 , y2 = 6 , 10
slope_1=(y2-y1)/(x2-x1)
dis = ((x2-x1)**2+(y2-y1)**2)**0.5
print("Slope:" , slope_1)
print("euclidean distance:" , dis)
print(slope == slope_1)

x_values= [-3,-2,-1,0,1,2,3]
for x in x_values:
    y = x**2 +6*x +9
    print("x:" , x, "y:" , y)

print(len("python")  == len("dragon"))

print('on' in 'python' and 'on' in 'dragon')

print('jaron' in 'I hope this course is not full of jaron')

print('on' not in 'dragon' and 'on' not in 'python')

length_python = len('python')
print(float(length_python))
print(str(length_python))

number = int( input())
print(number % 2 == 0)
print(7 // 3 == int(2.7))

print(type("10") == type(10))

print(int(float("9.8")) == 10)

h = float(input())
r = float(input())
p = h*r
print("your weekly earning is" , p)
years = int(input())
seconds = years * 365 *24 *60 *60
print("you have lived for" , seconds , "seconds")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")


def rectangle_area_calculate_v1(width, height):
    area = float(width) * float(height)
    print ("V1 Rectangle Area:",str(area))
    
 
wid = input("Enter the Width :")
 
hei = input("Enter the Height : ")
 
rectangle_area_calculate_v1(wid, hei)

def circle_area_calculate_v1(radius):
    area = float(radius) * float(radius)*3.14
    print ("V1 Circle Area :",str(area))
    

r = input("Enter the radius :")
 
circle_area_calculate_v1(r)

def rectangle_area_calculate_v2(width, height):
    area = float(width)*float(width)*float(height)*float(height)
    print("V2 Rectangle area :", str(area))

rectangle_area_calculate_v2(wid, hei)

def circle_area_calculate_v2(radius):
    area=float(radius)*float(radius)*float(radius)*float(radius)*3.14
    print("V2 Circle Area :" ,str(area))

circle_area_calculate_v2(r)

    

class Printer3D() : 
    brand = ""
    name = ""
    printing_type = ""
    resolution = ""
    price = ""

    def technology(self) : 
        print (self.name + " uses " + self.printing_type + " technology.")
    def material(self, material) :
        print (self.name +" uses " + material + " as material to print")

um3 = Printer3D()
um3.brand = "Ultimaker"
um3.name = "Ultimaker 3"
um3.printing_type = "Fused deposing modeling"
um3.resolution = "0.06 mm"
um3.price = "4500 .-"
um3.technology()

sl1 = Printer3D()
sl1.brand = "Prusa"
sl1.name = "Prusa SL1"
sl1.printing_type = "SLA"
sl1.resolution = "0.015 mm"
sl1.price = "5000 .-"
sl1.technology()
sl1.material("ABS resin")
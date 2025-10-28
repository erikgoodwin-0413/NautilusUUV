import numpy as np
SALT_WATER_DENSITY = 1025#kg/m^3
ATMOSPHERIC_PRESSURE = 101325 #Pa
GRAVITY = 9.81 #m/s^2
PI = 3.14
class submersible:
    def __init__(self):
        self.length = 1 #meter
        self.diameter = 0.25 #meter
        self.nose_fineness_ratio = 3
    def get_Nose_Volume(self):
        r =self.diameter/2
        h = self.nose_fineness_ratio * r
        V = 0.5 * PI * h * np.power(r,2)
        return V
    def get_Hull_Volume(self):
        L = self.length - (self.nose_fineness_ratio * self.diameter/2)
        V = PI * np.power(self.diameter/2, 2) * L
        return V
    def get_Total_Volume(self):
        V_t = self.get_Nose_Volume() + self.get_Hull_Volume()
        return V_t

UUV = submersible()
#Pressure
def calc_pressure(h):
    rho = SALT_WATER_DENSITY
    P_a = ATMOSPHERIC_PRESSURE
    g = GRAVITY
    P_t = P_a + (rho*g*h)
    return P_t/1000


#Buoyancy Force
def calc_buoyancy():
    rho = SALT_WATER_DENSITY
    g = GRAVITY
    F_b = rho * g * UUV.get_Total_Volume()
    return round(F_b,3)

#Drag Force

#Maybe h calculation?

def main():
    for i in range (10):
        h = i+1
        print("Underwater Pressure at " + str(h) +" meter is: " + str(round(calc_pressure(h),3)) + " KPa")
    print("Buoyancy Force is: " + str(calc_buoyancy()) + " Newtons.")
    print("Volume is " + str(round(UUV.get_Total_Volume(), 3)) + " m^3")
    print("Completed")

main()
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
def calc_drag_lateral():
    rho = SALT_WATER_DENSITY
    v = 2.5 # Max Cruising Speed (m/s)
    C_d = 0.00562 #From Solidworks Simulation
    A = 3.14 * np.power(UUV.diameter/2, 2) # m^2
    F_d = 0.5 * rho * np.power(v, 2) * C_d * A
    return round(F_d,3)
def calc_drag_vertical():
    rho = SALT_WATER_DENSITY
    v = 0.4 # Ascent/Descent rate from requirements
    C_d = 0.579 #From Solidworks simulation
    A = 0.219 #Calculated Using Solidworks... can derive though
    F_d = 0.5 * rho * np.power(v, 2) * C_d * A
    return round(F_d, 3)
#Weight and Ballast Volume
def calc_sub_weight():
    Weight = calc_buoyancy() - calc_drag_vertical()
    return round(Weight, 3) # in Newtons
def calc_ballast_volume():
    rho = SALT_WATER_DENSITY
    g = GRAVITY
    W_sub = calc_sub_weight()
    F_b = calc_buoyancy()
    F_d = calc_drag_vertical()
    ballastVolume = (F_d + F_b - W_sub)/(0.5*rho*g)
    return round(ballastVolume, 3)
#Required Thrust
def calc_required_thrust():
    F_t = calc_drag_lateral()
    return round(F_t, 3)
def main():
    for i in range (10):
        h = i+1
        print("Underwater Pressure at " + str(h) +" meter is: " + str(round(calc_pressure(h),3)) + " KPa")
    print("Buoyancy Force is: " + str(calc_buoyancy()) + " Newtons.")
    print("Volume is " + str(round(UUV.get_Total_Volume(), 3)) + " m^3")
    print("Lateral drag force is " + str(calc_drag_lateral()) + " N")
    print("Vertical drag force is " + str(calc_drag_vertical()) + " N")
    print("The weight of the submersible needs to be " + str(calc_sub_weight()) + " N in order to ascend at 0.4 m/s")
    print("The ballast volume needs to be " + str(calc_ballast_volume()) + " m^3 in order to descend at 0.4 m/s")
    print("The thrust required to cruise at 2.5 m/s is: " + str(calc_required_thrust())+ " N")
    print("Completed")

main()
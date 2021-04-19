class Unit:
    #Add (Default is Mechanics)
    #Temperature (K,C,F, R), ammounts (mole)
    #Electricty Ampere (A) -> Potential (eV, Voltage),  magnetism (henry, flux, etc.)
    def __init__(self, L, M, T, conv):
        # self.name = name
        self.L = L
        self.M = M
        self.T = T
        self.conv = conv

    def __mul__(self, Unit2):
        self.L = self.L + Unit2.L
        self.M = self.M + Unit2.M
        self.T = self.T + Unit2.T
        self.conv = self.conv * Unit2.conv

    def __truediv__(self, Unit2):
        self.L = self.L - Unit2.L
        self.M = self.M - Unit2.M
        self.T = self.T - Unit2.T
        self.conv = self.conv / Unit2.conv

    def type(self):
        if(self.L == 0 and self.M ==0 and self.T ==0):
            return f'{self.conv:.3e}'
        if (self.L == 1 and self.M == 0 and self.T == 0):
            return 'Length : L = 1, M = 0, T = 0'
        if (self.L == 2 and self.M == 0 and self.T == 0):
            return 'Area : L = 2, M = 0, T = 0'
        if(self.L == 0 and self.M == 0 and self.T == 1):
            return 'Time: L = 0, M = 0, T = 1'
        if(self.L ==0 and self.M ==1 and self.T == 0):
            return 'Mass: L = 0, M = 1, T = 0'
        if(self.L ==3 and self.M == 0 and self.T == 0):
            return 'Volume: L = 3, M = 0, T = 0'
        if(self.L ==3 and self.M == 0 and self.T == -1):
            return 'Volume Flow Rate: L = 3, M = 0, T = -1'
        if(self.L ==0 and self.M == 1 and self.T == -1):
            return 'Mass Flow Rate: L = 0, M = 1, T = -1'
        if(self.L ==-3 and self.M == 1 and self.T == 0):
            return 'Density: L = -3, M = 1, T = 0'
        if(self.L ==1 and self.M == 0 and self.T == -2):
            return 'Acceleration: L =1, M = 0, T = -2'
        if(self.L ==1 and self.M == 1 and self.T == -2):
            return 'Force: L =1, M = 1, T = -2'
        if(self.L ==-1 and self.M == 1 and self.T == -2):
            return 'Pressure: L =-1, M = 1, T = -2'
        if(self.L ==1 and self.M == 1 and self.T == -1):
            return 'Impulse | Momentum : L =1, M = 1, T = -1'
        if(self.L ==2 and self.M == 1 and self.T == -2):
            return 'Energy | Torque: L =2, M = 1, T = -2'
        if(self.L ==2 and self.M == 1 and self.T == -3):
            return 'Power: L = 2, M = 1, T = -3'
        else:
            return f'Not Found : L = {self.L}, M = {self.M}, T = {self.T}'


    def compare(conv, Unit1, Unit2):
        if (Unit1.L == Unit2.L and Unit1.M == Unit2.M and Unit1.T == Unit2.T):
            return conv * Unit1.conv / Unit2.conv
        else:
            return f'Error : Missing, Left Side Missing Units L:{Unit2.L-Unit1.L}, M:{Unit2.M-Unit1.M}, and T:{Unit2.T-Unit1.T}'

    def compute(numerators, operators, units, Unit2):
        new_unit = units[0]
        conv = numerators[0]
        for i in range(len(operators)):
            if (operators[i] == '*'):
                new_unit * units[i + 1]
                conv *= numerators[i + 1]
            if (operators[i] == '/'):
                new_unit / units[i + 1]
                conv /= numerators[i + 1]
            #conv *= numerators[i+1]
        return Unit.compare(conv, new_unit, Unit2)
    def computeType(operators, units):
        new_unit = units[0]
        for i in range(len(operators)):
            if (operators[i] == '*'):
                new_unit * units[i+1]
            if (operators[i] == '/'):
                new_unit / units[i+1]
        return new_unit.type()

Base_Units = {
    "meter": Unit(1, 0, 0, 1),
    "meters": Unit(1, 0, 0, 1),
    "feet": Unit(1, 0, 0, .3048),
    "ft" : Unit(1, 0, 0, .3048),
    "kilometers": Unit(1, 0, 0, 1000),
    "km": Unit(1, 0, 0, 1000),
    "inches": Unit(1, 0, 0, .3048 / 12),
    "in" : Unit(1,0,0,.3048/12),
    'in2' : Unit(2,0,0,.3048*.3048/12/12),
    "yard": Unit(1, 0, 0, .3048 / 12),
    "au": Unit(1, 0, 0, 1.49597871e11),
    "mile": Unit(1, 0, 0, 5280 * .3048),
    "nautical-mile": Unit(1, 0, 0, 1852),
    "nmile": Unit(1, 0, 0, 1852),
    "light-year": Unit(1, 0, 0, 9.4607e15),
    "ly": Unit(1, 0, 0, 9.4607e15),
    "square-feet": Unit(2, 0, 0, .3048 * .3048),
    "ft2":Unit(2,0,0,.3048*.3048),
    "square-meters": Unit(2, 0, 0, 1),
    "m2": Unit(2, 0, 0, 1),
    "Newtons": Unit(1,1,-2,1),
    "lbf" : Unit(1,1,-2,4.44822),
    "Joules" : Unit(2,1,-2,1),
    "kJ" : Unit(2,1,-2,1000),
    "Watts" : Unit(2,1,-3,1),
    "Watt-Hour" : Unit(2,1,-2,3600),
    "kW" : Unit(2,1,-3,1000),
    "hp" : Unit(2,1,-3,745.7),
    "btu" : Unit(2,1,-2,1055.06),
    "liters":Unit(3,0,0,.001),
    "cups" : Unit(3,0,0,.00023659),
    "teaspoons" : Unit(3,0,0,.00023659/48),
    "tablespoons" : Unit(3,0,0,.00023659/16),
    "quarts" : Unit(3,0,0,.000946353),
    "gallons" : Unit(3,0,0,.00378541),
    "kilograms" : Unit(0,1,0,1),
    "kg" : Unit(0,1,0,1),
    "slugs" : Unit(0,1,0,14.5939),
    "lbm" : Unit(0,1,0,.453592),
    "seconds": Unit(0,0,1,1),
    "sec" : Unit(0,0,1,1),
    "min" : Unit(0,0,1,60),
    "hour" : Unit(0,0,1,3600),
    "day" : Unit(0,0,1,86400),
    "Gravity" : Unit(1,0,-2,9.82),
    "kgperm3" : Unit(-3,1,0,1),
    "kPa" : Unit(-1, 1, -2, 100000),
    "Pa" : Unit(-1,1,-2,1),
    "atm" : Unit(-1,1,-2,101325),
    "psi" : Unit(-1,1,-2,6894.76)
}

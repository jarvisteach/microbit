#L9110 H-bridge controller Board

AIA = pin8  # A forward
AIB = pin12 # A reverse
BIA = pin0  # B forward
BIB = pin16 # B reverse

# VCC ---> AA Battery Pack +
# GND Ground ---> AA Battery Pack & Micro:Bit

def forward():
    AIA.write_digital(1)
    AIB.write_digital(0)
    BIA.write_digital(1)
    BIB.write_digital(0)
    
def stop():
    AIA.write_digital(1)
    AIB.write_digital(1)
    BIB.write_digital(1)
    BIA.write_digital(1)

def backward():
    AIA.write_digital(0)
    AIB.write_digital(1)
    BIA.write_digital(0)
    BIB.write_digital(1)

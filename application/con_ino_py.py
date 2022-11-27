# import serial

# port = "COM12"
# baudeRate = 9600
# arduino = serial.Serial(port,baudeRate)
# qtLiters = 0

def inoConnect():
    while True:
        # line = str(arduino.readline())
        # line = float(line[2:-5])
        qtLiters = 1
        line = 0
        price=0

        qtLiters = qtLiters+(line/1000)
        mCubic = qtLiters/1000
        price= mCubic*19.74

        return f'''
        Consumo em litros: {qtLiters:.2f}L
        Custo da hospedagem: R${price:.2f}
        '''
        
        
    arduino.close()
#! /usr/bin/env python

import time
from pymodbus.client.sync import ModbusTcpClient

registerMapping = {
    "outdoor_temp":       [20282, 0.1],
    "indoor_temp":        [20286, 0.1],
    "indoor_temp_wanted": [20260, 0.1],
    "bypass_state":       [21773, 1],
    "water_temp_bottom":  [20522, 0.11],
    "water_temp_wanted":  [20460, 0.11],
    "humidity_average":   [20164, 1],
}

client = ModbusTcpClient('10.10.10.90', port=502)


def readRegister(register, slaveID, unitConversionFactor):
    try:
        response = client.read_holding_registers(register, 1, unit=slaveID)
        calcUnit = round(response.registers[0] * unitConversionFactor, 2)
        return calcUnit
    except:
        print("Error reading register: " + register)


def getValues():

    for key in registerMapping:
        client.connect()
        print(
            key + " " + str(readRegister(registerMapping[key][0], 1, registerMapping[key][1])))
        client.close()


def loop():
    while True:
        getValues()
        time.sleep(5)


if __name__ == "__main__":
    getValues()

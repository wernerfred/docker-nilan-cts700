#! /usr/bin/env python

import os
from pymodbus.client.sync import ModbusTcpClient

host = os.environ.get('CTS700_HOST', 'localhost')
port = int(os.environ.get('CTS700_PORT', '502'))

registerMapping = {
    "outdoor_temp":       [20282, 0.1],
    "indoor_temp":        [20286, 0.1],
    "indoor_temp_wanted": [20260, 0.1],
    "bypass_state":       [21773, 1],
    "water_temp_bottom":  [20522, 0.11],
    "water_temp_wanted":  [20460, 0.11],
    "humidity_average":   [20164, 1],
}

client = ModbusTcpClient(host, port=port)


def readRegister(register, slaveID, unitConversionFactor):
    try:
        response = client.read_holding_registers(register, 1, unit=slaveID)
        calcUnit = round(response.registers[0] * unitConversionFactor, 2)
        return calcUnit
    except:
        print("Error reading register: " + register)
        raise


def getValues():
    result = {}
    for key in registerMapping:
        client.connect()
        response = readRegister(registerMapping[key][0], 1, registerMapping[key][1])
        result[key] = response
        client.close()
    return result


if __name__ == "__main__":
    getValues()

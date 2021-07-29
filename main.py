#! /usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient


def readRegister(register, slaveID):
    try:
        result = client.read_holding_registers(register, 1, unit=slaveID)
        print(result.registers)
    except:
        print("Error reading register")


client = ModbusTcpClient('10.10.10.90', port=502)
client.connect()

readRegister(20282, 1)  # T1 outdoor air temperature (C)
readRegister(20286, 1)  # T3 extract air, room temperature (C)

client.close()

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

print("Outdoor temp:")
readRegister(20282, 1)  # T1 outdoor air temperature (C)
print("Room temp:")
readRegister(20286, 1)  # T3 extract air, room temperature (C)
print("Room temp wanted:")
readRegister(20260, 1)  # Wanted room temperature (C)
print("Bypass:")
readRegister(21773, 1)  # Bypass damper
print("Water temp:")
readRegister(20522, 1)  # T12 bottom temperature in DHW water tank(C)
print("Water temp wanted:")
readRegister(20460, 1)  # Hot water set point (C)
print("Humidity:")
readRegister(20164, 1)  # Average Humidity (%)
client.close()

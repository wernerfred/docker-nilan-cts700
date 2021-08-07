#! /usr/bin/env python

import os
import time
from prometheus_client import Gauge, start_http_server
from cts700_modbus import getValues


port = int(os.environ.get('PROM_EXPORTER_PORT', 8080))
checkInterval = int(os.environ.get('PROM_EXPORTER_CHECK_INTERVAL', 60))

gOutdoorTemp = Gauge('nilan_cts700_outdoor_temp', 'Outdoor temperature', ['scale'])
gIndoorTemp = Gauge('nilan_cts700_indoor_temp', 'Indoor temperature', ['scale'])
gIndoorTempWanted = Gauge('nilan_cts700_indoor_temp_wanted', 'Indoor temperature wanted', ['scale'])
gBypassState = Gauge('nilan_cts700_bypass_state', 'Bypass state')
gWaterTempBottom = Gauge('nilan_cts700_water_temp_bottom', 'Water temperature bottom', ['scale'])
gWaterTempWanted = Gauge('nilan_cts700_water_temp_wanted', 'Water temperature wanted', ['scale'])
gHumidityAverage = Gauge('nilan_cts700_humidity_average', 'Humidity average')


gIndoorTemp.labels('°C')
gOutdoorTemp.labels('°C')
gIndoorTempWanted.labels('°C')
gWaterTempBottom.labels('°C')
gWaterTempWanted.labels('°C')


def setMetrics():
    try:
        values = getValues()
        gOutdoorTemp.labels('°C').set(values['outdoor_temp'])
        gIndoorTemp.labels('°C').set(values['indoor_temp'])
        gIndoorTempWanted.labels('°C').set(values['indoor_temp_wanted'])
        gBypassState.set(values['bypass_state'])
        gWaterTempBottom.labels('°C').set(values['water_temp_bottom'])
        gWaterTempWanted.labels('°C').set(values['water_temp_wanted'])
        gHumidityAverage.set(values['humidity_average'])
    except:
        print("Unexpected error")
        raise


def loop():
    while True:
        setMetrics()
        time.sleep(checkInterval)


if __name__ == "__main__":
    start_http_server(port)
    print("Serving sensor metrics on http://localhost:{}".format(port))
    loop()

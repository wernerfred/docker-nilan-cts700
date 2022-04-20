![GitHub Workflow Status](https://img.shields.io/github/workflow/status/wernerfred/docker-nilan-cts700/Build%20current%20version%20+%20push%20to%20DockerHub?label=Docker%20Build)
![Docker Pulls](https://img.shields.io/docker/pulls/wernerfred/docker-nilan-cts700?label=Docker%20Pulls)
![GitHub](https://img.shields.io/github/license/wernerfred/docker-nilan-cts700?label=License)
![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/wernerfred/docker-nilan-cts700?label=Image%20Size)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/wernerfred/docker-nilan-cts700?label=Latest%20Release)
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/wernerfred/docker-nilan-cts700?label=Latest%20Image)
![GitHub Release Date](https://img.shields.io/github/release-date/wernerfred/docker-nilan-cts700?label=Release%20Date)

# docker-nilan-cts700

This project uses `pymodbus` to read the Modbus RTU data from a [nilan system with a CTS700 controller](https://www.nilan.at/de-at/startseite/losungen/wohnungslosungen/kompaktlosung/compact-p-cts700). The `prometheus_client` library is used to expose the data via a Prometheus server. All of this is packed in a [Docker](https://hub.docker.com/r/wernerfred/docker-nilan-cts700) container.

## Metrics

The following metrics are exposed:

| Metric | Register | Description | Unit | Prometheus Type |
|--------|:--------:|-------------|:----:|:---------------:|
| `nilan_cts700_outdoor_temp` | `20282` | T1 outdoor air temperature | Celsius | `Gauge` |
| `nilan_cts700_indoor_temp` | `20286` | T3 extract air, room temperature | Celsius | `Gauge` |
| `nilan_cts700_indoor_temp_wanted `| `20260` | Wanted room temperature | Celsius | `Gauge` |
| `nilan_cts700_bypass_state` | `21773` | Bypass damper | | `Gauge` |
| `nilan_cts700_water_temp_bottom` | `20522` | T12 bottom temperature in DHW water tank | Celsius | `Gauge` |
| `nilan_cts700_water_temp_top` | `20520` | T11 top temperature in DHW water tank | Celsius | `Gauge` |
| `nilan_cts700_water_temp_wanted` | `20460` | Hot water set point | Celsius | `Gauge` |
| `nilan_cts700_humidity_average` | `20164` | Average Humidity | Percent | `Gauge` |

## Installation

### Build from source

To build this project from source make sure to clone this repository from github and run the following command:

```
docker build -t wernerfred/docker-nilan-cts700 .
```

### Pull from Docker Hub

You can directly pull the latest release from the [Docker Hub repository](https://hub.docker.com/r/wernerfred/docker-nilan-cts700/):

```
docker pull wernerfred/docker-nilan-cts700
```

## Usage

To run the container you can use `docker run`. You might adjust the following command according to your needs:

```
docker run -d \
           -p 8080:8080 \
           wernerfred/docker-nilan-cts700
```

### Configuration

The following environment variables can be used to configure the container:

| Variable | Default | Description |
|----------|---------|-------------|
| `CTS700_HOST` | `192.168.5.107` | The IP address of the nilan CTS700 controller |
| `CTS700_PORT` | `502` | The Modbus RTU port of the nilan CTS700 controller |
| `PROM_EXPORTER_PORT` | `8080` | The port on which the Prometheus server listens |
| `PROM_EXPORTER_CHECK_INTERVAL` | `60` | The interval at which the Prometheus server checks for new data in seconds |	

Simply add the  environment variables you want to change to your `docker run` command:

```
docker run -d \
           -p 8080:8080 \
           -e CTS700_HOST=192.168.5.107 \
           -e CTS700_PORT=502 \
           -e PROM_EXPORTER_PORT=8080 \
           -e PROM_EXPORTER_CHECK_INTERVAL=60 \
           wernerfred/docker-nilan-cts700
```

### Prometheus

The metrics are exposed via a Prometheus server. To access the metrics you can use the following URL:

`http://<docker-host>:<prom-exporter-port>/metrics`

To add this URL to your Prometheus configuration you can use the following snippet:

```
static_configs: [
  {"labels": {"job": "nilan_cts700"}, "targets": ["<docker-host>:<prom-exporter-port>"]}
]
```
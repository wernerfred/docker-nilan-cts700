![GitHub Workflow Status](https://img.shields.io/github/workflow/status/wernerfred/docker-nilan-cts700/Build%20current%20version%20+%20push%20to%20DockerHub?label=Docker%20Build)
![Docker Pulls](https://img.shields.io/docker/pulls/wernerfred/docker-nilan-cts700?label=Docker%20Pulls)
![GitHub](https://img.shields.io/github/license/wernerfred/docker-nilan-cts700?label=License)
![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/wernerfred/docker-nilan-cts700?label=Image%20Size)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/wernerfred/docker-nilan-cts700?label=Latest%20Release)
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/wernerfred/docker-nilan-cts700?label=Latest%20Image)
![GitHub Release Date](https://img.shields.io/github/release-date/wernerfred/docker-nilan-cts700?label=Release%20Date)

# docker-nilan-cts700

This project uses `pymodbus` to read the Modbus RTU data from a [nilan system with a CTS700 controller](https://www.nilan.at/de-at/startseite/losungen/wohnungslosungen/kompaktlosung/compact-p-cts700). The `prometheus_client` library is used to expose the data via a Prometheus server. All of this is packed in a [Docker](https://hub.docker.com/r/wernerfred/docker-nilan-cts700) container.

## Installation

### Build from source

To build this project from source make sure to clone this repository from github and run the following commands:

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

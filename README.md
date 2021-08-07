![GitHub Workflow Status](https://img.shields.io/github/workflow/status/wernerfred/docker-nilan-cts700/Build%20+%20push%20to%20DockerHub?label=Docker%20Build)
![Docker Pulls](https://img.shields.io/docker/pulls/wernerfred/docker-nilan-cts700?label=Docker%20Pulls)
![GitHub](https://img.shields.io/github/license/wernerfred/docker-nilan-cts700?label=License)
![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/wernerfred/docker-nilan-cts700?label=Image%20Size)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/wernerfred/docker-nilan-cts700?label=Latest%20Release)
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/wernerfred/docker-nilan-cts700?label=Latest%20Image)
![GitHub Release Date](https://img.shields.io/github/release-date/wernerfred/docker-nilan-cts700?label=Release%20Date)

# docker-nilan-cts700

This project uses `pymodbus` to read the Modbus RTU data from a nilan CTS700 controller. The `prometheus_client` library is used to expose the data via a Prometheus server.

## ENV

CTS700_HOST (localhost)
CTS700_PORT (502)
PROM_EXP_PORT (8080)
PROM_EXP_CHECK_INTERVAL (60)
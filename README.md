# RevitSense: Real-Time IoT Data Visualization

This project integrates sensors connected to an ESP32 with a data management platform for real-time visualization. Inspired and adapted from [João Martins' tutorial](https://joaomartins-callmejohn.github.io/iot-sample-tutorial/), the application displays an interactive heatmap over a house floorplan (developed in Revit), with sensor data updating the visualization in real time.

> **Note:** By default, the repository uses the Revit floorplan **racbasicsampleproject.rvt**, an Autodesk sample available [here](https://help.autodesk.com/view/RVT/2024/ENU/?guid=GUID-61EF2F22-3A1F-4317-B925-1E85F138BE88).


## Introduction

<div align="center">
  <img src="aps.gif" alt="APS GIF">
</div>

This project provides a complete solution that:

- Uses 4 sensors connected to an ESP32.
- Integrates sensor data into an application that renders a dynamic heatmap on a Revit floorplan.
- Displays real-time sensor data and allows historical data visualization based on a selected time period.
- Automates the integration with Autodesk Platform Services—from converting the Revit model to the required format, uploading it to Autodesk’s cloud, extracting necessary data for the integration, to creating the application and database containers.

## Features

- Dynamic Visualization
- Historical Data Query
- Autodesk Platform Services Integration
- Node.js API

## Prerequisites

- Autodesk Platform Services account
- Docker ([Install Docker](https://docs.docker.com/get-docker/))
- Git
- Python 3

## Deployment

1. Create an APS account and application to get your CLIENT_ID and CLIENT_SECRET.

2. Download the application:

```bash
git clone https://github.com/Aldrumont/revitsense
cd revitsense
sudo apt install -y unzip
unzip aps-iot-extensions-demo.zip
cd aps-iot-extensions-demo-master
```

3. Run the pre-configuration script:

```bash
python3 pre_config.py
```
Enter your CLIENT_ID and CLIENT_SECRET when prompted.

4. Start Docker containers:

```bash
docker compose up -d --build && sleep 10
```

5. Select the place of your sensor:

Follow [Joao Martins Example](https://joaomartins-callmejohn.github.io/iot-sample-tutorial/adapting/home/#ajustando-os-sensores)

6. Restart Docker containers:

```bash
docker compose down && docker compose up -d --build && sleep 10
```

7. Initialize the database:

```bash
docker exec aps-iot-extensions-demo-master-app-1 python3 init_sensor_db.py && sleep 5
```
To populate with example data:

```bash
docker exec aps-iot-extensions-demo-master-app-1 python3 post_example_data.py
```

## Automated Configuration

The `pre_config.py` script automates everything up to the sensor setup. You only need to input your APS credentials and the path to your .rvt Revit file. The script will:

- Convert and upload the model to Autodesk.
- Extract integration data.
- Set up containers.

## Endpoints and Integration

Node.js endpoints receive and provide data for visualization and interaction with the application.

## Data Generation Example

`gera_data.py` is a sample script that sends the following JSON to the API:

```json
{
  "temp": 21,
  "umidade": 498.7,
  "co": 100.0,
  "ruido": 10.0,
  "time": 1742656891
}
```

Adapt this format for real sensor data in production environments.

## Notes

- Based on the tutorial by João Martins with custom enhancements.
- Default Revit model: racbasicsampleproject.rvt

## Contact

Ferraz Junior – ferrazjunior97@gmail.com  
Project: https://github.com/Aldrumont/revitsense
# 🧱 Architecture
*Here you will found anything related to the current and past architectures*  

*Note: The choices are led by the first-simplicity-next-complexity philosophy. We use basic stuff at first, and then build something more complex, one thing at a time.*

## Major components
![Functionnal](/media/Architectures/Functionnal.png)

This project is composed of the following components:
* Factories that contains sensors
* A database
* A dashboarding application
* An Extract-Tansform-Load (ETL) tool

Awaited functionalities
1. Ability to watch the data in real time
2. Ability to store the data as archive after a period of time
3. Ability to alert one specific user as one data is out of the awaited range.

## The techs (V1)
For this project, we are using:
* A Rust application to simulate a sensor
* MariaDB to store the data from sensors
* Graphana to display the data
* Airflow to ETL and orchestrate pipelines

## Old versions
### V0
*Legacy architecture*
- Python to simulate the sensors
- Mongodb as database
- Graphana for data visualisation
- Prometheus for... I don't know
- Zookeeper for... I don't know
- Kafka as message broker

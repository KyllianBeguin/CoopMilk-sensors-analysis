# SYSTÈME BIG DATA - COPP'MILK  
![header](https://user-images.githubusercontent.com/50613619/167309970-bf82e8e7-52d6-4d0a-a218-3b6a927969b7.PNG)  
*By Data49 : Hortense C., Leo L., Rabah A., Marie-Pascale B., Kyllian B.*

Bienvenue sur le projet professionnel de l'équipe Data49 de l'école Sup de Vinci Rennes  
![Image1](https://user-images.githubusercontent.com/50613619/167310031-d208ef5f-474e-4dc0-bb5b-9eeb345aff5c.png)  
Ce répository a pour objectif de pouvoir déployer un système Big Data pour le compte de l'entreprise fictive COOP'MILK  
## Structure du repository
├── Datasets  
├── setup_vm  
│   ├── DockerCompose  
│   │   ├── docker_compose.yml  
│   │   ├── Mongo  
│   │   ├── grafana  
│   │   ├── prometheus  
│   ├── install_docker.sh  
│   ├── install_docker_compose.sh  
# PROCÉDURE DE DÉPLOIEMENT DU SYSTÈME  
## Déploiement des services
Après avoir démarrer votre machine virtuelle :  
1. update la vm : `sudo apt-get update`
2. installer git : `sudo apt-get install git`
3. [optionnel] Aller dans le dossier /home de votre machine virtuelle : `cd ..`  
4. cloner ce repository : `sudo git clone https://github.com/KyllianBeguin/b3_big-data_projet-pro.git`  
5. lancer le script d'installation de docker (pour Debian) : `bash b3_big-data_projet-pro/setup_vm/install_docker.sh`  
6. lancer le script d'installation de docker-compose (pour Debian) : `bash  b3_big-data_projet-pro/setup_vm/install_docker_compose.sh`  
7. aller dans le dossier du docker-compose.yml : `cd b3_big-data_projet-pro/setup_vm/DockerCompose`  
8. lancer le docker-compose.yml : `sudo docker-compose up -d`  
9. vérifier que les services sont tous présents : `sudo docker ps`  
## Configuration de la base de données mongodb  
Après avoir déployé les services :
1. aller dans le conteneur de mongodb : `sudo docker exec -it mongo bash`  
2. lancer le script de création de la base et d'insertion de données d'essai : `bash /setup/RUN_ME.sh`  
# ACCÉDER AUX SERVICES
| Service | Port |
| ----------- | ----------- |
| Mongo-Express | 8081 |
| Grafana | 3000 |
| Prometheus | 9090 |

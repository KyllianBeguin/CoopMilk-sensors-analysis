docker run -d \
    --name my-mongodb \
    -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=coop \
    -e MONGO_INITDB_ROOT_PASSWORD=milk \
    mongo:5.0
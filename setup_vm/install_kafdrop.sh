sudo docker run -d --rm -p 9000:9000 \
    -e KAFKA_BROKERCONNECT=host:port,host:port \
    -e JVM_OPTS="-Xms32M -Xmx64M" \
    -e SERVER_SERVLET_CONTEXTPATH="/" \
    obsidiandynamics/kafdrop:latest

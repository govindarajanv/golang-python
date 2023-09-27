# Localstack

```
python3 -m pip install awscli-local localstack
docker network create my-network
MAIN_DOCKER_NETWORK=my-network DOCKER_FLAGS="--network my-network" localstack start
s3api create-bucket --bucket my-bucket-name --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
aws --endpoint-url http://0.0.0.0:4566 s3api list-buckets   
```
"""
python -m pip install localstack
pip install aws
pip install awscli-local
#curl -Lo localstack-cli-2.2.0-linux-amd64-onefile.tar.gz \
    https://github.com/localstack/localstack-cli/releases/download/v2.2.0/localstack-cli-2.2.0-linux-amd64-onefile.tar.gz
#sudo tar xvzf localstack-cli-2.2.0-linux-*-onefile.tar.gz -C /usr/local/bin
awslocal kafka create-cluster \
    --cluster-name "EventsCluster" \
    --broker-node-group-info file://brokernodegroupinfo.json \
    --kafka-version "2.2.1" \
    --number-of-broker-nodes 3
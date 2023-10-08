## Admission controllers

```
openssl req -x509 -sha256 -newkey rsa:2048 -keyout webhook.key -out webhook.crt -days 1024 -nodes -addext "subjectAltName = DNS.1:validate.default.svc"               
cat webhook.crt | base64 | tr -d '\n'
cat webhook.key| base64 | tr -d '\n'
```

Add certificate in webhook yaml caBundle: and secret 

```
docker build -t govindarajanv/webhook:gunicorn -f Dockerfile .
docker push govindarajanv/webhook:gunicorn
```

change the image registry url and image name in manifests.yaml

```
kubectl apply -f manifests.yaml
kubectl apply -f label.yaml
kubectl logs validation-webhook-57cd5587f5-wzvbn
kubectl create deploy nginx_not_allowed --image=nginx
```
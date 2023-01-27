# DNS-Rebinding

Repository that hosts educational content on DNS Rebinding

## How to deploy

### Deploying client-side service

1. Build a container image

```
cd internal-service/
docker build -t dnsrbnd .
```

2. Run the dnsrbnd container
```
docker run -p 7777:7777 dnsrbnd
```


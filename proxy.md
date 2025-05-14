## skipper
most recent url: https://icy-breeze-pb82hbhf.fra0.kraft.host

curl to test chat:
```sh
curl -X POST \
  'https://icy-breeze-pb82hbhf.fra0.kraft.host/agent1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"input": "string"}'
```

does not support streaming - uses a buffer of 8kb and 
apparently cant modify that

## traefik
https://spring-sea-3lqlkvrt.fra0.kraft.host

```sh
curl -X POST \
  'https://spring-sea-3lqlkvrt.fra0.kraft.host/agent1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"input": "string"}'
```
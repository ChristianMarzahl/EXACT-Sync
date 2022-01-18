# REST-API Load Tests

We use [Locust](https://locust.io/) for load testing the api.

```bash
pip install locust
```

Please edit the [locustfile.py](locustfile.py) according to our test case and add authorization.

```bash
locust --web-port 8090 --locustfile locustfile.py
```
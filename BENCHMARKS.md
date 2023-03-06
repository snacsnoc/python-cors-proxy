# Benchmarks

This document has been created to outline the benchmarks of this project in comparison to other popular CORS proxy servers.

# cors-anywhere
https://github.com/Rob--W/cors-anywhere

### JMeter tests
1000 threads, 60 second ramp-up period
cors-anywhere: [![Screenshot-2023-01-17-at-21-13-39.png](https://i.postimg.cc/0yBHx9ss/Screenshot-2023-01-17-at-21-13-39.png)](https://postimg.cc/hXV01Wvy)


python-cors-proxy: [![Screenshot-2023-01-17-at-21-11-24.png](https://i.postimg.cc/1zzP7mK1/Screenshot-2023-01-17-at-21-11-24.png)](https://postimg.cc/9DsvrjSL)

### Chrome browser 
(Dev tools -> Network -> Timing)
Two subsequent requests to the CORS server requested by a webpage. (URL 1 loaded fully then URL 2)

cors-anywhere:
[![Screenshot-2023-01-16-at-23-47-55.png](https://i.postimg.cc/zv4V8L0h/Screenshot-2023-01-16-at-23-47-55.png)](https://postimg.cc/MfbWYGkZ)
[![Screenshot-2023-01-16-at-23-48-28.png](https://i.postimg.cc/PrZmNhYH/Screenshot-2023-01-16-at-23-48-28.png)](https://postimg.cc/xcfkFw6p)

python-cors-proxy: 
[![py1.png](https://i.postimg.cc/6QDW7sds/py1.png)](https://postimg.cc/bG9cMBCL)

[![py2.png](https://i.postimg.cc/1599VrNz/py2.png)](https://postimg.cc/DmMVts6V)

Result: 1.16 second vs 557ms

### Simple Postman request
cors-anywhere:
[![Screenshot-2023-03-05-at-20-43-50.png](https://i.postimg.cc/3RwYkKqx/Screenshot-2023-03-05-at-20-43-50.png)](https://postimg.cc/hJNHwqgk)

python-cors-proxy: 
[![Screenshot-2023-03-05-at-20-44-24.png](https://i.postimg.cc/GtW4P80Q/Screenshot-2023-03-05-at-20-44-24.png)](https://postimg.cc/T5c2fP3L)

Result: 84% decrease in response size

# upstream python-cors-proxy
https://github.com/fraigo/python-cors-proxy

This project is a modification of the upstream code with added features.

### Simple Postman request
Request to a URL using the CORS proxy


upstream python-cors-proxy:
[![Screenshot-2023-03-05-at-20-32-44.png](https://i.postimg.cc/Ss9mpZYy/Screenshot-2023-03-05-at-20-32-44.png)](https://postimg.cc/343sXFZ6)

This project:
[![Screenshot-2023-03-05-at-20-32-35.png](https://i.postimg.cc/7hgPSBqB/Screenshot-2023-03-05-at-20-32-35.png)](https://postimg.cc/vxZdstg9)

We can see the effect of adding gzip compression, the size of the response is 78% smaller
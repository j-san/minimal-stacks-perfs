
A simple performance test on various minimal setup

## Motivations:

Compare performance of minimal real live app server implemented on main popular languages.


## Method:

I prompted chat GPT with: `Can you give me a minimal production server in {stack} on a docker setup ?`

Then updated dependencies and made some fixes manually.


## Results:

```
### Running load test for node:

hey -n 100000 -c 100 http://localhost:3001
Total time: 7.9152
Avg response time: 0.0078

----------


### Running load test for go:

hey -n 100000 -c 100 http://localhost:3002
Total time: 3.8102
Avg response time: 0.0038

----------


### Running load test for rust:

hey -n 100000 -c 100 http://localhost:3003
Total time: 4.0084
Avg response time: 0.0040

----------


### Running load test for java:

hey -n 100000 -c 100 http://localhost:3004
Total time: 4.9757
Avg response time: 0.0049

----------


### Running load test for python:

hey -n 100000 -c 100 http://localhost:3005
Total time: 4.7259
Avg response time: 0.0047

----------
```

Run the test:
```
# install hey command
docker compose up -d
python tests.py
```

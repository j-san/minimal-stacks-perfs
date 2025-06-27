
A simple performance test on various minimal setup

## Motivations:

Compare performance of minimal real live app server implemented on main popular languages.


## Method:

I prompted chat GPT with: `Can you give me a minimal production server in {stack} on a docker setup ?`

Then updated dependencies and made some fixes manually.


## Results:

```
### Running load test for node:

hey -n 1000000 -c 100 http://localhost:3001
Total time: 77.241
Avg response time: 0.0077

----------


### Running load test for go:

hey -n 1000000 -c 100 http://localhost:3002
Total time: 36.1215
Avg response time: 0.0036

----------


### Running load test for rust:

hey -n 1000000 -c 100 http://localhost:3003
Total time: 35.5431
Avg response time: 0.0036

----------


### Running load test for java:

hey -n 1000000 -c 100 http://localhost:3004
Total time: 43.2438
Avg response time: 0.0043

----------


### Running load test for python:

hey -n 1000000 -c 100 http://localhost:3005
Total time: 41.8454
Avg response time: 0.0041


------------------------------------------------------------------------------------------------------------------------
rust      35.5431   ##############################################
go        36.1215   ##############################################
python    41.8454   ######################################################
java      43.2438   #######################################################
node      77.241    ####################################################################################################
------------------------------------------------------------------------------------------------------------------------
```

Run the test:
```
# install hey command
docker compose up -d
python tests.py
```

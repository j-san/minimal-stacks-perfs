
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
Total time: 42.5112
Avg response time: 0.0042

----------


### Running load test for go:

hey -n 1000000 -c 100 http://localhost:3002
Total time: 35.5503
Avg response time: 0.0035

----------


### Running load test for rust:

hey -n 1000000 -c 100 http://localhost:3003
Total time: 34.1833
Avg response time: 0.0034

----------


### Running load test for java:

hey -n 1000000 -c 100 http://localhost:3004
Total time: 44.921
Avg response time: 0.0045

----------


### Running load test for python:

hey -n 1000000 -c 100 http://localhost:3005
Total time: 49.0537
Avg response time: 0.0049


------------------------------------------------------------------------------------------------------------------------
rust      34.1833   #####################################################################
go        35.5503   ########################################################################
node      42.5112   ######################################################################################
java      44.921    ###########################################################################################
python    49.0537   ####################################################################################################
------------------------------------------------------------------------------------------------------------------------
```

Run the test:
```
# install hey command
docker compose up -d
python tests.py
```

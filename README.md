
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
Total time: 47.4752
Avg response time: 0.0047

----------


### Running load test for go:

hey -n 1000000 -c 100 http://localhost:3002
Total time: 33.3294
Avg response time: 0.0033

----------


### Running load test for rust:

hey -n 1000000 -c 100 http://localhost:3003
Total time: 31.7865
Avg response time: 0.0032

----------


### Running load test for java spr:

hey -n 1000000 -c 100 http://localhost:3004
Total time: 47.2255
Avg response time: 0.0047

----------


### Running load test for python:

hey -n 1000000 -c 100 http://localhost:3005
Total time: 40.5935
Avg response time: 0.004

----------


### Running load test for java vrtx:

hey -n 1000000 -c 100 http://localhost:3006
Total time: 37.1526
Avg response time: 0.0037


------------------------------------------------------------------------------------------------------------------------
rust      31.7865   ##################################################################
go        33.3294   ######################################################################
java vrtx 37.1526   ##############################################################################
python    40.5935   #####################################################################################
java spr  47.2255   ###################################################################################################
node      47.4752   ####################################################################################################
------------------------------------------------------------------------------------------------------------------------
```

Run the test:
```
# install hey command
docker compose up -d
python tests.py
```

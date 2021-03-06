# WAC Locust Tests

This repo has the details for setting up locust tests for WAC

### Server Details

`Master` - 157.245.138.188
`Slave1` - 134.122.21.50
`Slave2` - 178.128.149.168
`Slave3` - 167.172.135.158

### Test Files Details

Following are the test files to test each module of the application independently, use them one by one on locust to do a stress test against each module.

1. `Tracks` - tracks_stress_test.py
2. `Personal Interview`: personal_interview_stress_test.py
3. `DAT` - dat_stress_test.py
4. `GPT` - gpt_stress_test.py

### Steps For Runnning Tests

After making any change to the tests, login to the servers & kill the existing locust process and do the following:

1.  Start test on master

		cd load-testing
		source venv/bin/activate
        git pull
		nohup locust -f <test_file.py> --master &

2. Start test on slaves

		cd load-testing
		source venv/bin/activate
        git pull
		nohup locust -f <test-file.py> --slave --master-host=157.245.138.188 &
		
3. Run the test through UI - http://157.245.138.188:8089/
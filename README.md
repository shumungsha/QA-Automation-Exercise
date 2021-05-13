# QA-Automation-Exercise

**Task 1:**
Please make a test script to test the API listed below from HKO Open Data API Document
Weather Information API

API: https://data.weather.gov.hk/weatherAPI/opendata/weather.php

Test Cases:
https://docs.google.com/spreadsheets/d/1F9QrQgcma4m0xchFtsRUz-WHeRU69aid7trkvXZlHF4/edit?usp=sharing

The Python file Task1.py uploaded try to run the test cases automatically.


**Task 2:**
Given a binary file (no source code given). The binary is used to do health check on
FIXED HTTP endpoint (www.google.com).

If the response status code is 200, “It works!!!” will be displayed in the console. 
If the response status code is not 200, the response status code will be displayed in the console.

Test Cases: https://docs.google.com/spreadsheets/d/1F9QrQgcma4m0xchFtsRUz-WHeRU69aid7trkvXZlHF4/edit?pli=1#gid=566928799

Simulate different response status code of the fixed http endpoint:
1) Mocky.io https://designer.mocky.io/
  Firstly use Mocky.io to create mock API HTTP response which list in the test cases. 
  e.g. 400 / 404 / 500
2) Requestly.io https://requestly.io/
  Then, use Requestly.io to redirect the original request to URL of the mock request created in Mocky.io in step 1.

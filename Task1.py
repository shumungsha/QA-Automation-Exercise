import requests
from textblob import TextBlob
import datetime
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

#Test if API return with status 200 correctly
response=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en")
code=response.status_code
if code == 200:
    print("API status code returned correctly")
else:
    print("API failed")

#Test Case 1: check if lang is correct: en
tc1=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en")
json_responsetc1 = tc1.json()
text_tc1 = ""
for x in range (18):
    text_tc1 = text_tc1 + " " + json_responsetc1["rainfall"]["data"][x]["place"]
for y in range (26):
    text_tc1 = text_tc1 + " " + json_responsetc1["temperature"]["data"][y]["place"]
#print (text_tc1)
blob_tc1 = TextBlob(text_tc1)
#print(blob_tc1.detect_language())
if blob_tc1.detect_language() == "en":
    print("Test Case 1: rhrread data is returned with language as English correctly for dataType=rhrread&lang=en")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 1: Language is not returned correctly for lang=en"))


#Test Case 2: check if lang is correct: tc
tc2=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc")
json_responsetc2 = tc2.json()
text_tc2 = ""
for x in range (18):
    text_tc2 = text_tc2 + " " + json_responsetc2["rainfall"]["data"][x]["place"]
for y in range (26):
    text_tc2 = text_tc2 + " " + json_responsetc2["temperature"]["data"][y]["place"]
#print(text_tc2)
blob_tc2 = TextBlob(text_tc2)
#print(blob_tc2.detect_language())
#assert blob_tc2.detect_language() == "zh-TW" , "Language is not correct for lang=tc"
if blob_tc2.detect_language() == "zh-TW":
    print("Test Case 2: rhrread data is returned with language as Traditional Chinese correctly for dataType=rhrread&lang=tc")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 2: Language is not returned correctly for lang=tc"))

#Test Case 3: check if lang is correct: sc
tc3=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=sc")
json_responsetc3 = tc3.json()
text_tc3 = ""
for x in range (18):
    text_tc3 = text_tc3 + " " + json_responsetc3["rainfall"]["data"][x]["place"]
for y in range (26):
    text_tc3 = text_tc3 + " " + json_responsetc3["temperature"]["data"][y]["place"]
#print(text_tc3)
blob_tc3 = TextBlob(text_tc3)
#print(blob_tc3.detect_language())
#assert blob_tc3.detect_language() == "zh-CN" , "Language is not correct for lang=sc"
if blob_tc3.detect_language() == "zh-CN":
    print("Test Case 3: rhrread data is returned with language as Simplified Chinese correctly for dataType=rhrread&lang=sc")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 3: Language is not returned correctly for lang=sc"))

#Test Case 4: check if lang is correct for default lang
tc4=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread")
json_responsetc4 = tc4.json()
text_tc4 = ""
for x in range (18):
    text_tc4 = text_tc4 + " " + json_responsetc4["rainfall"]["data"][x]["place"]
for y in range (26):
    text_tc4 = text_tc4 + " " + json_responsetc4["temperature"]["data"][y]["place"]
#print (text_tc4)
blob_tc4 = TextBlob(text_tc4)
#print(blob_tc4.detect_language())
#assert blob_tc4.detect_language() == "en" , "Language is not correct for lang=en"
if blob_tc4.detect_language() == "en":
    print("Test Case 4: rhrread data is returned with default language as English correctly for dataType=rhrread")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 4: Language is not returned correctly for default language"))


#Test Case 5: check if lang is correct for default lang
tc5=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=")
json_responsetc5 = tc5.json()
text_tc5 = ""
for x in range (18):
    text_tc5 = text_tc5 + " " + json_responsetc5["rainfall"]["data"][x]["place"]
for y in range (26):
    text_tc5 = text_tc5 + " " + json_responsetc5["temperature"]["data"][y]["place"]
#print (text_tc5)
blob_tc5 = TextBlob(text_tc5)
#print(blob_tc5.detect_language())
#assert blob_tc5.detect_language() == "en" , "Language is not correct for lang=en"
if blob_tc5.detect_language() == "en":
    print("Test Case 5: rhrread data is returned with default language as English correctly for dataType=rhrread&lang=")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 5: Language is not returned correctly for default language"))

#Test Case 6: check if error message is return successfully for lang=xx
tc6=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=xx")
#print (tc6.text)
#assert ((tc6.text).startswith("Please include valid parameters in API request.")) , "Error message cannot show correctly for lang=xx"
if (tc6.text).startswith("Please include valid parameters in API request."):
    print("Test Case 6: Error message show correctly for dataType=rhrread&lang=xx")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 6: Error message cannot show correctly for dataType=rhrread&lang=xx"))

#Test Case 7: check if error message is return successfully for dataType=rhrreax
tc7=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrreax&lang=en")
#print (tc7.text)
#assert ((tc7.text).startswith("Please include valid parameters in API request.")) , "Error message cannot show correctly for dataType=rhrreax"
if (tc7.text).startswith("Please include valid parameters in API request."):
    print("Test Case 7: Error message show correctly for dataType=rhrreax&lang=en")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 7: Error message cannot show correctly for dataType=rhrreax&lang=en"))

#Test Case 8: check if error message is return successfully for dataType=rhrreadx
tc8=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrreadx&lang=tc")
#print (tc8.text)
#assert ((tc8.text).startswith("Please include valid parameters in API request.")) , "Error message cannot show correctly for dataType=rhrreadx"
if (tc8.text).startswith("Please include valid parameters in API request."):
    print("Test Case 8: Error message show correctly for dataType=rhrreadx&lang=tc")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 8: Error message cannot show correctly for dataType=rhrreadx&lang=tc"))

#Test Case 9: check if error message is return successfully for dataType=errortesting
tc9=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=errortesting&lang=sc")
#print (tc9.text)
#assert ((tc9.text).startswith("Please include valid parameters in API request.")) , "Error message cannot show correctly for dataType=errortesting"
if (tc9.text).startswith("Please include valid parameters in API request."):
    print("Test Case 9: Error message show correctly for dataType=errortesting&lang=sc")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 9: Error message cannot show correctly for dataType=errortesting&lang=sc"))

#Test Case 10: check if error message is return successfully for dataType=xxx&lang=xx
tc10=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=xxx&lang=xx")
#print (tc10.text)
#assert ((tc10.text).startswith("Please include valid parameters in API request.")) , "Error message cannot show correctly for dataType=xxx&lang=xx"
if (tc10.text).startswith("Please include valid parameters in API request."):
    print("Test Case 10: Error message show correctly for dataType=xxx&lang=xx")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 10: Error message cannot show correctly for dataType=xxx&lang=xx"))

#Test Case 11: check if error message is return successfully for dataType=null&lang=null
tc11=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=null&lang=null")
#print (tc11.text)
#assert ((tc11.text).startswith("Please include valid parameters in API request.")) , "Error message cannot show correctly for dataType=null&lang=null"
if (tc11.text).startswith("Please include valid parameters in API request."):
    print("Test Case 11: Error message show correctly for dataType=xxx&lang=xx")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 11: Error message cannot show correctly for dataType=null&lang=null"))

#Test Case 12: check if error message is return successfully for dataType=&lang=
tc12=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=&lang=")
#print (tc12.text)
#assert ((tc12.text).startswith("Please include valid parameters in API request.")) , "Error message cannot show correctly for dataType=&lang="
if (tc12.text).startswith("Please include valid parameters in API request."):
    print("Test Case 12: Error message show correctly for dataType=&lang=")
else:
    print(colored(255, 0, 0, "ERROR: Test Case 12: Error message cannot show correctly for dataType=&lang="))



#-------------------------------------Test Case 13-23-------------------------------------------
tc1323=requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en")
json_responsetc1323 = tc1323.json()

#----------------------------------Test Case 14: rainfall ----------------------------------------------
#Testing for Rainfall data place contains all 18 districts
testcase14placechecking = 'T'
#print("Testing for Rainfall data 18 districts")
#print(json_responsetc1323["rainfall"]["data"][0]["place"])
if json_responsetc1323["rainfall"]["data"][0]["place"] == "Central &amp; Western District":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Central & Western District' not correct"))
#print(json_responsetc1323["rainfall"]["data"][1]["place"])
if json_responsetc1323["rainfall"]["data"][1]["place"] == "Eastern District":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Eastern District' not correct"))
#print(json_responsetc1323["rainfall"]["data"][2]["place"])
if json_responsetc1323["rainfall"]["data"][2]["place"] == "Kwai Tsing":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Kwai Tsing' not correct"))
#print(json_responsetc1323["rainfall"]["data"][3]["place"])
if json_responsetc1323["rainfall"]["data"][3]["place"] == "Islands District":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Islands District' not correct"))
#print(json_responsetc1323["rainfall"]["data"][4]["place"])
if json_responsetc1323["rainfall"]["data"][4]["place"] == "North District":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'North District' not correct"))
#print(json_responsetc1323["rainfall"]["data"][5]["place"])
if json_responsetc1323["rainfall"]["data"][5]["place"] == "Sai Kung":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Sai Kung' not correct"))
#print(json_responsetc1323["rainfall"]["data"][6]["place"])
if json_responsetc1323["rainfall"]["data"][6]["place"] == "Sha Tin":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Sha Tin' not correct"))
#print(json_responsetc1323["rainfall"]["data"][7]["place"])
if json_responsetc1323["rainfall"]["data"][7]["place"] == "Southern District":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Southern District' not correct"))
#print(json_responsetc1323["rainfall"]["data"][8]["place"])
if json_responsetc1323["rainfall"]["data"][8]["place"] == "Tai Po":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Tai Po' not correct"))
#print(json_responsetc1323["rainfall"]["data"][9]["place"])
if json_responsetc1323["rainfall"]["data"][9]["place"] == "Tsuen Wan":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Tsuen Wan' not correct"))
#print(json_responsetc1323["rainfall"]["data"][10]["place"])
if json_responsetc1323["rainfall"]["data"][10]["place"] == "Tuen Mun":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Tuen Mun' not correct"))
#print(json_responsetc1323["rainfall"]["data"][11]["place"])
if json_responsetc1323["rainfall"]["data"][11]["place"] == "Wan Chai":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Wan Chai' not correct"))
#print(json_responsetc1323["rainfall"]["data"][12]["place"])
if json_responsetc1323["rainfall"]["data"][12]["place"] == "Yuen Long":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Yuen Long' not correct"))
#print(json_responsetc1323["rainfall"]["data"][13]["place"])
if json_responsetc1323["rainfall"]["data"][13]["place"] == "Yau Tsim Mong":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Yau Tsim Mong' not correct"))
#print(json_responsetc1323["rainfall"]["data"][14]["place"])
if json_responsetc1323["rainfall"]["data"][14]["place"] == "Sham Shui Po":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Sham Shui Po' not correct"))
#print(json_responsetc1323["rainfall"]["data"][15]["place"])
if json_responsetc1323["rainfall"]["data"][15]["place"] == "Kowloon City":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Kowloon City' not correct"))
#print(json_responsetc1323["rainfall"]["data"][16]["place"])
if json_responsetc1323["rainfall"]["data"][16]["place"] == "Wong Tai Sin":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Wong Tai Sin' not correct"))
#print(json_responsetc1323["rainfall"]["data"][17]["place"])
if json_responsetc1323["rainfall"]["data"][17]["place"] == "Kwun Tong":
    pass
else:
    testcase14placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data place 'Kwun Tong' not correct"))
if testcase14placechecking == 'T':
    print("Test Case 14: rainfall data place 18 districts returned correctly")

#Test for rainfall data main is equal to TRUE or FALSE
testcase14mainchecking = 'T'
for x in range (18):
    if json_responsetc1323["rainfall"]["data"][x]["main"] == "TRUE" or json_responsetc1323["rainfall"]["data"][x]["main"] == "FALSE":
        pass
    else:
        testcase14mainchecking = 'F'
        print(colored(255, 0, 0, "ERROR: Test Case 14: rainfall data main Maintenance flag returned incorrectly for data number "+ str(x+1)))

if testcase14mainchecking == 'T':
    print("Test Case 14: rainfall data main returned correctly")


#Test if rainfall data unit is with data type string
testcase14unitchecking = 'T'
for x in range (18):
    if type(json_responsetc1323["rainfall"]["data"][x]["unit"]) == str:
        pass
    else:
        testcase14unitchecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 14: rainfall data unit data type is not correct for data number " + str(x + 1)))
if testcase14unitchecking == 'T':
    print("Test Case 14: rainfall data unit returned correctly")

#Test for date format
date_stringtc14_startTime = json_responsetc1323["rainfall"]["startTime"]
date_stringtc14_endTime = json_responsetc1323["rainfall"]["endTime"]
format = "%Y-%m-%d"+"T"+"%H:%M:%S%z"       #YYYY-MM-DD'T'hh:mm:ssZ   Example:2020-09-01T08:19:00+08:00
try:
  datetime.datetime.strptime(date_stringtc14_startTime, format)
  print("Test Case 14: rainfall data startTime returned correctly")
except ValueError:
    print(colored(255, 0, 0,"ERROR: Test Case 14: This is the incorrect date string format for rainfall startTime. It should be YYYY-MM-DD'T'hh:mm:ssZ."))
try:
  datetime.datetime.strptime(date_stringtc14_endTime, format)
  print("Test Case 14: rainfall data endTime returned correctly")
except ValueError:
  print(colored(255, 0, 0,"ERROR: Test Case 14: This is the incorrect date string format for rainfall endTime. It should be YYYY-MM-DD'T'hh:mm:ssZ."))


#----------------------------------Test Case 15: icon --------------------------------------------
testcase15icon = json_responsetc1323["icon"]
testcase15iconchecking = 'T'
if isinstance(testcase15icon, list):
    pass
else:
    testcase15iconchecking = 'F'
    print(colored(255, 0, 0,"ERROR: Test Case 15: icon data returned with incorrect data format"))
for x in range(len(json_responsetc1323["icon"])):
    if type(json_responsetc1323["icon"][x-1]) == int:
        pass
    else:
        testcase15iconchecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 15: icon data type is not returned correctly for data number " + str(x + 1)))
if testcase15iconchecking == 'T':
    print("Test Case 15: icon data format returned correctly")


#----------------------------------Test Case 16: iconUpdateTime --------------------------------------------
date_stringtc16_iconUpdateTime = json_responsetc1323['iconUpdateTime']     #YYYY-MM-DD'T'hh:mm:ssZ   Example:2020-09-01T08:19:00+08:00
try:
  datetime.datetime.strptime(date_stringtc16_iconUpdateTime, format)
  print("Test Case 16: iconUpdateTime returned correctly")
except ValueError:
    print(colored(255, 0, 0,"ERROR: Test Case 16: This is the incorrect date string format for iconUpdateTime. It should be YYYY-MM-DD'T'hh:mm:ssZ."))



#----------------------------------Test Case 17: uvindex --------------------------------------------
testcase17uvindex = json_responsetc1323["uvindex"]
testcase17uvindexchecking = 'T'
"""
if isinstance(testcase17uvindex, list):
    pass
else:
    testcase17uvindexchecking = 'F'
    print(colored(255, 0, 0,"ERROR: Test Case 17: uvindex data returned with incorrect data format"))

for x in range(len(json_responsetc1323["uvindex"])):
    if type(json_responsetc1323["uvindex"]["data"][x-1]["value"]) == float:
        pass
    else:
        testcase17uvindexchecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 17: uvindex value data type is not returned correctly for data number " + str(x + 1)))
    if type(json_responsetc1323["uvindex"]["data"][x-1]["place"]) == str:
        pass
    else:
        testcase17uvindexchecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 17: uvindex place data type is not returned correctly for data number " + str(x + 1)))
    if type(json_responsetc1323["uvindex"]["data"][x-1]["desc"]) == str:
        pass
    else:
        testcase17uvindexchecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 17: uvindex desc data type is not returned correctly for data number " + str(x + 1)))

if type(json_responsetc1323["uvindex"]["recordDesc"]) == str:
    pass
else:
    testcase17uvindexchecking = 'F'
    print(colored(255, 0, 0,"ERROR: Test Case 17: uvindex recordDesc data type is not returned correctly for data number " + str(x + 1)))

if testcase17uvindexchecking == 'T':
    print("Test Case 17: uvindex data format returned correctly")
"""

#----------------------------------Test Case 18: updateTime --------------------------------------------
date_stringtc18_updateTime = json_responsetc1323["updateTime"]
format = "%Y-%m-%d"+"T"+"%H:%M:%S%z"       #YYYY-MM-DD'T'hh:mm:ssZ   Example:2020-09-01T08:19:00+08:00
try:
  datetime.datetime.strptime(date_stringtc18_updateTime, format)
  print("Test Case 18: updateTime returned correctly")
except ValueError:
    print(colored(255, 0, 0,"ERROR: Test Case 18: This is the incorrect date string format for updateTime. It should be YYYY-MM-DD'T'hh:mm:ssZ."))


#----------------------------------Test Case 19: warningMessage --------------------------------------------
testcase19warningMessage = json_responsetc1323["warningMessage"]
testcase19warningMessagechecking = 'T'
if isinstance(testcase19warningMessage, str):
    pass
else:
    testcase19warningMessagechecking = 'F'
    print(colored(255, 0, 0,"ERROR: Test Case 19: warningMessage data returned with incorrect data format"))

if testcase15iconchecking == 'T':
    print("Test Case 19: warningMessage returned correctly")


#----------------------------------Test Case 22: temperature --------------------------------------------
testcase22placechecking = 'T'
#print("Testing for Temperature data 27 places")
if json_responsetc1323["temperature"]["data"][0]["place"] == "King's Park":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'King's Park' not correct"))
if json_responsetc1323["temperature"]["data"][1]["place"] == "Hong Kong Observatory":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data  place 'Eastern District' not correct"))
if json_responsetc1323["temperature"]["data"][2]["place"] == "Wong Chuk Hang":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data  place 'Kwai Tsing' not correct"))
if json_responsetc1323["temperature"]["data"][3]["place"] == "Ta Kwu Ling":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data  place 'Ta Kwu Ling' not correct"))
if json_responsetc1323["temperature"]["data"][4]["place"] == "Lau Fau Shan":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Lau Fau Shan' not correct"))
if json_responsetc1323["temperature"]["data"][5]["place"] == "Tai Po":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Tai Po' not correct"))
if json_responsetc1323["temperature"]["data"][6]["place"] == "Sha Tin":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Sha Tin' not correct"))
if json_responsetc1323["temperature"]["data"][7]["place"] == "Tuen Mun":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Tuen Mun' not correct"))
if json_responsetc1323["temperature"]["data"][8]["place"] == "Tseung Kwan O":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Tseung Kwan O' not correct"))
if json_responsetc1323["temperature"]["data"][9]["place"] == "Sai Kung":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Sai Kung' not correct"))
if json_responsetc1323["temperature"]["data"][10]["place"] == "Cheung Chau":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Cheung Chau' not correct"))
if json_responsetc1323["temperature"]["data"][11]["place"] == "Chek Lap Kok":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Chek Lap Kok' not correct"))
if json_responsetc1323["temperature"]["data"][12]["place"] == "Tsing Yi":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Tsing Yi' not correct"))
if json_responsetc1323["temperature"]["data"][13]["place"] == "Shek Kong":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Shek Kong' not correct"))
if json_responsetc1323["temperature"]["data"][14]["place"] == "Tsuen Wan Ho Koon":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Tsuen Wan Ho Koon' not correct"))
if json_responsetc1323["temperature"]["data"][15]["place"] == "Tsuen Wan Shing Mun Valley":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Tsuen Wan Shing Mun Valley' not correct"))
if json_responsetc1323["temperature"]["data"][16]["place"] == "Hong Kong Park":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Hong Kong Park' not correct"))
if json_responsetc1323["temperature"]["data"][17]["place"] == "Shau Kei Wan":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Shau Kei Wan' not correct"))
if json_responsetc1323["temperature"]["data"][18]["place"] == "Kowloon City":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Kowloon City' not correct"))
if json_responsetc1323["temperature"]["data"][19]["place"] == "Happy Valley":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Happy Valley' not correct"))
if json_responsetc1323["temperature"]["data"][20]["place"] == "Wong Tai Sin":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Wong Tai Sin' not correct"))
if json_responsetc1323["temperature"]["data"][21]["place"] == "Stanley":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Stanley' not correct"))
if json_responsetc1323["temperature"]["data"][22]["place"] == "Kwun Tong":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Kwun Tong' not correct"))
if json_responsetc1323["temperature"]["data"][23]["place"] == "Sham Shui Po":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Sham Shui Po' not correct"))
if json_responsetc1323["temperature"]["data"][24]["place"] == "Kai Tak Runway Park":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Kai Tak Runway Park' not correct"))
if json_responsetc1323["temperature"]["data"][25]["place"] == "Yuen Long Park":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Yuen Long Park' not correct"))
if json_responsetc1323["temperature"]["data"][26]["place"] == "Tai Mei Tuk":
    pass
else:
    testcase22placechecking = 'F'
    print(colored(255, 0, 0, "ERROR: Test Case 22: Temperature data place 'Tai Mei Tuk' not correct"))
if testcase22placechecking == 'T':
    print("Test Case 22: Temperature data 27 places returned correctly")

#Test if temperature data value is with data type int
testcase22valuechecking = 'T'
for x in range (27):
    if type(json_responsetc1323["temperature"]["data"][x]["value"]) == int:
        pass
    else:
        testcase22valuechecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 22: temperature data value data type is not correct for data number " + str(x + 1)))
if testcase22valuechecking == 'T':
    print("Test Case 22: temperature data value returned correctly")

#Test if temperature data unit is with data type string
testcase22unitchecking = 'T'
for x in range (27):
    if type(json_responsetc1323["temperature"]["data"][x]["unit"]) == str:
        pass
    else:
        testcase22unitchecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 22: temperature data unit data type is not correct for data number " + str(x + 1)))
if testcase22unitchecking == 'T':
    print("Test Case 22: temperature data unit returned correctly")

#Test for date format recordTime
date_stringtc22_recordTime = json_responsetc1323["temperature"]["recordTime"]
try:
  datetime.datetime.strptime(date_stringtc22_recordTime, format)
  print("Test Case 22: temperature data recordTime returned correctly")
except ValueError:
    print(colored(255, 0, 0,"ERROR: Test Case 22: This is the incorrect date string format for temperature recordTime. It should be YYYY-MM-DD'T'hh:mm:ssZ."))


#----------------------------------Test Case 23: humidity --------------------------------------------
testcase23Humidity = json_responsetc1323["humidity"]
testcase23Humiditychecking = 'T'

for x in range(len(json_responsetc1323["humidity"])):
    if type(json_responsetc1323["humidity"]["data"][x-1]["value"]) == int:
        pass
    else:
        testcase23Humiditychecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 23: humidity value data type is not returned correctly for data number " + str(x + 1)))
    if type(json_responsetc1323["humidity"]["data"][x-1]["place"]) == str:
        pass
    else:
        testcase23Humiditychecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 23: humidity place data type is not returned correctly for data number " + str(x + 1)))
    if type(json_responsetc1323["humidity"]["data"][x-1]["unit"]) == str:
        pass
    else:
        testcase23Humiditychecking = 'F'
        print(colored(255, 0, 0,"ERROR: Test Case 17: humidity unit data type is not returned correctly for data number " + str(x + 1)))
if testcase23Humiditychecking == 'T':
    print("Test Case 23: humidity data format returned correctly")

#Test for humidity recordTime date format
date_stringtc23_recordTime = json_responsetc1323["humidity"]["recordTime"]
format = "%Y-%m-%d"+"T"+"%H:%M:%S%z"       #YYYY-MM-DD'T'hh:mm:ssZ   Example:2020-09-01T08:19:00+08:00
try:
  datetime.datetime.strptime(date_stringtc23_recordTime, format)
  print("Test Case 23: humidity recordTime returned correctly")
except ValueError:
    print(colored(255, 0, 0,"ERROR: Test Case 23: This is the incorrect date string format for humidity recordTime. It should be YYYY-MM-DD'T'hh:mm:ssZ."))







import requests
url='http://127.0.0.1:5001/predictdata'
data={'gender':'female','ethnicity':'group C','parental_level_of_education':'bachelor\'s degree','lunch':'standard','test_preparation_course':'none','reading_score':'70','writing_score':'80'}
r=requests.post(url,data=data)
print(r.status_code)
print(r.text)

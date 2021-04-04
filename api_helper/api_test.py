import requests

years_exp = [{"Age": 22, "Sex": "male", "Embarked": "S"},
             {"Age": 22, "Sex": "female", "Embarked": "C"},
             {"Age": 80, "Sex": "female", "Embarked": "C"},
             {"Age": 22, "Sex": "male", "Embarked": "S"},
             {"Age": 22, "Sex": "female", "Embarked": "C"},
             {"Age": 80, "Sex": "female", "Embarked": "C"},
             {"Age": 22, "Sex": "male", "Embarked": "S"},
             {"Age": 22, "Sex": "female", "Embarked": "C"},
             {"Age": 80, "Sex": "female", "Embarked": "C"},
             {"Age": 22, "Sex": "male", "Embarked": "S"},
             {"Age": 22, "Sex": "female", "Embarked": "C"},
             {"Age": 80, "Sex": "female", "Embarked": "C"},
             {"Age": 22, "Sex": "male", "Embarked": "S"},
             {"Age": 22, "Sex": "female", "Embarked": "C"},
             {"Age": 80, "Sex": "female", "Embarked": "C"},
             ]
response = requests.post(url='http://127.0.0.1:8000/predict', json=years_exp)
print(response)
result = response.json()
print('model API返回结果：', result)
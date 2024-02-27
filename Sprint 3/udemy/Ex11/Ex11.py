#Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
#Dica: leia a documentação do pacote json



import json

with open('person.json', 'r') as arquivo:
    dados_json = json.load(arquivo)


print(f"'name': '{dados_json['name']}', "
      f"'endereco': '{dados_json['endereco']}', "
      f"'startDateExecution': '{dados_json['startDateExecution']}', "
      f"'endDateExecution': '{dados_json['endDateExecution']}', "
      f"'siteId': '{dados_json['siteId']}', "
      f"'sitePage': '{dados_json['sitePage']}', "
      f"'serverName': '{dados_json['serverName']}', "
      f"'profileId': '{dados_json['profileId']}', "
      f"'type': '{dados_json['type']}', "
      f"'path': '{dados_json['path']}', "
      f"'performanceType': '{dados_json['performanceType']}'")
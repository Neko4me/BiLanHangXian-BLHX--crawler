import requests
import time
a=0
while True:
	filename='data.txt'
	url='http://activity.biligame.com/board/list?game_id=182&game_key=f2c26927abcd14f2&rows=32'
	r = requests.get(url)
	a=a+1
	print("Success!get"+str(a)+"time",r.status_code)
	response_dict=r.json()
	repo_dicts=response_dict['data']
	with open(filename,'a') as file_object:
		for repo_dict in repo_dicts:
			file_object.write(repo_dict['id']+'  '+repo_dict['sname']+'  '+repo_dict['rname']+'  '+repo_dict['info']+'\n')
	time.sleep(120)
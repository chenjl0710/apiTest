import requests,json

def get_token():
    url = "http://bt1.geosts.ac.cn/api/uc/api/v2/account/login"
    payload = {"username":"1368666314@qq.com","password":"111222","service":"http://www.imagesky.com.cn/"}
    r = requests.post(url,params = payload)
    # print(r.url)
    preview = json.loads(r.text)
    # print(preview)
    status = preview.get('status')
    token = None
    if status == 200:
        token = preview.get('data').get('token')
        # print(token)
    return token

def taskList(sheetId,owner):
    url = "http://bt1.geosts.ac.cn/api/dcpp/dcpp/rest/v1/task/avaliable/list"
    headers = {"Content-Type": "application/json"}
    data = {
        "sheetId":sheetId,
        "owner":owner
    }
    r = requests.post(url=url,json=data,headers=headers)
    preview = json.loads(r.text)
    status = preview.get('status')
    list = None
    if status == 200:
        # print("任务查询列表：\n",preview)
        list = preview.get('data').get('list')
    return list

def getTask(taskid,token):
    url = "http://bt1.geosts.ac.cn/api/dcpp/dcpp/rest/v1/task/" + taskid + "/take"
    headers = {"Authorization": token}
    r = requests.post(url=url,headers=headers)
    preview = json.loads(r.text)
    status = preview.get('status')
    defaultDir = None
    if status == 200:
        # print("任务领取内容：\n", json.dumps(preview,sort_keys=True,indent=4,separators=(',', ': '),ensure_ascii=False))
        defaultDir = preview.get('data').get('defaultDir')
    return preview,defaultDir


# if __name__ == '__main__':
#     # token = get_token()
#     tasks = taskList(sheetId=1, owner=146);print(tasks)
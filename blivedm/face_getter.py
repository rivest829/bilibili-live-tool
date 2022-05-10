import requests


def get_user_face(uid):
    url = "https://api.bilibili.com/x/space/acc/info?mid=" + str(uid)
    headers = {
        'Content-Type': 'text/plain'
    }
    response_json = requests.request("GET", url, headers=headers).json()
    success = response_json["code"] == 0
    face = ""
    if success:
        face = response_json["data"]["face"]
    else:
        print("get face failed!!!")
    return face

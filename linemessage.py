import requests

def sendmessage(send_contents):
    TOKEN = 'LINE_API_TOKEN'
    api_url = 'https://notify-api.line.me/api/notify'

    #情報を辞書型にする
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN} 
    send_dic = {'message': send_contents}

    #LINE通知を送る（200: 成功時、400: リクエストが不正、401: アクセストークンが無効：公式より）
    requests.post(api_url, headers=TOKEN_dic, data=send_dic)

#sendmessage('Function!')
import requests


client_id = '26d963fd24fd21542a20987d515d3d4f'
client_secret = '26d963fd24fd21542a20987d515d3d4f370f69036d9e0a80025c6f70047d84bb41ce35c1'
access_token = '25316c0c8ed9b146238d706db37a886a_e514b92379bd7d84a8648a18215d0017'
code = '8bcf4b8a37494fd7f0587e7b677039e982fc3d222d2ddd76cbaaf3f90db2929f5c42c379'
redirect_uri = 'https://heeyaaaworld.tistory.com/'
blogName = 'heeyaaaworld'
tag = '테스트, test'					#등록할 태그값, 쉼표로 구분
output = 'json'						#고정값
grant_type = 'authorization_code'   #고정값
visibility = 0  #0은 비공개, 3은 공개 발행
category =  617405

"""
def getToken():
    url = 'https://www.tistory.com/oauth/access_token?'
    data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri,
            'code': code,
            'grant_type': grant_type
            }
    r = requests.get(url, data)
    print (r.text)

def getCategory():
    url = 'https://www.tistory.com/apis/category/list?'
    data = {
            'access_token': access_token,
            'output': output,
            'blogName': blogName,
            }
    r = requests.get(url, data)
    print (r.text)
"""

def postWrite(content):
        title = '자동 포스팅 테스트'
        url = 'https://www.tistory.com/apis/post/write?'
        data = {
                 'access_token': access_token,
                 'output': output,
                 'blogName': blogName,
                 'title': title,
                 'content': content,
                 'visibility': visibility,
                 'category': category,
                 'tag': tag,
                 }
        r = requests.post(url, data=data)
        print ('자동 포스팅 성공')
        return r.text


if __name__ == '__main__':
    # getToken()    #최초 토큰 발급시에만 수행
    # getCategory()  #최초 카테고리 확인시에만 수행
	postWrite('테스트 등록 글입니다.')
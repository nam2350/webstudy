### 모듈 import
import requests

def load_data(**kwargs):
    ### 본인의 인정키 입력
    crtfc_key = "6f7c4a97fbac7c000f8a17c677f64faaddcfd094"
    ### load_data 함수 입력을 통해 corp_code 를 받기로 한다.
    corp_code = kwargs['corp_code']
    
    ###기업개황 요청하면
    if kwargs['request'] == 'company':
        
        ### 기업개황 요청 url
        url = 'https://opendart.fss.or.kr/api/company.json?crtfc_key='+crtfc_key+'&corp_code='+corp_code
        
        ### HTTP 요청
        r = requests.get(url)
        
        ### 요청한 데이터는 json형태이기 때문에 json으로 읽어줍니다.
        company_data = r.json()
        
        ### 기업개황을 요청했을 때 기업개황에 대한 자료를 반환합니다.
        return company_data

samsung = load_data(request='company', corp_code='00126380')

print(samsung)

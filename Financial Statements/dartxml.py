### 필요한 모듈
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import xml.etree.ElementTree as ET

### 회사고유번호 데이터 불러오기
url = 'https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=6f7c4a97fbac7c000f8a17c677f64faaddcfd094'
with urlopen(url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('corp_num')


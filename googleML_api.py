# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six
# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'''VR·AR
VR과 AR도 5G 전용 콘텐츠로 마련되고 있다. SK텔레콤은 VR 서비스로 ‘실감형 아이돌 방송’을 차례로 선보인다. 특히 5월 중 엠넷의 최고 인기프로그램 ‘프로듀스 101’ 시리즈를 실감형 버전으로 만들어 독점 중계한다. 아이돌 라디오, 아프리카TV ‘댄서프로젝트’, MBC플러스 ‘주간아이돌’ 등도 VR로 제공한다. 또 5G VR로 영어 강사와 1:1 코칭을 받는 느낌을 주는 가상현실 서비스 ‘Speak it!’, 세계 20개 도시와 고흐 · 클림트 등의 명화를 도슨트 설명과 함께 둘러보는 여행, 문화 콘텐츠도 함께 제공한다.
AR 영역에서는 ‘포켓몬 고’로 유명한 나이언틱과 독점 제휴를 통해 ‘해리포터 AR’을 상반기 오픈한다. SK텔레콤이 포켓몬 고 때 맺었던 제휴와 비슷한 형식으로 오프라인 영역에서 서비스를 제공할 것으로 보인다. AR글래스 업체 매직리프와 함께 AR 서비스도 곧 선보일 계획이다.
KT는 VR기기와 전용 콘텐츠를 함께 제공하는 개인형 대표 실감미디어 서비스인 ‘기가라이브TV’를 5G에 맞게 개선한다. 새로 출시된 기가 라이브 TV 앱을 설치하면 스마트폰 영상을 기가 라이브 TV에서 동시 시청할 수 있고, 세계 최초 스마트폰과 VR기기 간 연동 게임인 스페셜 포스 VR도 즐길 수 있다.
KT는 3D와 AR 기술을 활용한 영상통화 서비스 ‘나를(narle)’ 앱도 내놨다. ‘3D 아바타’와 ‘AR 이모티커’ 등 꾸미기 기능을 활용해 자신의 모습을 원하는 대로 설정할 수 있는 영상통화 앱이다.
‘리얼 360’ 앱도 선보였다. 이 앱은 최대 4명과 초고화질(UHD)로 360도 그룹 커뮤니케이션을 할 수 있고, SNS 팔로워에 360도 라이브 스트리밍을 제공하는 등 1인 미디어 생방송을 할 수 있는 차세대 커뮤니케이션 앱이다. 오는 5월 출시 예정인 넥밴드형 360카메라(FITT 360)를 착용하면, 3개의 카메라가 촬영한 영상을 스티칭하여 360도 영상으로 송수신할 수 있다.
LG유플러스는 VR기기를 이용해 스타데이트, 웹툰, 공연을 즐길 수 있는 콘텐츠를 준비했다. 내 앞에 앉아있는 스타와 1:1 데이트하는 느낌을 주는 VR 영상을 통해 손나은, 이달의 소녀, 차은우, 성훈 등을 만나볼 수 있으며, 네이버에서 극한의 공포로 폭발적인 인기를 기록했던 웹툰인 ‘옥수역 귀신’을 생동감 있게 볼 수 있다. 21세기 공연의 새로운 패러다임을 창조한 ‘태양의 서커스’ 공연을 실제와 같은 초고화질로 볼 수도 있다. 실제 스타가 내 앞에 있는 것처럼 3D로 나타나고, 360도 회전도 가능한 AR 서비스도 선보인다.'''
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

def entities_text(text): # 항목 분석
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type.name))
        print(u'{:<16}: {}'.format('metadata', entity.metadata))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))


entities_text(text)
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six
import json


# Instantiates a client
client = language.LanguageServiceClient()

analyze_file = "C:\\Secu\\파이썬팁.txt"

# https://googleapis.github.io/google-cloud-python/latest/language/usage.html

def sentiment_text(text): # 감정 분석
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    return [sentiment.score, sentiment.magnitude]

# print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


def entities_text(text): # 항목 분석
    entity_list = []
    cnt = 0
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type='PLAIN_TEXT')

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    for entity in entities:
        cnt += 1
        entity_type = enums.Entity.Type(entity.type)
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type.name))
        # print(u'{:<16}: {}'.format('metadata', entity.metadata))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        # print(u'{:<16}: {}'.format('wikipedia_url',
              # entity.metadata.get('wikipedia_url', '-')))

        ent_dict = dict(name=entity.name, type=entity_type.name, salience=float(entity.salience))
        entity_list.append(ent_dict)
        if cnt > 10:
            break
    return entity_list
# entities_text(text)


if __name__=='__main__':
    # The text to analyze

    text = u'''2019년 4월 17일 오전 4시 25분경 피의자 안인득(42세)은 자신의 집에서 휘발유를 뿌리자마자 방화를 저지른 후, 2층 계단으로 내려가 주민들이 대피하기만을 기다렸다. 화재가 일어나자마자 아파트 주민들이 내려가 대피하려던 순간, 흉기를 마구 휘둘렀다. 이 과정에서 5명이 숨졌고, 6명은 중·경상을 입었다.[2] 9명은 화재 연기를 마셔 병원 치료를 받았다.'''
    score, magnitude = sentiment_text(text)
    print("score : {},  magnitude : {}".format(score, magnitude))
    entities = entities_text(text)
    j = json.dumps(entities, ensure_ascii=False)
    print(j)
    with open('google_entity.json', 'w') as fout:
        json.dump(entities, fout)



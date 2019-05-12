# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six
import json


# Instantiates a client
client = language.LanguageServiceClient()


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
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    for entity in entities:
        cnt += 1
        entity_type = enums.Entity.Type(entity.type)
        '''print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type.name))
        print(u'{:<16}: {}'.format('metadata', entity.metadata))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
        '''
        ent_dict = dict(name=entity.name, type=entity_type.name, salience=float(entity.salience))
        entity_list.append(ent_dict)
        if cnt > 10:
            break
    return entity_list
# entities_text(text)


if __name__=='__main__':
    # The text to analyze
    text = u'''	OAuth 2.0 프로토콜에서 E-mail을 이용한 사용자 권한 인증.pdf'''
    score, magnitude = sentiment_text(text)
    print("score : {},  magnitude : {}".format(score, magnitude))
    entities = entities_text(text)
    j = json.dumps(entities, ensure_ascii=False)
    print(j)
    with open('google_entity.json', 'w') as fout:
        json.dump(entities, fout)



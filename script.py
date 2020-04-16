from flashtext.keyword import KeywordProcessor
import pickle

def get_keywords_api():
    keyword_processor = pickle.load(open('processor.pkl', 'rb'))

    def keywords_api(keywordProcessor, text, span_info=True):
        keywords_found = keywordProcessor.extract_keywords(text, span_info=True)
        return keywords_found

    return keywords_api

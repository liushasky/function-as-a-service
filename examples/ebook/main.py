
import nltk
import pandas as pd
import requests as rqst
import plotly.express as px

def text_processing(request):
    rpns = rqst.get(request.args['url'])
    sentence = rpns.text
    tokens = nltk.sent_tokenize(sentence)
    tokens_df = pd.DataFrame({'tokens': tokens})
    tokens_df['sentence_length'] = tokens_df['tokens'].apply(lambda x: len(x))
    fig = px.histogram(tokens_df, x="sentence_length", nbins=20, title='Source Book: {}'.format(request.args['url']))
    return fig.to_html()

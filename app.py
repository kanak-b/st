import streamlit as st
import spacy

from spacy import displacy
#from wordcloud import WordCloud

import matplotlib.pyplot as plt
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

from bs4 import BeautifulSoup
from urllib.request import urlopen

nlp = spacy.load('en_core_web_sm')

def sumy_summ(docx):
    parser = PlaintextParser.from_string(docx,Tokenizer('english'))
    lex_summ = LexRankSummarizer()
    summary = lex_summ(parser.document,3)
    summary_list = [str(s) for s in summary]
    result = ' '.join(summary_list)
    return result

#@st.cache(allow_output_mutation=True)
def analyze_text(text):
    return nlp(text)    


def main():

    st.title("Summary and Entity Checker")
    activities = ['Summarize', 'NER']
    choice = st.sidebar.selectbox("What do you want to do?", activities)

    if choice == "Summarize":
        st.subheader("Summary with NLP")
        raw_text = st.text_area("Enter text here")
        if st.button("Summarize"):
            sumresult = sumy_summ(raw_text)
            st.write(sumresult)

    if choice == "NER":
        st.subheader("Named Entity Recognition with spacy")
        raw_text = st.text_area("Enter text here")
        if st.button("Analyze"):
            docx = analyze_text(raw_text)
            html = displacy.render(docx, style = 'ent')
            html = html.replace("\n\n", "\n")
            st.write(HTML_WRAPPER.format(html), unsafe_allow_html = True)

     #   if st.checkbox("Show Wordcloud"):
     #       wc = WordCloud().generate(raw_text)
     #       plt.imshow(wc, interpolation='bilinear')
     #       plt.axis("off")
	 #       st.pyplot()
         


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

if __name__ == "__main__":
    main()

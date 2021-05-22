#!/usr/bin/env python
"""
Author: Denis Pointer

Purpose:
Portfolio Project for 100 Days of Code Course to read a PDF file and
convert to speech using an Internet Text-To-Speech API. For this project
I will be using http://www.voicerss.org/api/ there are several others
available, examples from course include:
- http://www.ispeech.org/api/#introduction
- https://cloud.google.com/text-to-speech/docs/basics
- https://aws.amazon.com/polly/


Course Reference: https://www.udemy.com/course/100-days-of-code
"""
import os

import PyPDF2
import requests

from dotenv import load_dotenv

load_dotenv()


def read_pdf(pdf):
    """
    Take a PDF File, read the text and return it as a single long string
    striping all line breaks

    Args:
        pdf (str): pdf file name

    Returns:
        str: long string from file
    """
    pages = []
    with open(pdf, "rb") as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        for page in range(pdf_reader.numPages):
            page_obj = pdf_reader.getPage(page)
            text = page_obj.extractText()
            text = text.replace("\n", "")
            text = text.strip()
            pages.append(text)
    return " ".join(pages)


def voice_rss_tts(text, lang="en-ca"):

    api_key = os.getenv("API_KEY")
    url = "http://api.voicerss.org/"
    params = {"key": api_key, "hl": lang, "src": text}
    response = requests.get(url, params=params)
    with open("response.wav", "wb") as f:
        f.write(response.content)


def main():
    text = read_pdf("samplePDF.pdf")
    voice_rss_tts(text)


if __name__ == "__main__":
    main()

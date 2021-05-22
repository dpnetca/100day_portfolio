# Day 90 - Convert PDF to Audio Book

## Instructions:

Too tired to read? Build a python script that takes a PDF file, identifies the text and converts the text to speech. Effectively creating a free audiobook.

AI text-to-speech has come so far. They can sound more lifelike than a real audiobook.

Using what you've learnt about HTTP requests, APIs and Python scripting, create a program that can convert PDF files to speech.

You right want to choose your own Text-To-Speech (TTS) API. But here are some you can consider:

- http://www.ispeech.org/api/#introduction
- https://cloud.google.com/text-to-speech/docs/basics
- https://aws.amazon.com/polly/

### Known Issues:

- There is a max request size of 100KB per request, so large PDF files using this script will fail. This could be resolved by checking the input text length, and chopping it into smaller pieces, and looping over these small pieces for conversion.
- By stripping all line breaks from the PDF file it may result paragraphs blending together instead of including a natural pause between paragraphs. Linebreaks were stripped though as PyPDF reader was inserting line breaks in places where no linebreak existed. In many cases this was mid-word. As such the decsion was made to remove all line breaks.

## Author Notes

This is a simple script following the course direction to convert PDF to a wav file. This project has inspired me to create a a similar application that has some real world use for me. As such I have not added a lot of features to this project but will instead focus that effort onto my real world use case: https://github.com/dpnetca/cc_prompt_generator

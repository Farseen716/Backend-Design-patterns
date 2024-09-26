"""The Template pattern use case example by Farseen Ashraf"""
from text_document import TextDocument
from html_document import HTMLDocument

text_document = TextDocument()
text_document.create_document("Some Document")

html_document = HTMLDocument()
html_document.create_document("Line 1\nLine 2")

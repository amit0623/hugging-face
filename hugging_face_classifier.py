# -*- coding: utf-8 -*-
"""hugging-face-classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ne9tm5hzccHxzlj8I5f18QeWn12MsC0g
"""

!pip install transformers

!pip install transformers[sentencepiece]

import transformers

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

classifier("We are very sad to show you the 🤗 Transformers library.")
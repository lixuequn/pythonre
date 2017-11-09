#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.analysis import RegexAnalyzer
analyzer = RegexAnalyzer(ur"([\u4e00-\u9fa5])|(\w+(\.?\w+)*)")
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
ix = create_in("/Users/lixuequn/Desktop/", schema)
writer = ix.writer()
writer.add_document(title=u"First document", path=u"/a",
content=u"This is the first document we’ve added!")
writer.add_document(title=u"Second document", path=u"/b",
content=u"The second one 你 中文测试中文 is even more interesting!")
writer.commit()
searcher = ix.searcher()
results = searcher.find("content", u"first")
print results[0]
results = searcher.find("content", u"你")
print results[0]
results = searcher.find("content", u"测试")
print results[0]

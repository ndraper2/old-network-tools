# -*- coding: utf-8 -*-
from echo_client import echo_client


def test_simple_string():
    response = echo_client('This is the message to send')
    assert response == "I heard: This is the message to send"


def test_same_size_as_buffer():
    response = echo_client('aaaaaaaabbbbbbbb'.encode('utf-8'))
    assert response == u"I heard: aaaaaaaabbbbbbbb"


def test_unicode_string():
    response = echo_client('test character ó'.encode('utf-8'))
    assert response == u"I heard: test character ó"


def test_unicode_above_255():
    response = echo_client('test character ɯ'.encode('utf-8'))
    assert response == u"I heard: test character ɯ"

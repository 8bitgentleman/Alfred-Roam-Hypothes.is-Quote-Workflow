# -*- coding: utf-8 -*-

import json
import urllib.request as urllib2
import datetime
import sys
import subprocess
from tkinter import Tk
import os

from string import Template

import pprint
pp = pprint.PrettyPrinter(indent=4)


# config
HYPOTHESIS_TOKEN = os.environ['token']
HYPOTESIS_USER = os.environ['username']

HYPOTESIS_ID = 'acct:' + HYPOTESIS_USER + '@hypothes.is'
HYPOTHESIS_USER_URL = "https://hypothes.is/users/" + HYPOTESIS_USER

# set clipboard
# subprocess.run("pbcopy", universal_newlines=True, input=data)


def create_hiccup(username, date, url, user_url="", highlight="", annotation=""):
    '''Takes highlight info and turns it into an HTML based clojure hiccup styled correctly. Based on HTMO from https://codepen.io/thearchitect21/pen/bGVzJLe'''

    hiccup = Template(""":hiccup [:html [:head [:style ".annotation-card {font-family: \"Helvetica\", sans-serif;font-size: 13px;border: 1px solid #ececec;list-style: none;padding: 13px;margin-bottom: 10px;box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.4);background: #fff;overflow-wrap: break-word;max-width: 400px;}.annotation-card:hover {box-shadow: 0 2px 3px 0 rgba(0, 0, 0, 0.45);}.annotation-card:hover .annotation-card__quote {border-left: #F79158 3px solid;color:black !important;}.annotation-card:hover .annotation-card__timestamp{color: #7a7a7a !important;}.annotation-card:hover .annotation-card__username{color: #7a7a7a !important;}.annotation-card:hover .annotation-card__text{color: #7a7a7a !important;}.annotation-card__header {color: #a6a6a6 !important;margin-bottom: 15px;-ms-flex-align: baseline;align-items: baseline;}.annotation-card__username-timestamp {display: -ms-flexbox;display: flex;-ms-flex-direction: row;flex-direction: row;-ms-flex-pack: justify;justify-content: space-between}.annotation-card__username {color: #a6a6a6 !important;font-style: italic;font-weight: 200}.annotation-card__timestamp {font-size: 11px;line-height: 12px;font-weight: 400;letter-spacing: .2px;color: #a6a6a6 !important;}.annotation-card__text {line-height: normal;overflow-wrap: break-word;color:#a6a6a6 !important;font-weight: 400;}.annotation-card__text h1,.annotation-card__text h2,.annotation-card__text h3,.annotation-card__text h4,.annotation-card__text h5,.annotation-card__text h6,.annotation-card__text p,.annotation-card__text ol,.annotation-card__text ul,.annotation-card__text img,.annotation-card__text pre,.annotation-card__text blockquote {margin: .618em 0}.annotation-card__text h1,.annotation-card__text h2,.annotation-card__text h3,.annotation-card__text h4,.annotation-card__text h5,.annotation-card__text h6 {font-family: \"Helvetica Neue\", Helvetica, Arial, \"Lucida Grande\", sans-serif}.annotation-card__text h1 {font-size: 2.618em;font-weight: bold;margin: .2327em 0}.annotation-card__text h2 {font-size: 1.991em;font-weight: bold;margin: .309em 0}.annotation-card__text h3 {font-size: 1.991em;margin: .309em 0}.annotation-card__text h4 {font-size: 1.618em;margin: .3803em 0}.annotation-card__text h5 {font-size: 1.231em;margin: .4944em 0}.annotation-card__text h6 {font-size: 1.231em;margin: .4944em 0}.annotation-card__text ol,.annotation-card__text ul {list-style-position: inside;padding-left: 0}.annotation-card__text ol ol,.annotation-card__text ol ul,.annotation-card__text ul ol,.annotation-card__text ul ul {padding-left: 1em}.annotation-card__text ol {list-style-type: decimal}.annotation-card__text ul {list-style-type: disc}.annotation-card__text ol ul,.annotation-card__text ul ul {list-style-type: circle}.annotation-card__text li {margin-bottom: .291em}.annotation-card__text li,.annotation-card__text p {line-height: 1.3}.annotation-card__text a {text-decoration: underline}.annotation-card__text img {display: block;max-width: 100%}.annotation-card__text blockquote {font-size: 13px;line-height: 15px;font-weight: 400;border-left: 3px solid #dbdbdb;color: #a6a6a6 !important;font-family: sans-serif;font-size: 12px;font-style: italic;letter-spacing: .1px;padding: 0 1em;margin: 1em 0}.annotation-card__text blockquote p,.annotation-card__text blockquote ol,.annotation-card__text blockquote ul,.annotation-card__text blockquote img,.annotation-card__text blockquote pre,.annotation-card__text blockquote blockquote {margin: .7063em 0}.annotation-card__text blockquote p,.annotation-card__text blockquote li {line-height: 1.5}.annotation-card__text code {font-family: Open Sans Mono, Menlo, DejaVu Sans Mono, monospace;font-size: .875em;color: #000}.annotation-card__text pre code {padding: 10px;display: block;background-color: #f2f2f2;border-radius: 2px}.annotation-card__quote {padding: 0 10px;overflow-wrap: break-word;color: #4d4d4d !important;font-weight: bold;font-family: sans-serif;font-size: 14px;font-style: italic;letter-spacing: .1px;border-left: 3px solid #dbdbdb;margin-bottom: 10px;margin-left: 0;margin-right: 0}.annotation-card__tags {display: -ms-flexbox;display: flex;-ms-flex-direction: row;flex-direction: row;-ms-flex-wrap: wrap;flex-wrap: wrap}.annotation-card__tag {text-decoration: none;border: 1px solid #dbdbdb;border-radius: 2px;padding: 0 5px 2px;color: #7a7a7a;background: #f2f2f2;margin: 0 5px 5px 0;font-size: 11px;cursor: pointer;white-space: nowrap;overflow: hidden;text-overflow: ellipsis}.annotation-card__footer {display: -ms-flexbox;display: flex;-ms-flex-direction: row;flex-direction: row;-ms-flex-pack: end;justify-content: flex-end;-ms-flex-align: baseline;align-items: baseline}.annotation-card__footer-link {margin-left: 15px;color: #a6a6a6;height: 16px;width: 16px;float:left}.annotation-card__incontext-link {height: 14px;width: 14px;padding-top: 1px}.annotation-card__incontext-link:visited {color: #7a7a7a}.svg-icon {transform: translateX(0)}svg {-webkit-tap-highlight-color: rgba(255, 255, 255, 0)}a,a:active,a:focus,a:hover {text-decoration: none}ul,ol,li {border: 0;list-style: none;margin: 0;padding: 0}*,*:after,*:before {box-sizing: border-box}a {background-color: transparent}html,body{background-color: var(--page-color, #fff) !important;}"]] [:body [:li{:class "annotation-card"}[:div{:class "annotation-card__header"}[:div{:class "annotation-card__username-timestamp"}[:a{:title "username",:href "$user_url",:target "_blank",:class "annotation-card__username"}"$username"] [:a{:title "date",:href "$url",:target "_blank",:class "annotation-card__timestamp"}"$date"]]] [:blockquote{:title "Annotation quote",:class "annotation-card__quote"}"$highlight"] [:div{:class "annotation-card__text"}[:p "$annotation"]] [:footer{:class "annotation-card__footer"}[:a{:href "$url",:rel "nofollow noopener",:target "_blank",:title "Visit annotation in context"}[:svg{:xmlns "http://www.w3.org/2000/svg",:class "svg-icon annotation-card__footer-link annotation-card__incontext-link",:height "11",:viewbox "0 0 11 11",:width "11"}[:path{:d "M7.586 2H4V0h5.997A1.002 1.002 0 0111 1.003V7H9V3.414l-7.293 7.293L.293 9.293 7.586 2z",:fill "currentColor",:fill-rule "evenodd"}]]]]]]]""")

    clip = hiccup.substitute(date=date, username=username, user_url=user_url, highlight=highlight, annotation=annotation, url=url)

    return clip


def get_highlight(auth, id):
    '''Gets a highlight from hypothes.is and returns relevant info.'''
    urlData = "https://hypothes.is/api/annotations/" + id
    req = urllib2.Request(urlData)
    req.add_header('Authorization', 'Bearer %s' % auth)

    webURL = urllib2.urlopen(req)
    data = webURL.read()
    # encoding = webURL.info().get_content_charset('utf-8')
    j = json.loads(data.decode('utf-8'))

    try:
        article = j['document']['title'][0]
    except Exception:
        article = ""
    try:
        url = j['links']['incontext']
    except Exception:
        url = ""
    try:
        date_created = j['created'][:10]
    except Exception:
        date_created = ""
    try:
        date_updated = j['updated'][:10]
    except Exception:
        date_updated = ""
    try:
        tags = j['tags']
    except Exception:
        tags = ""
    try:
        annotation = j['text']
    except Exception:
        annotation = ""
    try:
        highlight = j['target'][0]['selector'][2]['exact']
    except Exception:
        highlight = ""
    return highlight, annotation, tags, date_created, date_updated, url, article


def parse_clipboard_link():
    clip = Tk().clipboard_get()
    if "hyp.is" in clip:
        id = clip.split("hyp.is/")[1].split("/")[0]
        return id
    elif "annotations:" in clip:
        id = clip.split("annotations:")[1]
        return id
    else:
        return "G1VksG9WEeqdsytzMIjmww"


# get id from clipboard
highlight_id = parse_clipboard_link()

h = get_highlight(HYPOTHESIS_TOKEN, highlight_id)
username = HYPOTESIS_USER
date = h[4]
highlight = h[0]
annotation = h[1]
url = h[5]
hiccup = create_hiccup(username, date, url, user_url=HYPOTHESIS_USER_URL, highlight=highlight, annotation=annotation)


# sys.stdout.write(hiccup)  # send to alfred
print(str(hiccup.encode('utf-8').strip()))

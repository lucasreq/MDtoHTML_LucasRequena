import re
import os
from shutil import copyfile

def extract_md(file_n,path):
    files = open(path+'\\'+ file_n ,"r",encoding="utf-8")
    txt_lines = files.readlines()
    files.close()
    return txt_lines

class Searcher:
    def __init__(self, text_lines):
        self.text_lines = text_lines
        self.groups = None

    def __contains__(self, regex):
        match = re.search(regex, self.text_lines)
        if match:
            self.groups = match.groups()
        else:
            self.groups = None
        return bool(match)

    def __getitem__(self, index):
        return self.groups[index]


def html_files(txt_lines,path,file_n):
    file = open(path+'\\'+ file_n[:-3] + ".html",encoding="utf-8")
    for t in txt_lines:
        file.write(t + '\n')


def titles(txt_lines):

    result = []
    if '([#]+)(\s*)(w.*)' in txt_lines:
        result.append('<h3>' + txt_lines[3:] + ' ' + '</h3>')

    elif '([##]+)(\s*)(w.*)' in txt_lines:
        result.append('<h2>' + txt_lines[2:] + ' ' + '</h2>')

    elif '([###]+)(\s*)(w.*)' in txt_lines:
        result.append('<h1>' + txt_lines[1:] + ' ' + '</h1>')

    return result

def link(txt_lines):

    result = []
    if 'http://' in txt_lines:
        result.append('<a href=' + txt_lines + '">' + txt_lines + '</a>')

    elif 'https://' in txt_lines:
        result.append('<a href=' + txt_lines + '">' + txt_lines + '</a>')
    return result

def important(txt_lines):

    result = []
    if '([**]+)(\s*)(w.*)' in txt_lines:
        result.append('<strong>' + txt_lines + '</strong>')

    elif '([*]+)(\s*)(w.*)' in txt_lines:
        result.append('<em>' + txt_lines + '</em>')
    return result

def italic(txt_lines):

    result = []
    if '_' in txt_lines:
        result.append('<i>' + txt_lines + '</i>')
    return result

def text(txt_lines):

    result = []
    if '(^.+)' in txt_lines:
        result.append('<p>' + txt_lines + '</p>')
    else:
        result.append('<br>')
    return result


def addTemplate(template, output):
    for file in os.listdir(template):
        copyfile(template+'\\'+ file, output+'\\'+file)


def convert(path, file_n, output,txt_lines):
    txt_lines = extract_md(path, file_n)
    txt_lines = titles(txt_lines)
    txt_lines = important(txt_lines)
    txt_lines = link(txt_lines)
    txt_lines = italic(txt_lines)
    txt_lines = text(txt_lines)
    html_files(txt_lines, output, file_n)


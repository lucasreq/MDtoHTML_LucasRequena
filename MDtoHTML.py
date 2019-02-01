#em = "<em>"
#s_em = "</em>"
#strong = "<strong>"
#s_strong = "</strong>"
#p = '<p>'
#s_p = '</p>'
#h1 = '<h1>'
#h2 = '<h2>'
#h3 = '<h3>'
#link = '<a href="'
#s_link = '">'
#ss_link = '</a>'
#ul = '<ul>'
#li = '<li>'

import re


def extract_md(file_n,path):
    file = open(path+'\\'+ filename ,"r",encoding="utf-8")
    txt_lines = file.readlines()
    files.close()
    return txt_lines

def html_files(file_n,path,txt_lines):
    file = open(path+'\\'+ filename[:-3] + ".html",encoding="utf-8")
    for t in txt_lines:
        file.write(t + '\n')


def titles(txt_lines):
    result = []
    if "r'^\s*[#]{3}'" in txt:
        result.append('<h3>' + txt[3:] + ' ' + '</h3>')

    elif "r'^\s*[#]{2}'" in txt:
        result.append('<h2>' + txt[2:] + ' ' + '</h2>')

    elif "r'^\s*[#]{1}" in txt:
        result.append('<h1>' + txt[1:] + ' ' + '</h1>')
    return result

def link(txt_lines):
    result = []
    if 'http://' in txt:
        result.append('<a href=' + txt + '">' + txt + '</a>')

    elif 'https://' in txt:
        result.append('<a href=' + txt + '">' + txt + '</a>')
    return result

def important(txt_lines):
    result = []
    if '**' in txt:
        result.append('<strong>' + txt + '</strong>')

    elif '*' in txt:
        result.append('<em>' + txt + '</em>')
    return result

def italic(txt_lines):
    result = []
    if '_' in txt:
        result.append('<i>' + txt + '</i>')
    return result

def text(txt_lines):
    result = []
    if txt in txt:
        result.append('<p>' + txt + '</p>')
    else:
        result.append('<br>')
    return result

def addTemplate(template, output):
    for file in os.listdir(template):
        copyfile(template+'\\'+file, output+'\\'+file)

def convert(path, file_n, output):
    content = extract_md(path, file_n)
    content = titles(txt_lines)
    content = important(txt_lines)
    content = link(txt_lines)
    content = italic(txt_lines)
    content = text(txt_lines)
    writeFile(txt_lines, output, file_n)


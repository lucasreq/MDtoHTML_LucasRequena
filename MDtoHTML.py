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

def extract_md(file_n,path):
    file = open(path+'\\'+ filename ,"r",encoding="utf-8")
    txt_lines = file.readlines()
    files.close()
    return txt_lines

def conversion_files(file_n,path,txt_lines):
    file = open(path+'\\'+ filename[:-3] + ".html",encoding="utf-8")
    for c in txt_lines:
        file.write(c + '\n')



def Titles(txt_lines):
    result = []
    if '###' in txt:
        result.append('<h3>' + txt[3:] + ' ' + '</h3>')

    elif '##' in txt:
        result.append('<h2>' + txt[2:] + ' ' + '</h2>')

    elif '#' in txt:
        result.append('<h1>' + txt[1:] + ' ' + '</h1>')
    return result

def web(txt_lines):
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

def text(txt_lines):
    result = []
    if txt in txt:
        result.append('<p>' + txt + '</p>')
    else:
        result.append('<br>')
    return result


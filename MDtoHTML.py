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





txt = ''

def Titles(txt_lines):
    if '###' in txt:
        print('<h3>' + txt[3:] + ' ' + '</h3>')

    elif '##' in txt:
        print('<h2>' + txt[2:] + ' ' + '</h2>')

    elif '#' in txt:
        print('<h1>' + txt[1:] + ' ' + '</h1>')

def web(txt_lines):
    if 'http://' in txt:
    print('<a href=' + txt + '">' + txt + '</a>')

    elif 'https://' in txt:
        print('<a href=' + txt + '">' + txt + '</a>')

def important(txt_lines):
    if '**' in txt:
        print('<strong>' + txt + '</strong>')

    elif '*' in txt:
        print('<em>' + txt + '</em>')
def text(txt_lines):
    if txt in txt:
        print('<p>' + txt + '</p>')
    else:
        print('<br>')


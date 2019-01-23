



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

txt = ''

if '###' in txt:
    print('<h3>' + txt[3:] + ' ' + '</h3>')

elif '##' in txt:
    print('<h2>' + txt[2:] + ' ' + '</h2>')

elif '#' in txt:
    print('<h1>' + txt[1:] + ' ' + '</h1>')


if 'http://' in txt:
    print('<a href=' + txt + '">' + txt + '</a>')

elif 'https://' in txt:
    print('<a href=' + txt + '">' + txt + '</a>')

if '**' in txt:
    print('<strong>' + txt + '</strong>')

elif '*' in txt:
    print('<em>' + txt + '</em>')

if txt in txt:
    print('<p>' + txt + '</p>')
else:
    print('<br>')


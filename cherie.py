def biefait(jina):
    t=input(jina+' nipe ripoti yako:')
    return t


R={'AIME':11,'SIFA':20,'MUSUBAO':15,'JULLY':5}
S=R.get('AIME',0)                                      #'MUTU HUYU HAYALETA RIPOTI'

if S :
    print('aime alileta ripoti ya saa ',S)
else:
    print('aime hakuleta ripoti')
    print("sasa aime ameripoti saa ",biefait('aime'))
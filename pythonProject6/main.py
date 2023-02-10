import re

def transforme(text):
    def replace(x):
        hastag= x.group()
        link= f'<a href="https://www.instagram.com/seach?q=#{hastag[1:]}">{hastag}</a>'
        return link
    return re.sub(r'#\w+',replace,text)

text= 'bidof #jders fdafda #asdffdas. fda'
result= transforme(text)
print(result)
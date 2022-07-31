import re
import sys

ans = []
buf = sys.argv[1]
buf = buf.replace("101", "16")
buf = buf.replace("102", "26")
buf = buf.replace("103", "36")
lis = re.split('(..)',buf)[1::2]
print(lis)
hiragana = ["あいうえお", "かきくけこ", "さしすせそ", "たちつてと", "なにぬねの", "はひふへほ", "まみむめも", "やゆよ", "らりるれろ", "わをん", "がぎぐげご", "ざじずぜぞ", "だぢづでど", "ばびぶべぼ", "ぱぴぷぺぽ", "。ー!?@", "12345", "67890", "、:・_", "アイウエオ", "カキクケコ", "サシスセソ", "タチツテト", "ナニヌネノ", "ハヒフヘホ", "マミムメモ", "ヤユヨ", "ラリルレロ", "ワヲン", "ガギグゲゴ", "ザジズゼゾ", "ダヂヅデド", "バビブベボ", "パピプペポ", "ぁぃぅぇぉ", "っゎゃゅょ", "ァィゥェォ", "ッヮャュョ", "ヵヶ"]
for i in range(len(lis)):
    if lis[i] == "16":
        print(lis[i], hiragana[9][0])
        ans.append(hiragana[9][0])
    elif lis[i] == "26":
        print(lis[i], hiragana[9][1])
        ans.append(hiragana[9][1])
    elif lis[i] == "36":
        print(lis[i], hiragana[9][2])
        ans.append(hiragana[9][2])
    #elif lis[i]
# = ~ ^
    elif re.match("^-\d$", lis[i]) != None:
        print(lis[i], hiragana[10][int(lis[i].replace("-", ""))-1])
        ans.append(hiragana[10][int(lis[i].replace("-", ""))-1])
    elif re.match("^\d-$", lis[i]) != None:
        print(lis[i], hiragana[11][int(lis[i].replace("-", ""))-1])
        ans.append(hiragana[11][int(lis[i].replace("-", ""))-1])
    elif re.match("^\=\d$", lis[i]) != None:  
        print(lis[i], hiragana[12][int(lis[i].replace("=", ""))-1])
        ans.append(hiragana[12][int(lis[i].replace("=", ""))-1])
    elif re.match("^\d\=$", lis[i]) != None:
        print(lis[i], hiragana[13][int(lis[i].replace("=", ""))-1])
        ans.append(hiragana[13][int(lis[i].replace("=", ""))-1])
    elif re.match("^~\d$", lis[i]) != None:
        print(lis[i], hiragana[14][int(lis[i].replace("~", ""))-1])
        ans.append(hiragana[14][int(lis[i].replace("~", ""))-1])
    elif re.match("^\d~$", lis[i]) != None:
        print(lis[i], hiragana[15][int(lis[i].replace("~", ""))-1])
        ans.append(hiragana[15][int(lis[i].replace("~", ""))-1])
    elif re.match("^\^\d$", lis[i]) != None:
        print(lis[i], hiragana[16][int(lis[i].replace("^", ""))-1])
        ans.append(hiragana[16][int(lis[i].replace("^", ""))-1])
    elif re.match("^\d\^$", lis[i]) != None:
        print(lis[i], hiragana[17][int(lis[i].replace("^", ""))-1])
        ans.append(hiragana[17][int(lis[i].replace("^", ""))-1])
    elif re.match("^\:\d$", lis[i]) != None:
        print(lis[i], hiragana[18][int(lis[i].replace(":", ""))-1])
        ans.append(hiragana[18][int(lis[i].replace(":", ""))-1])
    elif re.match("^\d\:$", lis[i]) != None:
        print(lis[i], hiragana[19][int(lis[i].replace(":", ""))-1])
        ans.append(hiragana[19][int(lis[i].replace(":", ""))-1])
    elif re.match("^\+\d$", lis[i]) != None:
        print(lis[i], hiragana[20][int(lis[i].replace("+", ""))-1])
        ans.append(hiragana[20][int(lis[i].replace("+", ""))-1])
    elif re.match("^\d\+$", lis[i]) != None:
        print(lis[i], hiragana[21][int(lis[i].replace("+", ""))-1])
        ans.append(hiragana[21][int(lis[i].replace("+", ""))-1])
    elif re.match("^\*\d$", lis[i]) != None:
        print(lis[i], hiragana[22][int(lis[i].replace("*", ""))-1])
        ans.append(hiragana[22][int(lis[i].replace("*", ""))-1])
    elif re.match("^\d\*$", lis[i]) != None:
        print(lis[i], hiragana[23][int(lis[i].replace("*", ""))-1])
        ans.append(hiragana[23][int(lis[i].replace("*", ""))-1])
    elif re.match("^\#\d$", lis[i]) != None:
        print(lis[i], hiragana[24][int(lis[i].replace("#", ""))-1])
        ans.append(hiragana[24][int(lis[i].replace("#", ""))-1])
    elif re.match("^\d\#$", lis[i]) != None:
        print(lis[i], hiragana[25][int(lis[i].replace("#", ""))-1])
        ans.append(hiragana[25][int(lis[i].replace("#", ""))-1])
    elif re.match("^\[\d$", lis[i]) != None:
        print(lis[i], hiragana[26][int(lis[i].replace("[", ""))-1])
        ans.append(hiragana[26][int(lis[i].replace("[", ""))-1])
    elif re.match("^\d\[$", lis[i]) != None:
        print(lis[i], hiragana[27][int(lis[i].replace("[", ""))-1])
        ans.append(hiragana[27][int(lis[i].replace("[", ""))-1])
    elif re.match("^\]\d$", lis[i]) != None:
        print(lis[i], hiragana[28][int(lis[i].replace("]", ""))-1])
        ans.append(hiragana[28][int(lis[i].replace("]", ""))-1])
    elif re.match("^\d\]$", lis[i]) != None:
        print(lis[i], hiragana[29][int(lis[i].replace("]", ""))-1])
        ans.append(hiragana[29][int(lis[i].replace("]", ""))-1])
    elif re.match("^\.\d$", lis[i]) != None:
        print(lis[i], hiragana[30][int(lis[i].replace(".", ""))-1])
        ans.append(hiragana[30][int(lis[i].replace(".", ""))-1])
    elif re.match("^\d\.$", lis[i]) != None:
        print(lis[i], hiragana[31][int(lis[i].replace(".", ""))-1])
        ans.append(hiragana[31][int(lis[i].replace(".", ""))-1])
    elif re.match("^\,\d$", lis[i]) != None:
        print(lis[i], hiragana[32][int(lis[i].replace(",", ""))-1])
        ans.append(hiragana[32][int(lis[i].replace(",", ""))-1])
    elif re.match("^\d\,$", lis[i]) != None:
        print(lis[i], hiragana[33][int(lis[i].replace(",", ""))-1])
        ans.append(hiragana[33][int(lis[i].replace(",", ""))-1])
    elif re.match("^a\d$", lis[i]) != None:
        print(lis[i], hiragana[34][int(lis[i].replace("a", ""))-1])
        ans.append(hiragana[34][int(lis[i].replace("a", ""))-1])
    elif re.match("^\da$", lis[i]) != None:
        print(lis[i], hiragana[35][int(lis[i].replace("a", ""))-1])
        ans.append(hiragana[35][int(lis[i].replace("a", ""))-1])
    elif re.match("^b\d$", lis[i]) != None:
        print(lis[i], hiragana[36][int(lis[i].replace("b", ""))-1])
        ans.append(hiragana[36][int(lis[i].replace("b", ""))-1])
    elif re.match("^\db$", lis[i]) != None:
        print(lis[i], hiragana[37][int(lis[i].replace("b", ""))-1])
        ans.append(hiragana[37][int(lis[i].replace("b", ""))-1])
    elif re.match("^c\d$", lis[i]) != None:
        print(lis[i], hiragana[38][int(lis[i].replace("c", ""))-1])
        ans.append(hiragana[38][int(lis[i].replace("c", ""))-1])
    elif re.match("^\dc$", lis[i]) != None:
        print(lis[i], hiragana[39][int(lis[i].replace("c", ""))-1])
        ans.append(hiragana[39][int(lis[i].replace("c", ""))-1])
    else:
        print(lis[i], hiragana[int(lis[i][0])-1][int(lis[i][1])-1])
        ans.append(hiragana[int(lis[i][0])-1][int(lis[i][1])-1])

print("\ndecrypt: ", end="")
for x in range(len(ans)):
    print(ans[x], end="")

print()

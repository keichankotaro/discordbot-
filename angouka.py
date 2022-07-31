import re
import sys

ans = []
buf = sys.argv[1]
buf = list(buf)
print(buf)
hiragana = ["あいうえお", "かきくけこ", "さしすせそ", "たちつてと", "なにぬねの", "はひふへほ", "まみむめも", "やゆよ", "らりるれろ", "わをん", "がぎぐげご", "ざじずぜぞ", "だぢづでど", "ばびぶべぼ", "ぱぴぷぺぽ", "。ー!?@", "12345", "67890", "、:・_", "アイウエオ", "カキクケコ", "サシスセソ", "タチツテト", "ナニヌネノ", "ハヒフヘホ", "マミムメモ", "ヤユヨ", "ラリルレロ", "ワヲン", "ガギグゲゴ", "ザジズゼゾ", "ダヂヅデド", "バビブベボ", "パピプペポ", "ぁぃぅぇぉ", "っゎゃゅょ", "ァィゥェォ", "ッヮャュョ", "ヵヶ"]

for x in range(len(buf)):
    y = 0
    for y in range(39):
        try:
            if int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 111 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 120:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "-" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 121 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 130:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "-"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 131 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 140:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "=" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 141 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 150:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "="
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 151 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 160:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "~" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 161 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 170:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "~"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 171 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 180:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "^" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 181 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 190:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "^"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 191 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 200:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = ":" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 201 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 210:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + ":"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 211 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 220:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "+" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 221 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 230:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "+"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 231 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 240:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "*" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 241 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 250:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "*"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 251 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 260:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "#" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 261 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 270:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "#"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 271 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 280:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "[" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 281 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 290:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "["
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 291 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 300:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "]" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 301 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 310:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "]"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 311 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 320:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "." + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 321 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 330:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "."
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 331 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 340:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "," + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 341 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 350:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + ","
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 351 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 360:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "a" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 361 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 370:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "a"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 371 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 380:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "b" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 381 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 390:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "b"
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 391 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 400:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = "c" + lst[-1]
                ans.append(num)
            elif int(str(y+1)+str((hiragana[y].index(buf[x])+1))) >= 401 and int(str(y+1)+str((hiragana[y].index(buf[x])+1))) < 410:
                lst = list(str(str(y+1)+str(hiragana[y].index(buf[x])+1)))
                num = lst[-1] + "c"
                ans.append(num)
            else:
                num = y + 1
                ans.append(str(num)+str((hiragana[y].index(buf[x])+1)))
        except ValueError:
            continue

print("encrypt: ", end="")
for i in range(len(ans)):
    print(ans[i], end="")
print()

from opencc import OpenCC

cc = OpenCC('t2s')
print(cc.convert(u'Open Chinese Convert（OpenCC）「開放中文轉換」，是一個致力於中文簡繁轉換的項目，提供高質量詞庫和函數庫(libopencc)。'))
s = 'Open Chinese Convert（OpenCC）「開放中文轉換」'
print(cc.convert(s))
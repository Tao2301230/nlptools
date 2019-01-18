import pypinyin
from pypinyin import pinyin, lazy_pinyin, Style

pinyin(u'中心')
pinyin(u'中心', strict=False)
pinyin(u'下雨天', strict=False)
pinyin(u'下雨天', strict=False, style='NORMAL')
lazy_pinyin(u'下雨天', strict=False, style='NORMAL')
lazy_pinyin(u'下雨天', strict=False, style=pypinyin.NORMAL)
s = '法轮功'
print(''.join(lazy_pinyin(s, strict=False, style=pypinyin.NORMAL)))


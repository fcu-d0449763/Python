import re
re_str = r'\d+[.]\d+|[1-9]\d*'
print(re.fullmatch(re_str,'abc12.5hhh60,30.2kkk9nn0.12'))
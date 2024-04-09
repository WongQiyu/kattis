# def playlist(songs):
#     final = 0
#     counter = [0] * 60
#     for item in songs:
#         val = item % 60
#         final += counter[60-val] if val > 0 else counter[0]
#         counter[val] += 1
#     return final
#
# if __name__ == '__main__':
#     n = int(input())
#     songs = []
#     for _ in range(n):
#         songs.append(int(input()))
#     print(playlist(songs))
n = int(input())
text = []
for _ in range(n):
    text.append(input())

checker = set()
result = []
for item in text:
    item = item.strip()
    nice = ''.join(sorted(item))
    if nice not in checker:
        checker.add(nice)
        result.append(item)
print(sorted(result))
# import math
# import os
# import random
# import re
# import sys
# def funWithAnagrams(text):
#     checker = set()
#     result = []
#     for item in text:
#         item = item.strip()
#         nice = ''.join(sorted(item))
#         if nice not in checker:
#             checker.add(nice)
#             result.append(item)
#     return result
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     text_count = int(input().strip())
#
#     text = []
#
#     for _ in range(text_count):
#         text_item = input()
#         text.append(text_item)
#
#     result = funWithAnagrams(text)
#
#     fptr.write('\n'.join(result))
#     fptr.write('\n')
#
#     fptr.close()
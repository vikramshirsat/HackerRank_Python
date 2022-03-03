'''
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.

Constraints:
1<=n<=10^5

The sum of the lengths of all the words do not exceed 10^6
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, n.
The next n lines each contain a word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
d=OrderedDict()
n=int(input())
for i in range(n):
    s=input()
    if s in d.keys():
        d[s]+=1
    else:
        d[s]=1
print(len(d.keys()))
print(' '.join([str(d[k]) for k in d.keys()]))
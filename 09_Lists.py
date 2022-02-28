'''
Consider a list (list = []). You can perform the following commands:

     1. insert i e: Insert integer e at position i.
     2. print: Print the list.
     3. remove e: Delete the first occurrence of integer e .
     4. append e: Insert integer e at the end of the list. 
     5. sort: Sort the list.
     6. pop: Pop the last element from the list.
     7. reverse: Reverse the list
.
      Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 
      7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example:
    N=4
    append 1
    append 2
    insert 3 1
    print
            1. append 1: Append 1 to the list, arr=[1].
            2. append 2 :append 2 to the list, arr=[1,2]
            3. insert 3 1: Insert 3 at insex 1  , arr=[1,3,2]
            4. print: print the array

Output:
        [1, 3, 2]

Input Format:
        The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints:
         The elements added to the list must be integers.

Output Format:
         For each command of type print, print the list on a new line.
'''

if __name__ == '__main__':
    N = int(input())
    command=[]
    for i in range(N):
        command.append(input().split())

    result=[]
    for i in range(N):
        if command[i][0]=='insert':
            result.insert(int(command[i][1]),int(command[i][2]))
        elif command[i][0]=='print':
            print(result)
        elif command[i][0]=='remove':
            result.remove(int(command[i][1]))
        elif command[i][0]=='append':
            result.append(int(command[i][1]))
        elif command[i][0]=='pop':
            result.pop()
        elif command[i][0]=='sort':
            result.sort()
        elif command[i][0]=='reverse':
            result.reverse()

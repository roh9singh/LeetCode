'''
						Longest Absolute File Path


Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory 
subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. 
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:

    The name of a file contains at least a . and an extension.
    The name of a directory or sub-directory will not contain a ..

Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

Subscribe to see which companies asked this question

'''


class Solution(object):
    def lengthLongestPath(self, input):
        x=input.split("\n")

        levels=[0]*len(x)
        files=[0]*len(x)
        directories=[0]*len(x)   


        for i in range(len(x)):
            levels[i]=x[i].count('\t')

            if x[i].count('.')>=1:
                files[i]=1
                directories[i]=-1
            else:
                files[i]=-1
                directories[i]=1


        for i in range(len(x)):
            x[i]=x[i].replace("\t","")


        '''i=-1
        j=-1

        for l in range(len(levels)):
            if levels[l]>=j and files[l]==1:
                if i!=-1 and len(x[l])<len(x[i]):
                    continue 
                else:
                    i=l
                    j=levels[i]'''

        #i=levels.index(max(levels))
        #j=levels[i]

        #print(i,j)

        output=""

        


        for k in range(len(files)):
            temp=""
            if files[k]==1:
                i=k
                j=levels[i]
            else:
                continue

            while i>=0:
                if (levels[i]==j):
                    temp="/"+x[i]+temp
                    j=j-1

                i=i-1

            if len(temp)>len(output):
                output=temp


        print (levels)
        print (files)
        print (directories)


        return (output[1:len(output)])



c=Solution()

print(c.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(c.lengthLongestPath("a.tar.gz"))
print(c.lengthLongestPath("dir\n\t        file.txt\n\tfile2.txt"))
print(c.lengthLongestPath("a\n\taa\n\t\taaa\n\t\t\tfile1.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png"))


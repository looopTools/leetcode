# Solution versus Solution take two

## Solution

The first attempted solution simply utiise the generally classic approach.
Here you utilze a tmp value to store one of the values to swap after which one index is update to the other and then temp is stored in the none updated index.

**General Idea**

'''
tmp <- l[i]
l[i] <- l[j]
l[j] <- tmp
'''

## Solution Take Two

Here we utilize XOR to avoid use the tmp value.
We levaerage that a XOR b xor a == b

So that l[i] = l[i] XOR l[j] means that l[i] contains both the value of l[i] and l[j]
then l[j] = l[i] XOR l[j] now l[j] contians the original value of l[i].
Finally l[i] = l[i] XOR l[j] and now l[i] contains the original value of l[j]

## Results

BAsed on leetcode execution Solution one has a better runtime than Take two.
However, take two has a slightly better memory consumption. 
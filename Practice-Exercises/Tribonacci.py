

#The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.
#Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.
    #Your function should handle sequences of any length greater than or equal to zero.
    #If the length is zero, return an empty array.
    #Note that the starting numbers are part of the sequence.

def tribonacci_sequence(start_sequence,length):
    if length<=3 and length>0:
        return start_sequence[0:length];
    elif length==0:
        return [];
    else:
        for index in range(3,length):
            start_sequence.append(sum(start_sequence[index-3:index])) #sum from 3 to 3
        return start_sequence
    

#test
print(tribonacci_sequence([0,0,1],20))
print(tribonacci_sequence([21,32,43],1))
print(tribonacci_sequence([0,0,1],0))
print(tribonacci_sequence([10,20,30],2))
print(tribonacci_sequence([10,20,30],3))
print(tribonacci_sequence([123,456,789],8))
print(tribonacci_sequence([1,2,3],12))


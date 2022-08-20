# Bitmap Holes
# Have the function BitmapHoles(strArr) take the array of strings stored in strArr,
#  which will be a 2D matrix of 0 and 1's, and determine how many holes, or contiguous regions of 0's,
#  exist in the matrix. A contiguous region is one where there is a 
# connected group of 0's going in one or more of four directions: up, down, 
# left, or right. For example: if strArr is ["10111", "10101", "11101", "11111"], 
# then this looks like the following matrix:

# 1 0 1 1 1
# 1 0 1 0 1
# 1 1 1 0 1
# 1 1 1 1 1

# For the input above, your program should return 2 because there are two separate contiguous regions of 0's, which create "holes" in the matrix. You can assume the input will not be empty.
# Examples
# Input: ["01111", "01101", "00011", "11110"]
# Output: 3
# Input: ["1011", "0010"]
# Output: 2
###################################################################################################





def BitmapHoles(strArr):
  # code goes here
  arr = []
  for i in range(len(strArr)):
    arr.append(list(strArr[i]))

  arrCunt=[]
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      count =0
      count1=0
      
      if arr[i][j] == "0":
        for k in range(j,len(arr[i])):
         
          if arr[i][k] == "0":
            
            count = count + 1
          else:
            break

        for l in range(j,len(arr)):
         
          if arr[l][j] =="0":
           
            count1 = count1+1
          else:
            break

      if count>count1:
        arrCunt.append(count)

      elif count1>0:
        arrCunt.append(count1)

  arrCunt.sort()
  return arrCunt[-1]


str = ["01111", "01101", "00011", "11110"]
print(BitmapHoles(str))
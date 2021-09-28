# Build Array from Permutation
from  collections import defaultdict

# Build Array from Permutation
def buildArray(nums):
  n = len(nums)
  output = [None] * n
  for i in range(n):
    output[i] = nums[nums[i]]
  
  return output

# Concatenation of Array
def getConcatenation(nums):
  n = len(nums)
  output = [0] * (2 * n)
  for i in range(2 * n):
      output[i] = nums[i % n]
  
  return output

# Running Sum of 1d Array
def runningSum(nums):
  n = len(nums)
  for i in range(1, n):
    nums[i] = nums[i - 1] + nums[i]
  return nums

# Richest Customer Wealth
def maximumWealth(accounts):
  ROWS, COLS = len(accounts), len(accounts[0])
  maxCustomerSum = float("-inf")
  for row in range(ROWS):
    maxCustomerSum = max(maxCustomerSum, sum(accounts[row]))

  return maxCustomerSum

# Shuffle the Array
def shuffle(nums, n):
  i, j = 0, n
  output = []
  while(i < n):
    output.append(nums[i])
    output.append(nums[j])
    i += 1
    j += 1
  
  return output

# Shuffle the Array
def shuffle2(nums, n):
  i, j = n - 1, len(nums) - 1

  while( i >= 0):
    nums[j] <<= 10
    nums[j] |= nums[i]

    i -= 1
    j -= 1

  i, j = 0, n


  while ( j < len(nums)):
    num1 = nums[j] & 1023
    num2 = nums[j] >> 10
    nums[i] = num1
    nums[i + 1] = num2
    i += 2
    j += 1

  return nums

# Kids With the Greatest Number of Candies
def kidsWithCandies(candies, extraCandies):
  maximum = max(candies)
  output = [False] * len(candies)
  for i, num in enumerate(candies):
    if num + extraCandies >= maximum:
      output[i] = True

  return output

# Number of Good Pairs
def numIdenticalPairs(nums):
  mapping = defaultdict(int)
  for num in nums:
    mapping[num] += 1
  
  count = 0
  for key, value in mapping.items():
    count += value * (value - 1) / 2
  
  return count

# How Many Numbers Are Smaller Than the Current Number
def smallerNumbersThanCurrent(nums):
  mapping = {}
  for i, num in enumerate(sorted(nums)):
    mapping.setdefault(num, i)
  
  output =  [mapping[num] for num in nums]
  
  return output

# Check if the Sentence Is Pangram
def checkIfPangram(sentence):
  count = [0] * 26
  for ch in sentence:
    index = ord(ch) - ord('a')
    count[index] += 1

  for i in range(len(count)):
    if count[i] < 1:
      return False

  return True

# Count Items Matching a Rule
def countMatches(items, ruleKey, ruleValue):
  def matches(rule, item):
    ruleKey, ruleValue = rule
    
    itemType, color, name = item
    
    return (ruleKey == "type" and ruleValue == itemType) or (ruleKey == "color" and ruleValue == color) or (ruleKey == "name" and ruleValue == name)
        
        
  rule = (ruleKey, ruleValue)
  count = 0
  
  for item in items:
    if matches(rule, item):
      count += 1
  
  return count

# Find the Highest Altitude
def largestAltitude(gain):
  highest = 0
  total = 0
  
  for num in gain:
    total += num
    highest = max(highest, total)
  
  return highest

# Flipping an Image
def flipAndInvertImage(image):
  ROWS, COLS = len(image), len(image[0])

  for row in range(ROWS):
    for col in range(COLS // 2):
      image[row][col], image[row][COLS - col - 1]  = image[row][COLS - col - 1], image[row][col]
    for col in range(COLS):
      image[row][col] = 1 if image[row][col] == 0 else 0
  
  return image

# Matrix Diagonal Sum
def diagonalSum(mat):
  ROWS, COLS = len(mat), len(mat[0])
  total = 0
  for row in range(ROWS):
    for col in range(COLS):
      
      if row + col == ROWS - 1:
        total += mat[row][col]
        continue
      
      if row - col == 0:
        total += mat[row][col]
        continue
    
  return total

# Find Numbers with Even Number of Digits
def findNumbers(nums):
  count = 0
  for num in nums:
    if len(str(num)) % 2 == 0:
      count += 1
  
  return count

# Transpose Matrix
def transpose(matrix):
  ROWS, COLS = len(matrix), len(matrix[0])
  output = []
  for col in range(COLS):
    rowValues = []
    for row in range(ROWS):
      rowValues.append(matrix[row][col])
    output.append(rowValues)
  return output

# Add to Array-Form of Integer
def addToArrayForm(num, k):
  firstNum = int(''.join(map(str, num)))
  total = firstNum + k
  n = len(str(total))
  i = n - 1
  output = [0] * n
  
  while i>= 0:
    output[i] = total % 10
    total = total // 10
    i -= 1
  
  return output

# Maximum Population Year
def maximumPopulation(logs):
  population = defaultdict(int)
  for birth, death in logs:
    year = birth
    while year < death:
      population[year] += 1
      year += 1
      
  largestPopulation = 0
  yearWithLargestPopulation = float("-inf")
  
  for year, people in population.items():
    if people > largestPopulation:
      largestPopulation = people
      yearWithLargestPopulation = year 
    
    elif people == largestPopulation and year < yearWithLargestPopulation:
      yearWithLargestPopulation = year
      
  return yearWithLargestPopulation

# Determine Whether Matrix Can Be Obtained By Rotation
def findRotation(mat, target):
  def equal(matrix1, matrix2):
    ROWS, COLS = len(matrix1), len(matrix1[0])
          
    for row in range(ROWS):
      for col in range(COLS):
        if matrix1[row][col] != matrix2[row][col]:
          return False
    
    return True
    
  
  if mat == target:
    return True
  
  ROWS, COLS = len(mat), len(mat[0])
  temp = [[ 0 for _ in range(COLS)] for _ in range(ROWS)]
        
        
  for i in range(4):
    for row in range(ROWS):
      for col in range(COLS):
        temp[col][COLS - row - 1] = mat[row][col]
    
    if equal(temp, target):
      return True
    
    mat = [[ temp[i][j] for j in range(COLS)] for i in range(ROWS)]
    
  
  
  return False

# Two Sum
def twoSum( nums, target):
  seen = {}
  for i, num in enumerate(nums):
      if target - num in seen:
          return [seen[target - num], i]
      seen[num] = i
  return [-1, -1]

# Find N Unique Integers Sum up to Zero
def sumZero(n):
  output = []
  for i in range(n):
    output.append(i * 2 - n + 1)
  return output

# Saddle Point In Matrix
def luckyNumbers(matrix):
  mi = [min(row) for row in matrix]
  mx = [max(col) for col in zip(*matrix)]
  
  return [cell for i, row in enumerate(matrix) for j, cell in enumerate(row) if mi[i] == mx[j]]

# Maximum Subarray
def maxSubArray(nums):
  if len(nums) == 1:
      return nums[0]
  
  maxSum = nums[0]
  maxSumSoFar = nums[0]
  for i in range(1, len(nums)):
      num = nums[i]
      maxSum = max(num, num + maxSum)
      maxSumSoFar = max(maxSum, maxSumSoFar)
  
  return maxSumSoFar

# Reshape the Matrix
def matrixReshape( mat, r, c):
  if len(mat) == 0 or  (r * c) != len(mat) * len(mat[0]):
    return mat
  count = 0
  result = [[None for _ in range(c) ] for _ in range(r)]

  for row in range(len(mat)):
    for col in range(len(mat[0])):
      result[count // c][count % c] = mat[row][col]
      count += 1

  return result


# print(buildArray([0,2,1,5,3,4])) 
# print(getConcatenation([1,2,1]))
# print(runningSum([1,2,3,4]))
# print(maximumWealth([[1,2,3],[3,2,1]]))
# print(shuffle([1,2,3,4,4,3,2,1], 4))
# print(kidsWithCandies([2,3,5,1,3], 3))
# print(numIdenticalPairs([1,2,3,1,1,3]))
# print(smallerNumbersThanCurrent([8,1,2,2,3]))
# print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
# print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], 'color', 'silver'))
# print(largestAltitude([-5,1,5,0,-7]))
# print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]));
# print(diagonalSum([[1,2,3],
#               [4,5,6],
#               [7,8,9]]))
# print(findNumbers([12,345,2,6,7896]))

# print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
# print(addToArrayForm([1,2,0,0], 34))

# print(maximumPopulation([[1993,1999],[2000,2010]]))

# print(findRotation([[0,1],[1,0]], [[1,0],[0,1]]))

# print(twoSum([2,7,11,15], 9))
# print(sumZero(4))
# print(matrixReshape([[1,2],[3,4]], 1, 4))



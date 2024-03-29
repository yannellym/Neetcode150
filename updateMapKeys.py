Codewriting

You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.
To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.

Example

For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be solution(queryType, query) = 5.

The hashmap looks like this after each query:

1 query: {1: 2}
2 query: {1: 2, 2: 3}
3 query: {1: 4, 2: 5}
4 query: {2: 4, 3: 5}
5 query: answer is 5
The result of the last get query for 3 is 5 in the resulting hashmap.



# For queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] and query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]], the output should be solution(queryType, query) = 6.

# The hashmap looks like this after each query:

# 1 query: {1: 2}
# 2 query: {1: 4}
# 3 query: answer is 4
# 4 query: {1: 4, 2: 3}
# 5 query: {2: 4, 3: 3}
# 6 query: {2: 3, 3: 2}
# 7 query: answer is 2
# The sum of the results for all the get queries is equal to 4 + 2 = 6.

# Input/Output

# [execution time limit] 4 seconds (py)

# [memory limit] 1 GB

# [input] array.string queryType

# Array of query types. It is guaranteed that each queryType[i] is either "addToKey", "addToValue", "get", or "insert".

# Guaranteed constraints:
# 1 ≤ queryType.length ≤ 105.

# [input] array.array.integer query

# Array of queries, where each query is represented either by two numbers for insert query or by one number for other queries. It is guaranteed that during all queries all keys and values are in the range [-109, 109].

# Guaranteed constraints:
# query.length = queryType.length,
# 1 ≤ query[i].length ≤ 2.

# [output] integer64

# The sum of the results for all get queries.

# [Python 2] Syntax Tips

# # Prints help message to the console


class CustomHashMap:
    def __init__(self):
        self.hash_map = {}

    def insert(self, x, y):
        self.hash_map[x] = y

    def get(self, x):
        return self.hash_map.get(x, 0)

    def addToKey(self, x):
        updated_map = {}
        for key, value in self.hash_map.items():
            updated_map[key + x] = value
        self.hash_map = updated_map

    def addToValue(self, y):
        for key in self.hash_map:
            self.hash_map[key] += y

def solution(queryType, query):
    custom_hash_map = CustomHashMap()
    result_sum = 0

    for i in range(len(queryType)):
        query_type = queryType[i]
        query_args = query[i]

        if query_type == "insert":
            custom_hash_map.insert(query_args[0], query_args[1])
        elif query_type == "get":
            result_sum += custom_hash_map.get(query_args[0])
        elif query_type == "addToKey":
            custom_hash_map.addToKey(query_args[0])
        elif query_type == "addToValue":
            custom_hash_map.addToValue(query_args[0])

    return result_sum

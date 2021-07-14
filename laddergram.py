from collections import defaultdict, deque
from itertools import product

def build_graph(words):
  """Given a list of words, build a graph such that each neighbor corresponds by a difference of 1 letter"""
  buckets = defaultdict(list)
  graph = defaultdict(set)

  # Iterate over words, using _ as a placeholder for the 1 letter difference, putting matching words into buckets
  for word in words:
    for i in range(len(word)):
      bucket = word[:i] + '_' + word[i + 1:]
      buckets[bucket].append(word)
  
  # Add edges for words in the same bucket
  for bucket, neighbors in buckets.items():
    for word1, word2 in product(neighbors, repeat=2):
      if word1 != word2:
        graph[word1].add(word2)
        graph[word2].add(word1)

  return graph

def traverse(graph, starting_vertex):
  """Traverse a given graph using breadth first search, yielding each vertex and the path"""
  visited = set()
  queue = deque([[starting_vertex]])
  while queue:
    path = queue.popleft()
    vertex = path[-1]
    yield vertex, path
    for neighbor in graph[vertex] - visited:
      visited.add(neighbor)
      queue.append(path + [neighbor])

def laddergram(words, start, end):
  word_graph = build_graph(words)

  for vertex, path in traverse(word_graph, start):
    if vertex == end:
      print(' -> '.join(path))
      return len(path)
  return ""
 

# Test with valid sequence
VALID_WORDS = ["fool", "foul", "foil", "fail", "fall", "pall", "poll", "pool", "cool", "pole", "pope", "pale", "page", "sale", "sage"]
laddergram(VALID_WORDS, "fool", "sage")

# Test with invalid sequence
INVALID_WORDS = ["fool", "foul", "foil", "fail", "fall", "pink", "poll", "pool", "cool", "pong", "pope", "pale", "page", "sale", "sage"]
laddergram(INVALID_WORDS, "fool", "sage")
https://leetcode.com/problems/word-pattern/description/
https://leetcode.com/problems/word-pattern/submissions/869232093/
class Solution(object):
  def wordPattern(self, pattern, s):
      t = s.split()
#         print(map(pattern.index, pattern))
#         print(map(t.index, t))
      return [map(pattern.index, pattern)] == [map(t.index, t)]

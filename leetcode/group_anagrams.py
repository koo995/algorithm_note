class Solution:
    def groupAnagrams(self, str_arr: list[str]) -> list[list[str]]:
        from collections import defaultdict

        # 일단 그룹화가 되어야 한다. 적절한 자료구조는? dic이 어울리긴한다.
        # 아래와 같은 문자열들이 일치하는 것은 어떻게 정의하지? 당장에 드는 생각은.. 정렬이다. 문자열은 정렬이 안되니 리스트로?

        anagram_dic = defaultdict(list)
        for word in str_arr:
            sorted_word = "".join(sorted(list(word)))
            anagram_dic[sorted_word].append(word)

        print("anagram_dic: ", anagram_dic)
        grouped_anagram = list(anagram_dic.values())
        print("anagram: ", grouped_anagram)


sol = Solution()
sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

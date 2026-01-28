class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        reslen=0
        st=""
        for i in s:
            if st.find(i)==-1:
                st+=i
            else:
                st=st[st.find(i)+1:]+i
            if len(st)>reslen:
                reslen=len(st)
        return reslen
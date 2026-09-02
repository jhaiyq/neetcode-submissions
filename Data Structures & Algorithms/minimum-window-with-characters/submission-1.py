class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #idea:

        # two pointers start 0 and 1 for l and r
        # if s[l] and s[r] are not in t and we have found nothing so far we can ignore everythign to the left of r
        #so l = r + 1, r += 2
        # if one of our pointers finds 
        
        #Tells us what characters we need and their frequency
        

        if t == "":
            return ""
        
        freq, window = {}, {}
        for c in t:
            freq[c] = 1 + freq.get(c,0)
        
        have, need = 0, len(freq)
        res, resLen = [-1,1], float("infinity")
        l = 0
        for r in range((len(s))):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in freq and window[c] == freq[c]:
                have += 1
            
            while have == need:
                if (r-l + 1) < resLen:
                    res = [l, r]
                    resLen  = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have -=1
                l += 1
        l, r = res
        if resLen != float("infinity"):
            return s[l: r + 1]  
        else:
            return ""




        

        
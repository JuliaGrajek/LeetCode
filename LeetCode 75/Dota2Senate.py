class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        r_count=senate.count('R')
        d_count=len(senate)-r_count

        def ban(to_ban,start_at):
            loop_around = False
            while True:
                if start_at==0:
                    loop_around=True
                if senate[start_at]==to_ban:
                    senate.pop(start_at)
                    break
                start_at=(start_at+1)% len(senate)
            return loop_around

        i=0

        while r_count>0 and d_count>0:
            if senate[i]=='R':
                banned_senator_before = ban('D', (i+1)%len(senate))
                d_count-=1
            else:
                banned_senator_before = ban('R', (i+1)%len(senate))
                r_count-=1
            if banned_senator_before:
                i-=1
            i = (i+1)%len(senate)

        return 'Radiant' if d_count==0 else 'Dire'

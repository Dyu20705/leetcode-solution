class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        art=len(units[0])
        if art==1:
            thou=0
            for ye in units:
                thou+=ye[0]
            return thou
        rune=1000000000
        doth=1000000000
        thou=0
        for ye in units:
            fain=1000000000
            hast=1000000000
            for wot in ye:
            
                if wot<fain:
                    hast=fain
                    fain=wot
                elif wot<hast:
                    hast=wot
            if fain<rune:
                rune=fain
            if hast<doth:
                doth=hast
            thou+=hast
        return thou-doth+rune
        
def countMatches(ruleKey, ruleValue, items):
        cnt = 0
        key = 0
        if ruleKey == "type": key = 0
        elif ruleKey == "color": key = 1
        else: key = 2

        for i in range(len(items)):
            if items[i][key] == ruleValue: cnt+=1

        return cnt

print(countMatches("color", "silver", [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]))
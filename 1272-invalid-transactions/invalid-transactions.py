class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        self.amt_lim = 1000
        self.time_lim = 60
        self.trans_map = {}
        invalid_trans = set()

        for i in range(len(transactions)):
            name, time, amt, loc = transactions[i].split(",")
            if int(amt) > self.amt_lim:
                invalid_trans.add(i)
            self.trans_map[name] = self.trans_map.get(name, [])
            self.trans_map[name].append((int(time), loc, i))
        # sort the values by time
        for key, val in self.trans_map.items():
            val.sort(key=lambda x:x[0])
            l = 0
            for r in range(len(val)):
                # shrink the window if time > 60
                while (val[r][0] - val[l][0] > self.time_lim ):
                    l += 1
                for k in range(l,r):
                    if (val[k][1]!= val[r][1]):
                        invalid_trans.add(val[k][2])
                        invalid_trans.add(val[r][2])
        return [transactions[r] for r in invalid_trans]


        


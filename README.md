# double-linear-correalation
linear correalation of 4 categories plus the combination between of each categories
data.txt is example of data, the first four columns are the categories and the last one is the result
the score is from 1 to 5, and it can be devided by a space or tab

THE RESULTS:
1: const
2: cat1
2: cat1xcat2
3: cat1xcat3
4: cat1xcat4
5: cat1xncat1
6: cat1xncat2
8: cat1xncat3
9: cat1xncat4
10: cat2
11: cat2xcat3
12: cat2xcat4
13: cat2xncat1
14: cat2xncat2
15: cat2xncat3
16: cat2xncat4
17: cat3
18: cat3xcat4
19: cat3xncat1
20: cat3xncat2
21: cat3xncat3
22: cat3xncat4
23: cat4
24: cat4xncat1
25: cat4xncat2
26: cat4xncat3
27: cat4xncat4
28: ncat1
29: ncat1xncat2
30: ncat1xncat3
31: ncat1xncat4
32: ncat2
33: ncat2xncat3
34: ncat2xncat4
35: ncat3
36: ncat3xncat4
37: ncat4

WARNING!!!
With low amount of data (below 250) the model will OVERFIT. For small sample the regular linear regriossion would be more suitable

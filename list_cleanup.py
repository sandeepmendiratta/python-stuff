daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,;
09/15/17   ,Herbert Tran   ;,;   $7.29;,;
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell
;,;   $5.13   ;,; white   ;,; 09/15/17,
Myrtle Morris
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

daily_sales_split = daily_sales.replace(";,;", "+")
print(daily_sales_split)
daily_sales_split_clean = daily_sales_split.strip(",")
# print(daily_sales_split_clean)
daily_tran = []
for tran in daily_sales_split:
    daily_tran.append(tran.split("+"))
print(daily_tran)




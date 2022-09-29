import re
codes = ["4123456789123456","5123-4567-8912-3456","61234-567-8912-3456","4123356789123456","5133-3367-8912-3456","5123 - 3567 - 8912 - 3456"]
pattern = r"[456][0-9]{3}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}"
pattern2 = r"(1\-?1\-?1\-?1)|(2\-?2\-?2\-?2)|(3\-?3\-?3\-?3)|(4\-?4\-?4\-?4)|(5\-?5\-?5\-?5)|(6\-?6\-?6\-?6)|(7\-?7\-?7\-?7)|(8\-?8\-?8\-?8)|(9\-?9\-?9\-?9)|(0\-?0\-?0\-?0)"

for i in codes:
    x = re.findall(pattern,i)
    if x:
        y = re.findall(pattern2,i)
        if y:
            print("Invalid")
        else:
            print("Valid")
    else: 
        print("Invalid")
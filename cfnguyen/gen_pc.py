import string

"""
select * from c222 where random() < 0.01 limit 1;
select * from c222 limit 1

-- 20 phut- 45.435.424 record
insert into c222 (
  code
) 
select  
  '222'||code
from
  pc_template
"""
l1 =  ['2', '3', '4', '5', '6', '7', '8', '9'] + list(string.ascii_lowercase)
l2 =  ['2', '3', '4', '5', '6', '7', '8', '9'] + list(string.ascii_lowercase)
l3 =  ['2', '3', '4', '5', '6', '7', '8', '9'] + list(string.ascii_lowercase)
l4 =  ['2', '3', '4', '5', '6', '7', '8', '9'] + list(string.ascii_lowercase)
l5 =  ['2', '3', '4', '5', '6', '7', '8', '9'] + list(string.ascii_lowercase)

def x():
    c = 0
    file = open("d:\\testfile.txt","w") 
    for i1 in l1:
        for i2 in l2:
            for i3 in l3:
                for i4 in l4:
                    for i5 in l5:
                        t = "INSERT INTO public.pc_template(code) VALUES ('%s%s%s%s%s');\n"%(i1, i2, i3, i4, i5)
                        file.write(t) 
                        # print(t)
                        # c = c+1
                        # if c > 100:
                        #     return
    file.close()

x()                        

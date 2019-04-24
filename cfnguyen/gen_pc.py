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
  

-- Table: public.c222

-- DROP TABLE public.c222;

CREATE TABLE public.c222
(
    code character(8) COLLATE pg_catalog."default" NOT NULL,
    bill_id character varying(120) COLLATE pg_catalog."default",
    price character varying(50) COLLATE pg_catalog."default",
    callback_url character varying(240) COLLATE pg_catalog."default",
    status integer DEFAULT 0,
    CONSTRAINT code PRIMARY KEY (code)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.c222
    OWNER to postgres;

-- Index: c222idex

-- DROP INDEX public.c222idex;

CREATE INDEX c222idex
    ON public.c222 USING btree
    (code COLLATE pg_catalog."default")
    TABLESPACE pg_default;  
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

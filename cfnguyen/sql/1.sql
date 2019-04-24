CREATE or REPLACE FUNCTION alloc_pc(tbl char(4),  _bill_id VARCHAR(120), _price VARCHAR(50), _callback_url VARCHAR(240)) RETURNS json  AS $$
DECLARE 
  t_row c222%ROWTYPE;
  c VARCHAR(8);  
BEGIN
    EXECUTE format('select code from %s TABLESAMPLE SYSTEM(0.001)  where status=0 limit 1 for UPDATE SKIP LOCKED ;', tbl)
    INTO c;
    -- select * from c223 where status=0 ORDER BY random()  limit 1 for UPDATE  SKIP LOCKED  ;
    -- select code into c  from quote_ident(tbl)  where  random() < 0.01 and  status=0  limit 1 for UPDATE SKIP LOCKED ;
    IF c is NULL 
    THEN
        return NULL;
    ELSE	
        EXECUTE format('update %s set status = 1, bill_id=''%s'', price=''%s'', callback_url=''%s'' where code=''%s''',tbl, _bill_id, _price, _callback_url, c);
	
        -- select code into c  from c222 limit 1;
        EXECUTE format('SELECT * FROM %s where code=''%s''', tbl, c)
        INTO t_row ;
        -- SELECT * into t_row FROM c222 where code=c;
        RETURN row_to_json(t_row);
    END IF;
END;
$$ LANGUAGE plpgsql;

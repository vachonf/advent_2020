SELECT If((t1.val+t2.val+t3.val)=2020,CONCAT(t1.val,",",t2.val,",",t3.val,",","=",t1.val*t2.val*t3.val ),"") AS sumIds 
FROM new_table t1, new_table  t2, new_table t3
WHERE (t1.val+t2.val+t3.val)=2020
AND t1.val!=t2.val
GROUP BY sumIds
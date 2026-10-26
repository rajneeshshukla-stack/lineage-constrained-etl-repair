-- Primary key uniqueness check query
SELECT key_col, COUNT(*) FROM target_relation GROUP BY key_col HAVING COUNT(*) > 1;

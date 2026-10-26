-- Nullability bound check query
SELECT COUNT(*) FROM target_relation WHERE critical_attr IS NULL;

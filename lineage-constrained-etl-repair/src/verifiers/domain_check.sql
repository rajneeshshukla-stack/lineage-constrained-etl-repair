-- Domain constraint check query
SELECT COUNT(*) FROM target_relation WHERE domain_val NOT IN ('ACTIVE', 'INACTIVE');

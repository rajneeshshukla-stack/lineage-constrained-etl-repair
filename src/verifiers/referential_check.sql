-- Foreign key orphan check query
SELECT c.fk FROM child_table c LEFT JOIN parent_table p ON c.fk = p.pk WHERE p.pk IS NULL;

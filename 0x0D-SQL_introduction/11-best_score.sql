-- list best scores of the second database ordered by score.
-- list users with scores >= 10.
SELECT score, name FROM second_table 
WHERE score >= 10
ORDER BY score DESC;

SELECT s.name, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = 2  -- ID группы
AND g.subject_id = 3;  -- ID предмета

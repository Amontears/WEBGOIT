SELECT sub.name
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
WHERE g.student_id = 4;  -- ID студента

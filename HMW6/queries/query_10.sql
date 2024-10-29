SELECT sub.name
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
WHERE g.student_id = 5  -- ID студента
AND sub.teacher_id = 2;  -- ID преподавателя

SELECT 
    AVG(g.grade) AS average_grade,
    s.name AS subject_name,
    t.name AS teacher_name
FROM 
    grades g
JOIN 
    subjects s ON g.subject_id = s.id
JOIN 
    teachers t ON s.teacher_id = t.id
WHERE 
    t.id = 2 AND
    g.student_id = 3
    s.name;
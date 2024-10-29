SELECT g.id, g.name, AVG(gr.grade) AS average_grade
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades gr ON s.id = gr.student_id
WHERE gr.subject_id = 2  -- ID предмета
GROUP BY g.id;

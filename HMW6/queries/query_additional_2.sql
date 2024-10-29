SELECT 
    g.grade,
    s.name AS subject_name,
    st.name AS student_name
FROM 
    grades g
JOIN 
    subjects s ON g.subject_id = s.id
JOIN 
    students st ON g.student_id = st.id
WHERE 
    st.group_id = 1 AND
    g.subject_id = 3 AND
    g.date = (SELECT MAX(date) FROM grades WHERE student_id = g.student_id);

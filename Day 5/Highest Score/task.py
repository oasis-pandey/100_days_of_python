student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_val = student_scores[0]
for student_score in student_scores:
    if student_score > max_val:
        max_val = student_score

print(max_val)

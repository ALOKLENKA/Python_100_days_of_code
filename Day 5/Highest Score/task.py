student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_score=sum(student_scores)
print(total_score)
sum_score=0
for score in student_scores:
            sum_score += score
       
print(sum_score)    
 
highest_score=max(student_scores)
print(highest_score)

high_score=0
for score in student_scores:
    if(score > high_score):
        high_score=score
print(high_score)


for number  in range (1,11,3):
    print(number)
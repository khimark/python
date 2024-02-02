#get the average score

first_score = float(input("Enter the first test score: "))
second_score = float(input("Enter the second test score: "))
third_score = float(input("Enter the third test score: "))

#calculate average score
average_score = (first_score + second_score + third_score) / 3.0

#assigning range of score
def get_score():
  score = float(input("Enter the score: "))
  if score >= 0 and score <= 100:
    return score
  else:
    print("Error: the score must be between 0 and 100")

#assign grade
if average_score >= 70 and average_score <=100:
  grade = "A"
elif average_score >= 60 and average_score <=69:
  grade = "B"
elif average_score >= 50 and average_score <=59:
  grade = "C"
elif average_score >= 40 and average_score <=49:
  grade = "D"
else:
  grade = "Fail"
  
#print grade
print("Your grade is: "+ grade)

# Input a Python list of student heights

student_heights = input("height?").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  sum=+student_heights[n]
average=int(sum/len(student_heights))
print(f"total height ={sum}")
print(f"number of students= {len(student_heights)}")
print(f"average height = {average}")
# Write your code below this row 👇
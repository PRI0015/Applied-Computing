# find out student tital in class
student_amount = int(input("How many students have this class? "))

# get students names
student_names = []
for i in range(student_amount):
    name = input(f"Enter the name of student {i + 1}: ")
    student_names.append(name.strip())

# finds out how many periods per week
while True:
    try:
        period = int(input("How many times does this class happen a week? (1–5): "))
        if 1 <= period <= 5:
            break
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a number.")

# holds attendance data
attendance_data = {}

# Individual attendance 
for name in student_names:
    print(f"\n attendance for: {name}")
    present_count = 0
    for p in range(1, period + 1):
        while True:
            attendance = input(f"  Period {p} — Present (P) or Absent (A) ").strip().upper()
            if attendance in ['P', 'A']:
                if attendance == 'P':
                    present_count += 1
                break
            else:
                print("Please enter 'P' for present or 'A' for absent.")
    attendance_data[name] = present_count

# show summary and write t file
print("\nAttendance results:")
with open("attendance_summary.txt", "w") as file:
    for name in student_names:
        present = attendance_data[name]
        percentage = (present / period) * 100
        summary = f"{name}: ({percentage:.1f}%)"
        print(summary)
        file.write(summary + "\n")
        
        # warning when below 75%
        if percentage < 75:
            warning = "Attendance is below 75%, Please speak with your teacher ASAP."
            print("  " + warning)
            file.write("  " + warning + "\n")
        file.write("\n")

print("\nAttendance has been saved.")

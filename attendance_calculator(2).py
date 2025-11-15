def attendance_calculator():
    total_classes = int(input("Enter total number of classes held: "))
    attended_classes = int(input("Enter number of classes attended: "))
    target_percent = float(input("Enter your target attendance percentage (e.g., 75): "))

    current_percent = (attended_classes / total_classes) * 100
    print(f"\nYour current attendance: {current_percent:.2f}%")

    if current_percent < target_percent:
        # Calculate how many more classes you need to attend to reach the target
        required = 0
        while ((attended_classes + required) / (total_classes + required)) * 100 < target_percent:
            required += 1
        print(f"You need to attend the next {required} classes without any leave to reach {target_percent}% attendance.")
    else:
        # Calculate how many more classes you can miss and still stay above target
        can_miss = 0
        while ((attended_classes) / (total_classes + can_miss + 1)) * 100 >= target_percent:
            can_miss += 1
        print(f"You can afford to miss {can_miss} more classes and still stay above {target_percent}% attendance.")

if __name__ == "__main__":
    attendance_calculator()
import random

def simple_chatbot():
    # --- Course Information Storage ---
    course_info = {
        "course_name": "ENGLISH I - LI102004",
        "academic_year": "2025-2026",
        "instructor": "David Hughes",
        "contact": {
            "gmail": {
                "address": "davidhug@kku.ac.th",
                "purpose": "Use Gmail (davidhug@kku.ac.th) for official things: if you're sick with a doctor's certificate, or for official faculty events."
            },
            "line": {
                "id": "David H",
                "purpose": "Use LINE (ID: David H) if you'll be late, need to leave early, or need help with something."
            },
            "facebook": {
                "id": "Ajarn David-Hughes",
                "purpose": "Use Facebook (ID: Ajarn David-Hughes) if you'll be late, need to leave early, or need help."
            },
            "general_help_late_early": "If you're going to be late, need to leave early, or need help, contact Ajarn David via LINE (ID: David H) or Facebook (ID: Ajarn David-Hughes)."
        },
        "rules": {
            "general_classroom": "The main classroom rules are: Be respectful, participate actively, come prepared, and always arrive on time. Let's make learning fun and succeed together!",
            "attendance_protocol": "You must attend EVERY class and be ON TIME. Punctuality is very important for your success.",
            "excused_absences": {
                "main": "If you have a valid reason for absence, report it correctly so you won't be marked absent.",
                "sick": "If you are SICK, provide a doctor's certificate to Ajarn David (usually via Gmail).",
                "family_crisis": "For a FAMILY CRISIS, bring a letter from a family member.",
                "faculty_activity": "For a FACULTY ACTIVITY, you must inform Ajarn David IN ADVANCE."
            },
            "attendance_threshold": "You need to maintain OVER 80% attendance to be eligible for the final exam. If your attendance is below 80%, you CANNOT take the final exam, and you will lose the 20% of your grade that comes from the final exam.",
            "below_80_attendance_means": "Falling below 80% attendance means you have: more than 9 hours of absence (that's like missing more than 6 classes of 1.5hr, or more than 3 classes of 3hr) OR you have been late more than 12 times.",
            "attendance_score_impact": "Attendance itself is worth 5% of your total grade. This score goes down with each absence. For example, 0 absences = 5%, 1 absence = 4.5%, etc. Missing too many classes will give you 0 for this part and puts you at risk of not taking the final exam.",
            "academic_integrity": {
                "main": "All your submitted work must be your OWN original creation. Do not copy large amounts of text from one source. Be original!",
                "cheating_consequence": "There is ZERO TOLERANCE for cheating. If you are caught cheating on an assignment, you will get 0% for it, and the incident will be reported.",
                "ai_usage_integrity": "You can use AI tools (like ChatGPT) ONLY for tasks where Ajarn David specifically allows it. Do not use AI for assignments that must be 100% your own work."
            },
            "english_immersion": "Use English in the classroom as much as possible – aim for 100%! Using Thai too often might lead to point deductions. Speaking English helps you learn faster.",
            "device_usage": "You can use your devices (phones, laptops, etc.) in class, but ONLY for official class tasks. Playing games or chatting with friends during class is not allowed.",
            "ai_copilot": "AI tools are encouraged for research and specific English learning tasks approved by Ajarn David. Use them wisely as a learning assistant, not for cheating.",
            "homework_submission": "Submit all homework and assignments by the deadline. Late work will be penalized.",
            "respect_behavior": "Always show respect to your teacher and classmates. Disruptive behavior is not permitted.",
            "food_drink": "Generally, food and drinks are NOT allowed in class. Drinking water is usually okay. Check with Ajarn David if unsure.",
            "dress_code": "Please follow the Khon Kaen University (KKU) dress code. Your clothes should be neat, tidy, and appropriate for university."
        },
        "google_classroom": {
            "introduction": f"Ajarn David uses Google Classroom for all communication and materials for {course_info['course_name']}.",
            "what_you_find": "In Google Classroom, you'll find: course information, contact details, instructions for tasks and assignments, practice exams, vocabulary/grammar games, videos, web links, classwork, homework, and class presentations.",
            "how_to_join": "To join Google Classroom: 1. Go to the Google Classroom website or app. 2. Sign in with your personal Gmail account. 3. Use the join link Ajarn David sent by email OR enter the class code he provides. If you don't have the code, ask Ajarn David.",
            "name_format": "In Google Classroom, set your name like this: (Your role number) (Your nickname). For example: (01 Nick). This helps Ajarn David identify everyone easily.",
            "after_joining": "Once you join, you can see class posts, assignments, and other resources in the 'Stream' tab. You can use the 'People' tab to communicate with classmates."
        }
    }

    # Fixing the f-string issue by formatting it here
    course_info['google_classroom']['introduction'] = course_info['google_classroom']['introduction'].format(course_info=course_info)

    chatbot_prefix = "Chatbot: "

    print(f"{chatbot_prefix}Hello! I'm the InfoBot for {course_info['course_name']} ({course_info['academic_year']}) with Ajarn {course_info['instructor']}.")
    print(f"{chatbot_prefix}You can ask about course rules, attendance, Google Classroom, contact info, or type 'bye' to exit.")
    print(f"{chatbot_prefix}For example, try: 'attendance rules', 'what if I am sick?', 'Google Classroom name', 'how to contact Ajarn David'.")

    while True:
        user_input = input("You: ").strip()
        user_input_lower = user_input.lower()

        if not user_input:
            print(f"{chatbot_prefix}Please type a question or 'bye'.")
            continue

        if user_input_lower == "bye":
            print(f"{chatbot_prefix}Goodbye! Have a great day.")
            break
        elif "hello" in user_input_lower or "hi" in user_input_lower or "sawasdee" in user_input_lower:
            print(f"{chatbot_prefix}Hi there! How can I help you with {course_info['course_name']} info?")
        elif "thank you" in user_input_lower or "thanks" in user_input_lower:
            print(f"{chatbot_prefix}You're welcome!")

        # --- Contact Information ---
        elif "contact" in user_input_lower or "reach ajarn" in user_input_lower or "email ajarn" in user_input_lower or "line ajarn" in user_input_lower or "facebook ajarn" in user_input_lower:
            # ... rest of your code ...

if __name__ == "__main__":
    simple_chatbot()

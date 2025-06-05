Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Enter "help" below or click "Help" above for more information.
SyntaxError: invalid syntax
import random

def simple_chatbot():
    # --- Course Information Storage ---
    course_info = {
        "course_name": "ENGLISH I - LI102004",
        "academic_year": "2025-2026",
        "instructor": "David Hughes",
        "contact": { # Based on slide 6 and previous info
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
            "homework_submission": "Submit all homework and assignments by the deadline. Late work will be penalized.", # Kept from earlier, still relevant
            "respect_behavior": "Always show respect to your teacher and classmates. Disruptive behavior is not permitted.", # Kept, reinforced by new slides
            "food_drink": "Generally, food and drinks are NOT allowed in class. Drinking water is usually okay. Check with Ajarn David if unsure.", # Kept, standard rule
            "dress_code": "Please follow the Khon Kaen University (KKU) dress code. Your clothes should be neat, tidy, and appropriate for university." # Kept, standard rule
        },
        "google_classroom": {
            "introduction": f"Ajarn David uses Google Classroom for all communication and materials for {course_info['course_name']}.",
            "what_you_find": "In Google Classroom, you'll find: course information, contact details, instructions for tasks and assignments, practice exams, vocabulary/grammar games, videos, web links, classwork, homework, and class presentations.",
            "how_to_join": "To join Google Classroom: 1. Go to the Google Classroom website or app. 2. Sign in with your personal Gmail account. 3. Use the join link Ajarn David sent by email OR enter the class code he provides. If you don't have the code, ask Ajarn David.",
            "name_format": "In Google Classroom, set your name like this: (Your role number) (Your nickname). For example: (01 Nick). This helps Ajarn David identify everyone easily.",
            "after_joining": "Once you join, you can see class posts, assignments, and other resources in the 'Stream' tab. You can use the 'People' tab to communicate with classmates."
        }
    }

    print(f"Hello! I'm the InfoBot for {course_info['course_name']} ({course_info['academic_year']}) with Ajarn {course_info['instructor']}.")
    print("You can ask about course rules, attendance, Google Classroom, contact info, or type 'bye' to exit.")
    print("For example, try: 'attendance rules', 'what if I am sick?', 'Google Classroom name', 'how to contact Ajarn David'.")

    while True:
        user_input = input("You: ").strip()
        user_input_lower = user_input.lower()

        if not user_input: # Handle empty input
            print("Chatbot: Please type a question or 'bye'.")
            continue

        if user_input_lower == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif "hello" in user_input_lower or "hi" in user_input_lower or "sawasdee" in user_input_lower:
            print(f"Chatbot: Hi there! How can I help you with {course_info['course_name']} info?")
        elif "thank you" in user_input_lower or "thanks" in user_input_lower:
            print("Chatbot: You're welcome!")

        # --- Contact Information ---
        elif "contact" in user_input_lower or "reach ajarn" in user_input_lower or "email ajarn" in user_input_lower or "line ajarn" in user_input_lower or "facebook ajarn" in user_input_lower:
            if "gmail" in user_input_lower or "email" in user_input_lower:
                print(f"Chatbot: {course_info['contact']['gmail']['purpose']}")
            elif "line" in user_input_lower:
                print(f"Chatbot: {course_info['contact']['line']['purpose']}")
            elif "facebook" in user_input_lower:
                print(f"Chatbot: {course_info['contact']['facebook']['purpose']}")
            elif ("sick" in user_input_lower and "gmail" not in user_input_lower and "line" not in user_input_lower and "facebook" not in user_input_lower): # User mentions sick but not a method
                print(f"Chatbot: If you're sick with a doctor's certificate, use Gmail: {course_info['contact']['gmail']['address']}.")
            elif (("late" in user_input_lower or "leave early" in user_input_lower or "help" in user_input_lower) and "gmail" not in user_input_lower and "line" not in user_input_lower and "facebook" not in user_input_lower):
                print(f"Chatbot: {course_info['contact']['general_help_late_early']}")
            else:
                print("Chatbot: You can contact Ajarn David Hughes via:")
                print(f"  - Gmail ({course_info['contact']['gmail']['address']}): {course_info['contact']['gmail']['purpose']}")
                print(f"  - LINE (ID: {course_info['contact']['line']['id']}): {course_info['contact']['line']['purpose']}")
                print(f"  - Facebook (ID: {course_info['contact']['facebook']['id']}): {course_info['contact']['facebook']['purpose']}")
                print("What specific reason or method are you asking about?")

        # --- Attendance Rules ---
        elif "attendance" in user_input_lower or "attend class" in user_input_lower or "punctual" in user_input_lower or "on time" in user_input_lower and not "80%" in user_input_lower and not "threshold" in user_input_lower:
             if "excused" in user_input_lower or "sick" in user_input_lower or "family crisis" in user_input_lower or "faculty activity" in user_input_lower:
                if "sick" in user_input_lower: print(f"Chatbot: {course_info['rules']['excused_absences']['sick']}")
                elif "family crisis" in user_input_lower: print(f"Chatbot: {course_info['rules']['excused_absences']['family_crisis']}")
                elif "faculty activity" in user_input_lower: print(f"Chatbot: {course_info['rules']['excused_absences']['faculty_activity']}")
                else: print(f"Chatbot: {course_info['rules']['excused_absences']['main']}")
             elif "score" in user_input_lower or "impact" in user_input_lower or "grade" in user_input_lower:
                print(f"Chatbot: {course_info['rules']['attendance_score_impact']}")
             else:
                print(f"Chatbot: {course_info['rules']['attendance_protocol']}")
        elif "excused" in user_input_lower and "absence" in user_input_lower:
            if "sick" in user_input_lower: print(f"Chatbot: {course_info['rules']['excused_absences']['sick']}")
            elif "family crisis" in user_input_lower: print(f"Chatbot: {course_info['rules']['excused_absences']['family_crisis']}")
            elif "faculty activity" in user_input_lower: print(f"Chatbot: {course_info['rules']['excused_absences']['faculty_activity']}")
            else:
                print(f"Chatbot: For excused absences: {course_info['rules']['excused_absences']['main']} Specific reasons are: Sick (doctor's note), Family Crisis (family letter), Faculty Activity (tell Ajarn in advance).")
        elif "sick" in user_input_lower and ("absence" in user_input_lower or "miss class" in user_input_lower or "rule" in user_input_lower):
             print(f"Chatbot: {course_info['rules']['excused_absences']['sick']} Remember to also inform Ajarn David via Gmail: {course_info['contact']['gmail']['address']}.")
        elif "80%" in user_input_lower or "threshold" in user_input_lower or "final exam" in user_input_lower and "attendance" in user_input_lower :
            print(f"Chatbot: {course_info['rules']['attendance_threshold']}")
            print(f"Chatbot: Details: {course_info['rules']['below_80_attendance_means']}")
        elif "how many lates" in user_input_lower or "late 12 times" in user_input_lower:
             print(f"Chatbot: If you are late more than 12 times, your attendance falls below 80%, and you can't take the final exam. {course_info['rules']['below_80_attendance_means']}")
        elif "how many hours absent" in user_input_lower or "9 hours absent" in user_input_lower or "miss 9 hours" in user_input_lower:
             print(f"Chatbot: If you miss more than 9 hours of class, your attendance falls below 80%, and you can't take the final exam. {course_info['rules']['below_80_attendance_means']}")
        elif "attendance score" in user_input_lower or "attendance grade" in user_input_lower:
            print(f"Chatbot: {course_info['rules']['attendance_score_impact']}")


        # --- Academic Integrity & AI Usage ---
        elif "academic integrity" in user_input_lower or "honour code" in user_input_lower or "original work" in user_input_lower:
            print(f"Chatbot: {course_info['rules']['academic_integrity']['main']}")
            if "ai" not in user_input_lower and "cheat" not in user_input_lower: # if not asking specifically about AI/cheating
                 print(f"Chatbot: Also, remember: {course_info['rules']['academic_integrity']['cheating_consequence']}")
                 print(f"Chatbot: And for AI: {course_info['rules']['academic_integrity']['ai_usage_integrity']}")
        elif "cheat" in user_input_lower or "plagiarism" in user_input_lower:
            print(f"Chatbot: {course_info['rules']['academic_integrity']['cheating_consequence']}")
        elif "ai use" in user_input_lower or "chatgpt" in user_input_lower or "artificial intelligence" in user_input_lower and ("assignment" in user_input_lower or "work" in user_input_lower or "rule" in user_input_lower):
            print(f"Chatbot: Regarding AI tools like ChatGPT: {course_info['rules']['academic_integrity']['ai_usage_integrity']}")
            print(f"Chatbot: But generally, AI can be a good learning assistant for research or specific tasks: {course_info['rules']['ai_copilot']}")

        # --- Other Course Rules ---
        elif "english only" in user_input_lower or "speak thai" in user_input_lower or "immersion" in user_input_lower:
            print(f"Chatbot: {course_info['rules']['english_immersion']}")
        elif "device" in user_input_lower or "phone" in user_input_lower or "laptop" in user_input_lower or "gadget" in user_input_lower and "rule" in user_input_lower:
            print(f"Chatbot: {course_info['rules']['device_usage']}")
        elif "homework" in user_input_lower or "assignment" in user_input_lower and "submit" in user_input_lower or "deadline" in user_input_lower:
            print(f"Chatbot: {course_info['rules']['homework_submission']}")
        elif "respect" in user_input_lower or "behave" in user_input_lower or "disrupt" in user_input_lower:
            print(f"Chatbot: {course_info['rules']['respect_behavior']}")
        elif "food" in user_input_lower or "drink" in user_input_lower or "water" in user_input_lower and "class" in user_input_lower:
            print(f"Chatbot: {course_info['rules']['food_drink']}")
        elif "dress" in user_input_lower or "attire" in user_input_lower or "uniform" in user_input_lower:
            print(f"Chatbot: {course_info['rules']['dress_code']}")
        elif "general rules" in user_input_lower or ("rules" in user_input_lower and "classroom" in user_input_lower):
            print(f"Chatbot: {course_info['rules']['general_classroom']}")


        # --- Google Classroom ---
        elif "google classroom" in user_input_lower or "class code" in user_input_lower:
            if "name" in user_input_lower and "format" in user_input_lower:
                print(f"Chatbot: {course_info['google_classroom']['name_format']}")
            elif "join" in user_input_lower or "how to" in user_input_lower or "class code" in user_input_lower:
                print(f"Chatbot: {course_info['google_classroom']['how_to_join']}")
            elif "find on" in user_input_lower or "what is on" in user_input_lower or "content" in user_input_lower :
                print(f"Chatbot: {course_info['google_classroom']['what_you_find']}")
            else:
                print(f"Chatbot: {course_info['google_classroom']['introduction']}")
                print(f"Chatbot: To join: {course_info['google_classroom']['how_to_join']}")
                print(f"Chatbot: Remember the name format: {course_info['google_classroom']['name_format']}")
        elif "name format" in user_input_lower and "google classroom" in user_input_lower:
             print(f"Chatbot: {course_info['google_classroom']['name_format']}")

        # --- General fallback ---
        elif "what can you do" in user_input_lower or "help" in user_input_lower:
...             print("Chatbot: I can tell you about:")
...             print("  - Course rules (attendance, academic integrity, device usage, etc.)")
...             print("  - Google Classroom (how to join, name format, what's on it)")
...             print("  - How to contact Ajarn David Hughes")
...             print("  - Specific policies like the 80% attendance rule.")
...             print("Try asking a specific question like 'What is the rule for using phones?' or 'How do I join Google Classroom?'")
...         else:
...             print("Chatbot: Sorry, I'm not sure how to answer that. Can you try asking in a different way? You can ask about course rules, Google Classroom, or contact info.")
... 
... if __name__ == "__main__":
...     # Initialize course_info by calling a helper or defining it directly
...     # For this setup, course_info is defined inside simple_chatbot to make it self-contained
...     # However, for the f-string for google_classroom.introduction to work correctly with course_info['course_name']
...     # it needs course_info to be defined before it's used.
...     # A simple way is to define it globally or pass it into the function.
...     # For now, I'll redefine the specific string that uses an f-string from course_info within the function before printing.
...     
...     # Actually, defining course_info at the beginning of the function makes it available
...     # for the f-string used in course_info['google_classroom']['introduction']
...     # This is a bit of a circular setup if not careful, but Python evaluates dict values at definition time.
...     # To ensure it works cleanly, I'll adjust the problematic f-string to be formatted when used.
...     
...     # Re-evaluating: The f-string inside the dictionary value will capture the state of course_info['course_name']
...     # at the moment the dictionary is defined. This should be fine as course_name is static.
... 

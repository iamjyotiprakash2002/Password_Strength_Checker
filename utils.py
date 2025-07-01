import random
import string

def check_strength(password):
    score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("🔴 Looks like your password is quite short. Aim for at least 8 characters to boost your security.")
    else:
        score += 1

    if not any(c.islower() for c in password):
        feedback.append("🟡 Including lowercase letters makes your password more balanced.")
    else:
        score += 1

    if not any(c.isupper() for c in password):
        feedback.append("🟡 Try mixing in some uppercase letters — it adds complexity.")
    else:
        score += 1

    if not any(c.isdigit() for c in password):
        feedback.append("🟡 Adding numbers can make passwords harder to crack.")
    else:
        score += 1

    if not any(c in "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~" for c in password):
        feedback.append("🟡 Special characters like ! or # can significantly improve strength.")
    else:
        score += 1

    return score, feedback

def is_common_password(password):
    try:
        with open("common_passwords.txt", "r") as file:
            common = file.read().splitlines()
        return password.strip() in common
    except FileNotFoundError:
        return False

def suggest_stronger_password(base_password):
    suggestion = base_password

    if len(suggestion) < 8:
        suggestion += ''.join(random.choices(string.ascii_letters + string.digits, k=8 - len(suggestion)))

    if not any(c.isupper() for c in suggestion):
        suggestion += random.choice(string.ascii_uppercase)

    if not any(c.islower() for c in suggestion):
        suggestion += random.choice(string.ascii_lowercase)

    if not any(c.isdigit() for c in suggestion):
        suggestion += str(random.randint(0, 9))

    if not any(c in "!@#$%^&*()" for c in suggestion):
        suggestion += random.choice("!@#$%^&*()")

    # Shuffle characters
    return ''.join(random.sample(suggestion, len(suggestion)))

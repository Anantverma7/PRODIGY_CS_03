import re

def assess_password_strength(password):
    # Define the criteria
    length_criteria = 8
    lowercase_criteria = re.compile(r'[a-z]')
    uppercase_criteria = re.compile(r'[A-Z]')
    number_criteria = re.compile(r'\d')
    special_char_criteria = re.compile(r'[\W_]')

    # Initialize score and feedback
    score = 0
    feedback = []

    # Check length
    if len(password) >= length_criteria:
        score += 1
    else:
        feedback.append(f'Password should be at least {length_criteria} characters long.')

    # Check for lowercase letters
    if lowercase_criteria.search(password):
        score += 1
    else:
        feedback.append('Password should include at least one lowercase letter.')

    # Check for uppercase letters
    if uppercase_criteria.search(password):
        score += 1
    else:
        feedback.append('Password should include at least one uppercase letter.')

    # Check for numbers
    if number_criteria.search(password):
        score += 1
    else:
        feedback.append('Password should include at least one number.')

    # Check for special characters
    if special_char_criteria.search(password):
        score += 1
    else:
        feedback.append('Password should include at least one special character.')

    # Determine strength
    if score == 5:
        strength = 'Very Strong'
    elif score == 4:
        strength = 'Strong'
    elif score == 3:
        strength = 'Moderate'
    else:
        strength = 'Weak'

    # Combine feedback into a single string
    feedback_message = ' '.join(feedback)

    return {
        'strength': strength,
        'score': score,
        'feedback': feedback_message
    }

# Take password input from user
password = input("Enter your password: ")

# Assess password strength
result = assess_password_strength(password)

# Display the results
print(f"Password Strength: {result['strength']}")
print(f"Score: {result['score']}/5")
print(f"Feedback: {result['feedback']}")

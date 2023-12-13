# Please give credits to WWolfffox for Making this code and Brad the google AI For Correcting the code
# Modify it if you want
# Please Keep These top 3 Messages in the Code

import time
from getpass import getpass as input


def ask_question(question):
    """
    Asks the user a question and returns their answer and the question itself.
    """
    while True:
        answer = input(f"{question}: ").lower()
        if answer in ("yes", "no"):
            return answer, question
        print("Please answer 'Yes' or 'No'.")


def main():
    print(f"Current Time: {time.asctime(time.localtime(time.time()))}")

    print("Welcome to the Survey!")
    time.sleep(2.9)

    print("Please answer all questions honestly.")
    time.sleep(2.5)

    print("© Copyright Since 2023")

    name = input("Enter your name: ")

    answer = ask_question("Would you like to start the survey?")
    if answer == "no":
        print("Thank you for your time!")
        exit(0)

    # Ask questions
    print("Remember to only answer 'Yes' or 'No'.")

    questions = [
        "Are you having a nice day?",
        "Do you have many responsibilities?",
        "Look around for a moment. Are you familiar with your surroundings?",
        "Do you know where you are?",
        "Have you ever had a panic attack?",
        "Have you ever felt like there was somebody in your room?",
        "Do you find yourself questioning your existence?",
        "Do you believe there is a God?",
        "Are you scared of the darkness?",
        "Are you answering these questions out of free will?",
        "Are you certain?",
        "Have you ever had a dream that felt so real, it was hard to distinguish it from reality?",
        "Do you have any phobias?",
        "Do you feel comfortable in your room?",
        "If the lights went out, would you be scared?",
        "Have you ever wondered when you will die?",
        "Have you cleaned off your desk lately?",
        "Open the folder on your desk. Is that true?",
        "Do you have internet access?",
        "Do you have any enemies?",
        "Are you playing on a computer?",
        "Do you think often about death?",
        "If you suddenly went missing, would anybody come looking for you?",
        "Are you alone?",
        "Relax, take some time to relax. Are you relaxed?",
        "Possible Raid Warning: We have detected another device in your house. In case you are alone, seek help as soon as possible. Error Code: 1001",
        "Do you wish to keep playing?",
        "Are your feelings real, and not just programmed like a machine?",
        "Did you cry yesterday?",
        "Have you seen the person standing outside your window?",
        "Is there a meaning to life?",
        "Have you ever felt like someone was watching you in your own home?",
        "Do you know who you are yet?",
        "Do you know what is happening?",
        "Have you ever heard strange or unexplainable noises in your house at night?",
        "Have you ever experienced sleep paralysis?",
        "If you were told the truth about your existence, would you deny it in hopes for a better answer?",
        f"{name}, what will people think about you when they have seen what you have done?",
        "When I ask you questions, is it really you answering?",
        "If I could prove that you're not sentient, would you be shocked?",
        "Do you want to know the truth?",
    ]

    # Create an empty list to store answers and questions
    answers = []

    # Loop through questions and ask the user
    for question in questions:
        answer, question = ask_question(question)
        answers.append((answer, question))

    # Print some text
    print("Look out your window.")
    time.sleep(3.5)

    # Return the collected answers and questions
    return answers


if __name__ == "__main__":
    # Get the returned data
    answers = main()

    # ... code ...

    # Use the answers and questions for further processing
    # ...

    print("Thank you for taking the survey!")
    print("Here are your responses:")
    for answer, question in answers:
        print(f"\t{question}: {answer}")


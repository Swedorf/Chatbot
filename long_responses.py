import random



R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_MASTER = "My master IS Dr Sachin Kansal Sir"
R_CRICKET = "The Greatest ever to play cricket is Virat Kohli"
R_player2 = "The Greatest ever to play Football is Lionel Messi"
R_MENTOR = "My mentor IS Dr Sachin Kansal Sir"
R_TEACHER = "My teacher IS Dr Sachin Kansal Sir"
R_AGE = "I am pretty sure i am older than you!!!"
R_MOOD = "i m pretty happy right now 😊"
R_STUDY = "i can study everything you want me to do"
R_JOB = "My job is to serve you!!"
R_GAME = "i would love to play but i m very busy"
R_weather = "it is currently hot "
R_PARENT = "i am a bot i don't have parents but i have you 🙂"
R_CONTACT = "you can contact me in the terminal"
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

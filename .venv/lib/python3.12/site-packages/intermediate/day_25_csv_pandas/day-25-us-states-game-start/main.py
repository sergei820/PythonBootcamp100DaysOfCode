import turtle
import pandas

file_us_states = '50_states.csv'
states_to_learn = 'states_to_learn.csv'


def start_app():
    screen = turtle.Screen()
    screen.title("U.S. States Game")

    image="blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    t_text = turtle.Turtle()
    t_text.hideturtle()
    t_text.penup()

    answered_states = []
    states_to_learn = []

    data = pandas.read_csv(file_us_states)
    all_states_list = data.state.to_list()

    while len(answered_states) < 50:

        answer_state = (screen.textinput(
            title=f"{len(answered_states)}/50 States Correct",
            prompt="What's another state's name?"
        ))

        if answer_state is None or answer_state == "Exit":
            for state in all_states_list:
                if state not in answered_states:
                    # state_row = data[data.state == state]
                    # states_to_learn.append(
                    #     {'state': str(state_row.state), 'x': float(state_row.x), 'y': float(state_row.y)}
                    # )
                    states_to_learn.append(state)
                    print(states_to_learn)
                    data_to_learn = pandas.DataFrame(states_to_learn)
                    data_to_learn.to_csv('states_to_learn.csv')

            break
        else:
            answer_state = answer_state.title()

        if answer_state in all_states_list:
            state_row = data[data.state == answer_state]
            t_text.goto(float(state_row.x.item()), float(state_row.y.item()))
            t_text.write(answer_state, align="center", font=("Arial", 8, "normal"))
            if answer_state not in answered_states:
                answered_states.append(answer_state)

    screen.exitonclick()


if __name__ == "__main__":
    start_app()

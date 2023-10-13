import requests
import json
import gradio as gr

IATA = ['ICN', 'KIX', 'CTS']
port = 8000

def input(departure, arrival, year, month, day):
    result = f"Departure is {departure} and arrival is {arrival}\nYour flight is {int(year)}-{int(month)}-{int(day)}"
    data = {'departure':departure, 'arrival':arrival, 'year':year, 'month':month, 'day':day}
    res = requests.post(
        f"http://127.0.0.1:{port}/upload/",
        data=json.dumps(data)
    )
    return result

demo = gr.Interface(
    input,
    [
        gr.Dropdown(
            IATA, label="Departure"
        ),
        gr.Dropdown(
            IATA, label="Arrival"
        ),
        gr.Number(
            label="year"
        ),
        gr.Number(
            label="month"
        ),
        gr.Number(
            label="day"
        )
    ],
    'text'
)

demo.launch()
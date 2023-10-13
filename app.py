import requests
import gradio as gr

def input(departure, arrival, year, month, day):
    result = f"Departure is {departure} and arrival is {arrival}\nYour flight is {int(year)}-{int(month)}-{int(day)}"
    return result

demo = gr.Interface(
    input,
    [
        gr.Dropdown(
            ["ICN", "KIX", "CTS"], label="Departure"
        ),
        gr.Dropdown(
            ["ICN", "KIX", "CTS"], label="Arrival"
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
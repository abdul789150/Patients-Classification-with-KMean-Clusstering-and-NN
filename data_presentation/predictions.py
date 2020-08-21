# -*- coding: utf-8 -*-

# This is the main file for running the data presentation web app
# Libraries to be used
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import visualization_backend

# Functions for getting training and testing accuracies from visualization_backend script
def get_training_accuracy():
    score = visualization_backend.get_training_acc()
    str_score = "{:.2%}".format(score)
    return str_score

def get_testing_accuracy():
    score = visualization_backend.get_testing_acc()
    str_score = "{:.2%}".format(score)
    return str_score

# Initializing our web app with a theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Side panel
panel = html.Div([
    dbc.Col(html.H3("Results"), width={"size":6,"offset":3}), 
    html.Br(),
    dbc.Card(body=True, className="text-white bg-dark", children=[
        html.H6("Training Accuracy:", style={"color":"white"}),
        html.H5(children=get_training_accuracy(), id="training_accuracy", className="text-danger"),
        
        html.H6("Testing Accuracy:", style={"color":"white"}),
        html.H5(children=get_testing_accuracy(), id="testing_accuracy", className="text-danger"),

        html.Br(),
        html.H6("Model Prediction from given values: ", style={"color":"white"}),
        # html.H6("Model Prediction:", style={"color":"white"}),
        html.H5(id="prediction", className="text-danger"),
    ])
])




# Input Fields
systolic_input = dbc.FormGroup([
    dbc.Label("Systolic"),
    dbc.Input(id="systolic", placeholder="Ex: 93.0", type="text"),
    dbc.FormText("Enter patient\'s systolic information")
])

diastolic_input = dbc.FormGroup([
    dbc.Label("Diastolic"),
    dbc.Input(id="diastolic", placeholder="Ex: 69.0", type="text"),
    dbc.FormText("Enter patient\'s Diastolic information")
])

avg_bp_input = dbc.FormGroup([
    dbc.Label("Average Blood Pressure"),
    dbc.Input(id="avg_bp", placeholder="Ex: 75.0", type="text"),
    dbc.FormText("Enter patient\'s Average Blood Pressure information")
])

heart_rate_input = dbc.FormGroup([
    dbc.Label("Heart Rate"),
    dbc.Input(id="heart_rate", placeholder="Ex: 95.0", type="text"),
    dbc.FormText("Enter patient\'s Heart Rate information")
])

glucose_input = dbc.FormGroup([
    dbc.Label("Glucose"),
    dbc.Input(id="glucose", placeholder="Ex: 78.0", type="text"),
    dbc.FormText("Enter patient\'s Glucose information")
])

spo2_input = dbc.FormGroup([
    dbc.Label("SpO2"),
    dbc.Input(id="spo2", placeholder="Ex: 95.0", type="text"),
    dbc.FormText("Enter patient\'s SpO2 information")
])

weight_input = dbc.FormGroup([
    dbc.Label("Weight"),
    dbc.Input(id="weight", placeholder="Ex: 49.3", type="text"),
    dbc.FormText("Enter patient\'s Weight information")
])

height_input = dbc.FormGroup([
    dbc.Label("Height"),
    dbc.Input(id="height", placeholder="Ex: 1.57", type="text"),
    dbc.FormText("Enter patient\'s Height information")
])

imc_input = dbc.FormGroup([
    dbc.Label("IMC"),
    dbc.Input(id="imc", placeholder="Ex: 19.3", type="text"),
    # html.Br(),
    dbc.FormText("Enter patient\'s IMC information")
])


# Creating a proper formating of input fields 

input_form = html.Div([
    dbc.Col(html.H3("Data Prediction"), width={"size":6,"offset":5}), 
    html.Br(),
    html.H6("Fill up all fields with patient data for prediction"),
    html.Br(),
    dbc.Row([
        dbc.Col(html.Div([systolic_input]), width=4),
        dbc.Col(html.Div([diastolic_input]), width=4),
        dbc.Col(html.Div([avg_bp_input]), width=4),
    ]),
    dbc.Row([
        dbc.Col(html.Div([heart_rate_input]), width=4),
        dbc.Col(html.Div([glucose_input]), width=4),
        dbc.Col(html.Div([spo2_input]), width=4),
    ]),
    dbc.Row([
        dbc.Col(html.Div([weight_input]), width=4),
        dbc.Col(html.Div([height_input]), width=4),
        dbc.Col(html.Div([imc_input]), width=4),
    ]),
    dbc.Row([

    ]),
    dbc.Row([

    ]),

])

# Adding everything in a div 
row = html.Div(
    [
        html.Div([
            html.Br(),
            dbc.Col(html.H1("Model Presentation"), style={'text-align': 'center'}), 
            html.Br(),html.Br()
        ]),
        dbc.Row(
            [
                dbc.Col(html.Div([panel]), width=3),
                dbc.Col(html.Div([input_form]), width=8),
            ]
        ),
    ]
)


app.layout = dbc.Container(fluid=True, children=
    [
        row,
    ],
)


# This is the calback function whenever input fields are updated with data it will be called
@app.callback(
    Output("prediction", "children"),
    [Input("systolic", "value"), Input("diastolic", "value"), Input("avg_bp", "value"),
    Input("heart_rate", "value"), Input("glucose", "value"), Input("spo2", "value"),
    Input("weight", "value"), Input("height", "value"), Input("imc", "value")],
)
# Function attached to callback which is responsible for the computation of data
def update_output(systolic, diastolic, avg_bp, heart_rate, glucose, spo2, weight, height, imc):
    if (systolic != None and systolic != "") and (diastolic != None and diastolic != "") and (avg_bp != None and avg_bp != "") and (heart_rate != None and heart_rate != "") and (glucose != None and glucose != "") and (spo2 != None and spo2 != "") and (weight != None and weight != "") and (height != None and height != "") and (imc != None and imc != ""):
        # Checking if all values are float
        try:
            conv_systolic = float(systolic)
            conv_diastolic = float(diastolic)
            conv_avg_bp = float(avg_bp)
            conv_heart_rate = float(heart_rate)
            conv_glucose = float(glucose)
            conv_spo2 = float(spo2)
            conv_weight = float(weight)
            conv_height = float(height)
            conv_imc = float(imc)

            # Getting predicted value from the backend file
            predicted_data = visualization_backend.predict_class(conv_systolic, conv_diastolic, conv_avg_bp, conv_heart_rate, conv_glucose, conv_spo2, conv_weight, conv_height, conv_imc)
            print(predicted_data)
            if predicted_data[0] == 1:
                return "Diagnose"
            elif predicted_data[0] == 0:
                return "Healthy"

        except ValueError:
            return "Please enter float or integer numbers only!"

        return "Okk working now"
    else:
        return 'Please fill all fields'


if __name__ == "__main__":
    app.run_server(debug=True)

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', results=None)
    
    else:
        # Capturing form elements matching the HTML input 'name' attributes
        data = CustomData(
            type=str(request.form.get('type')),
            air_temperature_k=float(request.form.get('air_temperature')),
            process_temperature_k=float(request.form.get('process_temperature')),
            rotational_speed_rpm=float(request.form.get('rotational_speed')),
            torque_nm=float(request.form.get('torque')),
            tool_wear_min=float(request.form.get('tool_wear'))
        )
        
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        # Passing results back to the main dashboard
        return render_template('index.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
import pandas as pd
from potassium import Potassium, Request, Response
from transformers import pipeline
import torch

# Initialize Potassium app
app = Potassium("my_app")

# Initialize BERT model
@app.init
def init():
    # Check if there is a GPU
    device = 0 if torch.cuda.is_available() else -1

    # Define the BERT model using the pipeline interface from transformers
    bert_model = pipeline('fill-mask', model='bert-base-uncased', device=device)
   
    context = {
        "model_b": bert_model,
    }

    return context

# Handler to process each row and append predicted activity to pivot_data4
def process_rows(context: dict, pivot_data4: pd.DataFrame) -> pd.DataFrame:
    # Retrieve the BERT model from the context
    model = context.get("model_b")

    # Initialize empty lists to store predicted activities and substitutions
    predicted_activities = []
    substitutions = []

    # Iterate over each row of pivot_data4
    for index, row in pivot_data4.iterrows():
        # Extract motion type from the current row
        motion_type = row['motion_type']

        # Create prompt using the motion type and [MASK] token
        prompt = f"I am {motion_type} thus am performing [MASK]"

        # Generate predictions using the BERT model
        predictions = model(prompt)

        # Extract the first prediction suggestion for the [MASK] token
        suggestion = predictions[0]['token_str']

        # Append the predicted activity and suggestion to the respective lists
        predicted_activities.append(predictions[0]['sequence'])
        substitutions.append(suggestion)

    # Add the lists of predicted activities and suggestions as new columns to pivot_data4
    pivot_data4['predicted_activity'] = predicted_activities
    pivot_data4['suggestion_for_mask'] = substitutions

    return pivot_data4

# Endpoint to trigger the processing of rows
@app.handler("/process_rows")
def handler(context: dict, request: Request) -> Response:
    # Retrieve pivot_data4 from the request payload
    pivot_data4 = request.json.get("pivot_data4")

    # Process rows and append predicted activities and substitutions
    pivot_data4_with_predictions = process_rows(context, pd.DataFrame(pivot_data4))

    # Return the updated pivot_data4 with predicted activities and substitutions
    return Response(
        json=pivot_data4_with_predictions.to_dict(orient='records'),
        status=200
    )

# Run the Potassium app
if __name__ == "__main__":
    app.serve()
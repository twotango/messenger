from potassium import Potassium, Request, Response
from transformers import pipeline
import torch
import time

app = Potassium("my_app")

# @app.init runs at startup, and initializes the app's context
@app.init
def init():
    # Check if there is a GPU
    device = 0 if torch.cuda.is_available() else -1

    # Defind the model, using the "pipeline" interface from transformers
    bertModel = pipeline('fill-mask', model='bert-base-uncased', device=device)
   
    
    context = {
        "model_b": bertModel,
    }

    return context



# @app.handler is an http post handler running for every call
@app.handler("/bert")
def handler(context: dict, request: Request) -> Response:
    
    # our model is from 'model_b' as defined in the context earlier
    model = context.get("model_b")

    # our prompt is from the 'prompt' key in the user request
    prompt = request.json.get("prompt")

    # the outputs is created by passing the user request to the model
    outputs = model(prompt)

    # returned
    return Response(
        json = {"outputs": outputs}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()
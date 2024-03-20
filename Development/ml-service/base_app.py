from potassium import Potassium, Request, Response
# from transformers import pipeline
import torch

app = Potassium("my_app")

def custom_model(inputData):
  outcome = "Hello from a function, this is your input data: " + inputData
  print(outcome) 
  return outcome

# @app.init runs at startup, and initializes the app's context
@app.init
def init():

    # Check if there is a GPU
    device = 0 if torch.cuda.is_available() else -1

    # Define the model, using the "pipeline" interface from transformers
    # bertModel = pipeline('fill-mask', model='bert-base-uncased', device=device)

    # define any model that you understand how to process
    # model = custom_model
    
    context = {
        # "model_b": bertModel,
        # model: model
    }

    return context



# @app.handler is an http post handler running for every call
@app.handler("/custom")
def handler(context: dict, request: Request) -> Response:
    
    # our model is from 'model_b' as defined in the context earlier
    # model = context.get("model")
    # model = custom_model

    # our prompt is from the 'prompt' key in the user request
    # input = request.json.get("prompt")

    inputData = 'this is where my input data will be.'

    # the outputs is created by passing the user request to the model
    outcome = custom_model(inputData)

    print(outcome)

    # returned
    return Response(
        json = {"outputs": outcome}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()
# folder for potassium (python framework for apis)

1. Install potassium via banana-cli (for more automated scaffolding)

```
pip3 install banana-cli
```

2. Set up the project
```
banana init my-app
```

If banana doesn't work, that's okay. It just means we will need to build the project manually, which is good practice anyway,
because it gives you more control and ensures you understand exactly what you are running.


---

# Manually

1. Install potassum manually (for more control)

```
pip3 install potassium
```

2. Create the project (this is already done in ml-service)
```
...
```

3. Install dependencies
```
pip3 install transformers torch
```

4. Run the python script (application)
```
python3 default_app.py
```

5. Talk to the python script like it is an internet serice (api - application programing interface)
```
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "I am really [MASK] right now."}' http://localhost:8000
```


## References

https://github.com/bananaml/potassium - the link this all started from
https://pypi.org/project/transformers/ - reading about pipelines
https://huggingface.co/google-bert/bert-base-uncased - bert model we used
https://node-red
https://mini.ai/ - What I curled
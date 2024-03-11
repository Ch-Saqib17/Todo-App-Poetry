**First Follow These Step**
[https://github.com/mkdeveloper/Installing_Poetry_on_windows_OS]
**Second Step Create Project**
```python
poetry new pathname
``` 
(poetry new todo)
**Third Step Add Packages**
poetry add fastapi sqlmodel python-dotenv uvicorn
**After Installation Then Test Api**
->Create a file
->Write Get Method Api
Like
`@app.get("/")
def getdata():
    return {"message": "Hello World"}`
**After This Run Uvicorn Server**
->First Enter File Directory Where you make api
->Then Write command in Terminal 
`uvicorn filename:app --reload`
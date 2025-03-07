from fastapi import FastAPI
from pydantic import BaseModel
from rag_app.query_rag import QueryResponse, query_rag
import uvicorn
from mangum import Mangum

app = FastAPI()

handler = Mangum(app) # creates entrypoint for AWS Lambda


class SubmitQueryRequest(BaseModel):
    query_text : str


@app.get("/")
def index():
    return('Hi there')


@app.post("/submit_query")
def submit_query_endpoint(request: SubmitQueryRequest) -> QueryResponse:
    query_response = query_rag(request.query_text)
    return query_response


if __name__ == "__main__":
   # Run this as a server directly.
   port = 8000
   print(f"Running the FastAPI server on port {port}.")
   uvicorn.run("app_api_handler:app", host="0.0.0.0", port=port)
   # http://localhost:8000
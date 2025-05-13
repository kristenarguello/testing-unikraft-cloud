import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI(root_path="/agent1")


class InputBody(BaseModel):
    input: str


@app.post("/chat")
async def chat(input_body: InputBody):
    return StreamingResponse(
        event_stream(input_body),
        media_type="text/event-stream",
        headers={"X-Accel-Buffering": "no"},
    )


async def event_stream(body: InputBody):
    for i in range(5):
        yield f"data: Hello, world! {i} - {body.input}\n\n"
        await asyncio.sleep(3)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

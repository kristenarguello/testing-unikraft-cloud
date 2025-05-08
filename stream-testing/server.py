import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn

app = FastAPI()

@app.post('/chat')
async def chat():
    return StreamingResponse(
        event_stream(),
        media_type='text/event-stream',
    )

async def event_stream():
    for i in range(5):
        yield f"data: Hello, world! {i}\n\n"
        await asyncio.sleep(3)



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)


import asyncio

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route

import ocr

ocr.load()


async def handler(request):
    form = await request.form()
    if "image" not in form:
        return PlainTextResponse("Missing `image` field.", 400)

    contents = await form["image"].read()
    loop = asyncio.get_event_loop()
    latex = await loop.run_in_executor(None, ocr.test_image, contents)

    return PlainTextResponse(latex)


middleware = [Middleware(CORSMiddleware, allow_origins=["*"])]
app = Starlette(debug=True, routes=[Route("/image", handler, methods=["POST"])], middleware=middleware)

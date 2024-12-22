from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()

@app.get("/sub")
def get_sub():
    headers = {
        "routing": (
            "eyJydWxlcyI6W3sidHlwZSI6ImZpZWxkIiwib3V0Ym91bmRUYWciOiJmcmVlZG9tIiwiX19pZF9fIjoiRTY0MkQ2MjMtRUZEMy00NTVGLTlBNkEtRTk1Q0FBQUNDRjVDIiwiZG9tYWluIjpbImdlb3NpdGU6dmsiXSwiZG9tYWluTWF0Y2hlciI6Imh5YnJpZCIsIl9fbmFtZV9fIjoidmsifV0sIm5hbWUiOiLQsNC90LTRgNC10Lkg0LvQvtGFIiwiZG9tYWluU3RyYXRlZ3kiOiJBc0lzIiwiaWQiOiI5Q0E2RjVERS02NDY1LTQ4Q0MtOTU0Qy00OTFDNUZGRjM3MDQiLCJkb21haW5NYXRjaGVyIjoiaHlicmlkIiwiYmFsYW5jZXJzIjpbXX0="
        )
    }

    content = (
        "vless://"
    )

    return Response(content=content, media_type="text/plain", headers=headers)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
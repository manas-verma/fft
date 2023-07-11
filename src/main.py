from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
import ruspy as rp


app = FastAPI()

# Configure CORS
# This allows all origins (you can specify specific origins as well)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ComplexArray(BaseModel):
    re: List[str]
    im: Optional[List[str]] = None


@app.get("/")
async def welcome():
    return "Welcome to FFT API"


@app.post("/post")
async def fft(values: ComplexArray):
    re = values.re
    im = values.im if values.im is not None else [0] * len(re)
    values = [complex(float(re[i]), float(im[i])) for i in range(len(re))]
    output = rp.fft(rp.array(values))
    return {
        "re": [str(output[i].real) for i in range(len(output))],
        "im": [str(output[i].imag) for i in range(len(output))],
    }


@app.get("/calc")
async def fft(re: List[str], im: Optional[List[str]] = None):
    re = re
    im = im if im is not None else [0] * len(re)
    values = [complex(float(re[i]), float(im[i])) for i in range(len(re))]
    output = rp.fft(rp.array(values))
    return {
        "re": [str(output[i].real) for i in range(len(output))],
        "im": [str(output[i].imag) for i in range(len(output))],
    }

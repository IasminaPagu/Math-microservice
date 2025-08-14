from pydantic import BaseModel, Field, conint, confloat

class PowInput(BaseModel):
    base: float = Field(..., description="Base (float)")
    exponent: float = Field(..., description="Exponent (float)")

class PowResult(BaseModel):
    result: float


class FibonacciInput(BaseModel):
    n: conint(strict=True, ge=1) = Field(..., description="Fibonacci term index (integer >= 1)")

class FibonacciResult(BaseModel):
    result: int  

class FactorialInput(BaseModel):
    n: conint(strict=True, ge=1) = Field(..., description="Positive integer for factorial")

class FactorialResult(BaseModel):
    result: int

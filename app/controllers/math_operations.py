from fastapi import APIRouter, Depends
from app.schemas.math_models import *
from app.services.math_services import power as calc_power, fibonacci as calc_fib, factorial as calc_fact
from app.services.db_services import save_operation
import time
from app.utils.security import get_current_user
from app.utils.messaging import send_to_queue
from app.models.db_models import User
router = APIRouter(
    prefix="/math",
    tags=["math"],
    dependencies=[Depends(get_current_user)] 
)

@router.post("/pow", response_model=PowResult)
async def power(payload: PowInput, user: User = Depends(get_current_user)):
    print("\n\n🚨 Endpoint Power executat!\n\n")
    start_time = time.perf_counter()
    result = await calc_power(payload.base, payload.exponent)
    end_time = time.perf_counter()
    await send_to_queue({
        "operation": "pow", 
        "input": payload.dict(), 
        "result": result, 
        "execution_time_ms": end_time - start_time,
        "user_id": user.id
    })
    return PowResult(result=result)


   

@router.post("/fibonacci", response_model=FibonacciResult)
async def fibonacci(payload: FibonacciInput, user: User = Depends(get_current_user)):
    print("\n\n🚨 Endpoint Fibonacci executat!\n\n")
    start_time = time.perf_counter()
    result = await calc_fib(payload.n)
    end_time = time.perf_counter()
    await send_to_queue({
        "operation": "fibonacci", 
        "input": payload.dict(), 
        "result": result, 
        "execution_time_ms": end_time - start_time,
        "user_id": user.id
    })
    return FibonacciResult(result=result)

@router.post("/factorial", response_model=FactorialResult)
async def factorial(payload: FactorialInput, user: User = Depends(get_current_user)):
    print("\n\n🚨 Endpoint Factorial executat!\n\n")
    start_time = time.perf_counter()
    result = await calc_fact(payload.n)
    end_time = time.perf_counter()
    await send_to_queue({
        "operation": "factorial", 
        "input": payload.dict(), 
        "result": result, 
        "execution_time_ms": end_time - start_time,
        "user_id": user.id
    })
    return FactorialResult(result=result)

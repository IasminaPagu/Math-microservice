import json
from datetime import datetime
from app.db.db import SessionLocal
from app.models.db_models import OperationRequest

def save_operation(operation_name: str, input_data: dict, result: dict, execution_time_ms: float, user_id: int ):
    db = SessionLocal()
    try:
        operation = OperationRequest(
            operation=operation_name,
            input_data=json.dumps(input_data), 
            result=json.dumps(result),
            timestamp=datetime.utcnow(),
            execution_time_ms=execution_time_ms,
            user_id=user_id
        )
        db.add(operation)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

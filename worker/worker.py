import asyncio
import aio_pika
import json
from app.services.db_services import save_operation

QUEUE_NAME = "math_queue"

async def connect_rabbitmq():
    while True:
        try:
            connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")
            return connection
        except Exception as e:
            print(f"RabbitMQ not ready, retrying in 5 seconds... ({e})")
            await asyncio.sleep(5)

async def main():
    connection = await connect_rabbitmq()
    channel = await connection.channel()
    queue = await channel.declare_queue(QUEUE_NAME, durable=True)
    print(f"✅ Listening on queue: {QUEUE_NAME}",flush=True)

    async def on_message(message: aio_pika.IncomingMessage):
        async with message.process():
            try:
                data = json.loads(message.body.decode())
                print(f"[📥] Received: {data}")
                operation = data["operation"]
                input_data = data["input"]
                result = data["result"]
                exec_time = data["execution_time_ms"]
                user_id = data.get("user_id")
                save_operation(operation, input_data, {"result": result}, exec_time,user_id=user_id)
                print("💾 Operation saved in DB!")
            except Exception as e:
                print(f"[❌] Error processing message: {e}")

    await queue.consume(on_message)
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
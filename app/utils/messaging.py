import aio_pika
import json
from typing import Any


async def send_to_queue(message: dict, queue_name: str = "math_queue") -> None:
    try:
        connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")

        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue(queue_name, durable=True)

            body = json.dumps(message).encode()
            await channel.default_exchange.publish(
                aio_pika.Message(body=body, delivery_mode=aio_pika.DeliveryMode.PERSISTENT),
                routing_key=queue_name,
            )

            print(f"[x] Sent message to '{queue_name}': {body.decode()}")

    except Exception as e:
        print(f"[!] Error sending message to queue: {e}")

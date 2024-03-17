import asyncio
import threading
import time

# Define a blocking function
def blocking_function(name):
    print(f"{name}: Blocking function started")
    time.sleep(2)  # Simulate a blocking operation
    print(f"{name}: Blocking function completed")

# Define an asynchronous function that runs the blocking function in a separate thread
async def async_with_thread(name):
    print(f"{name}: Async with thread started")
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, blocking_function, name)
    print(f"{name}: Async with thread completed")

# Run multiple async functions concurrently
async def main():
    tasks = []
    for i in range(3):
        tasks.append(asyncio.create_task(async_with_thread(f"Task-{i}")))
    await asyncio.gather(*tasks)

# Run the asyncio event loop in the main thread
asyncio.run(main())
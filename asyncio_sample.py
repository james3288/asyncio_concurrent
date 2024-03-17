import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

# Define CPU-bound tasks
def cpu_bound_task(n):
    print(f"Task {n} started")
    result = sum(i * i for i in range(10**7))  # Simulate a CPU-bound task
    print(f"Task {n} completed")
    return result

# Asynchronous function to execute CPU-bound tasks concurrently
async def run_cpu_tasks():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as executor:
        # Submit CPU-bound tasks to the thread pool
        futures = [loop.run_in_executor(executor, cpu_bound_task, i) for i in range(3)]
        # Gather results asynchronously
        results = await asyncio.gather(*futures)
        print("All tasks completed")
        print("Results:", results)

# Run the asynchronous function
async def main():
    print("Starting...")
    await run_cpu_tasks()
    print("Finished!")

# Execute the asyncio event loop
asyncio.run(main())
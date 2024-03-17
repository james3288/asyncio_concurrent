import asyncio

# Synchronous function that performs a CPU-bound operation
def cpu_bound_operation(x, y):
    print("Performing CPU-bound operation...")
    return x + y

# Asynchronous function that calls run_in_executor() to run the CPU-bound operation asynchronously
async def async_cpu_bound_operation(x, y):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, cpu_bound_operation, x, y)
    print("Result:", result)

# Run the asynchronous function
async def main():
    await async_cpu_bound_operation(3, 5)

# Execute the asyncio event loop
asyncio.run(main())
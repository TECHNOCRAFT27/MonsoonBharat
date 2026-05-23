from concurrent.futures import ThreadPoolExecutor

def hello(name):
    print(f"Hello {name}")

with ThreadPoolExecutor(max_workers=3) as executor:

    executor.submit(hello, "Mumbai")

    executor.submit(hello, "Delhi")

    executor.submit(hello, "Pune")
from asyncio import run, sleep, wait, create_task, gather

values = [1, 5, 3, 2, 7]

async def add_after_time(result, value):
    await sleep(value / 1000)
    result.append(value)

async def sleep_sorted(values):
    result = []
    task = set()
    for v in values:
        task.add(create_task(add_after_time(result, v)))
    await gather(*task)
    return result

def main():
    print(run(sleep_sorted(values)))

main()

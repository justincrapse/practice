import asyncio


async def foo():
    print('start foo')
    await asyncio.sleep(2)
    print('end foo')


async def bar():
    print('start bar')
    await asyncio.sleep(2)
    print('end bar')


async def diddy():
    print('start diddy')
    await asyncio.sleep(2)
    print('end diddy')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar()), ioloop.create_task(diddy())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)

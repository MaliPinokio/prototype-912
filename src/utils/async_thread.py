import asyncio
import threading

class AsyncThread(threading.Thread):
    """ Wrapper that allows a thread to run async function """
    def __init__(self, target, args=None, *other_args, **kwargs):
        super().__init__(
            target=self.__translation,
            args=[target] + (args if args else [])
        )

    def __translation(self, asyncf, *args):
        """ Runs the target async function in a loop """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_until_complete(asyncf(*args))
        loop.close()
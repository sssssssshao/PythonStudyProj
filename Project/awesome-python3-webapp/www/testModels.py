import orm, asyncio
from models import User, Blog, Comment


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop, user='sfy', password='123456', db='awesome')

    u = User(name='Test', email='ddd@aa.com', passwd='123', image='about:blank')
    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
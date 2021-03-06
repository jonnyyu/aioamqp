"""
    Amqp basic tests for recover methods
"""

import asynctest

from . import testcase


class RecoverTestCase(testcase.RabbitTestCaseMixin, asynctest.TestCase):

    async def test_basic_recover_async(self):
        await self.channel.basic_recover_async(requeue=True)

    async def test_basic_recover_async_no_requeue(self):
        await self.channel.basic_recover_async(requeue=False)

    async def test_basic_recover(self):
        result = await self.channel.basic_recover(requeue=True)
        self.assertTrue(result)

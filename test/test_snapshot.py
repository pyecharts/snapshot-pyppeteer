import os
import asyncio
import unittest

from pyppeteer import launch


class TestBrowser(unittest.TestCase):
    SNAPSHOT_JS = (
        "echarts.getInstanceByDom(document.querySelector('div[_echarts_instance_]'))."
        "getDataURL({type: '%s', pixelRatio: %s, excludeComponents: ['toolbox']})"
    )

    def setUp(self) -> None:
        super().setUp()
        self.loop = asyncio.get_event_loop()

    async def _make_snapshot(self):
        html_path = "file://" + os.path.abspath("render.html")
        browser = await launch({"headless": True})
        page = await browser.newPage()
        await page.setJavaScriptEnabled(enabled=True)
        await page.goto(html_path)
        await asyncio.sleep(2)
        snapshot_js = self.SNAPSHOT_JS % ("png", 2)
        execute_js_result = await page.evaluate(snapshot_js)
        self.assertNotEqual(execute_js_result, "{}")
        await browser.close()

    async def test_snapshot_base(self):
        self.loop.run_until_complete(self._make_snapshot())

import os

import asyncio
from pyppeteer import launch

SNAPSHOT_JS = (
    "echarts.getInstanceByDom(document.querySelector('div[_echarts_instance_]'))."
    "getDataURL({type: '%s', pixelRatio: %s, excludeComponents: ['toolbox']})"
)

SNAPSHOT_SVG_JS = "document.querySelector('div[_echarts_instance_] div').innerHTML"


async def run_snapshot(
    html_path: str, file_type: str, pixel_ratio: int = 2, delay: int = 2
):
    if not html_path.startswith("http"):
        html_path = "file://" + os.path.abspath(html_path)

    browser = await launch({"headless": True})
    page = await browser.newPage()
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto(html_path)
    await asyncio.sleep(delay)

    if file_type == "svg":
        snapshot_js = SNAPSHOT_SVG_JS
    else:
        snapshot_js = SNAPSHOT_JS % (file_type, pixel_ratio)

    execute_js_result = await page.evaluate(snapshot_js)
    await browser.close()
    return execute_js_result


def make_snapshot(html_path: str, file_type: str, pixel_ratio: int = 2, delay: int = 2):
    snapshot_result = asyncio.get_event_loop().run_until_complete(
        run_snapshot(
            html_path=html_path,
            file_type=file_type,
            pixel_ratio=pixel_ratio,
            delay=delay,
        )
    )
    return snapshot_result

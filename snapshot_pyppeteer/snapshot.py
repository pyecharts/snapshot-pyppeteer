import os
import asyncio
from typing import Any

from pyppeteer import launch, connect

SNAPSHOT_JS = (
    "echarts.getInstanceByDom(document.querySelector('div[_echarts_instance_]'))."
    "getDataURL({type: '%s', pixelRatio: %s, excludeComponents: ['toolbox']})"
)

SNAPSHOT_SVG_JS = "document.querySelector('div[_echarts_instance_] div').innerHTML"


async def run_snapshot(
    html_path: str,
    file_type: str,
    pixel_ratio: int = 2,
    delay: int = 2,
    **kwargs
) -> Any:
    # You can load remote html file or local file
    if not html_path.startswith("http"):
        html_path = "file://" + os.path.abspath(html_path)

    # You can use browserless by docker(chrome browser)
    """
    $ docker pull browserless/chrome:latest
    $ docker run -d -p 3000:3000 --shm-size 2gb --name browserless --restart always \
      -e "DEBUG=browserless/chrome" -e "MAX_CONCURRENT_SESSIONS=10" \
      browserless/chrome:latest
    # the args `remoteAddress` is "ws://<server IP>:3000"
    """
    remote_address = kwargs.get("remoteAddress")
    if remote_address is not None:
        browser = await connect({"browserWSEndpoint": kwargs.get("remoteAddress")})
    else:
        browser = await launch({"headless": True})

    # Init and config code
    page = await browser.newPage()
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto(html_path)
    await asyncio.sleep(delay)

    # Generate js function
    if file_type == "svg":
        snapshot_js = SNAPSHOT_SVG_JS
    else:
        snapshot_js = SNAPSHOT_JS % (file_type, pixel_ratio)

    # execute js function
    execute_js_result = await page.evaluate(snapshot_js)

    # disconnect or close the browser session
    if remote_address is not None:
        await browser.disconnect()
    else:
        await browser.close()
    return execute_js_result


def make_snapshot(
    html_path: str, file_type: str, pixel_ratio: int = 2, delay: int = 2, **kwargs
) -> Any:
    # For notebook environment
    is_notebook = kwargs.get("notebook", False)
    if is_notebook:
        import nest_asyncio
        nest_asyncio.apply()

    snapshot_result = asyncio.get_event_loop().run_until_complete(
        run_snapshot(
            html_path=html_path,
            file_type=file_type,
            pixel_ratio=pixel_ratio,
            delay=delay,
            **kwargs
        )
    )
    return snapshot_result

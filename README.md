<h1 align="center">snapshot-pyppeteer</h1>
<p align="center">
    <em>Render pyecharts as image via pyppeteer</em>
</p>
<p align="center">
    <a href="https://github.com/sunhailin-Leo">
        <img src="https://img.shields.io/badge/Author-sunhailin--Leo-blue" alt="Author">
    </a>
</p>
<p align="center">
    <a href="https://travis-ci.org/pyecharts/snapshot-pyppeteer">
        <img src="https://travis-ci.org/pyecharts/snapshot-pyppeteer.svg?branch=master" alt="Travis Build Status">
    </a>
    <a href="https://ci.appveyor.com/project/sunhailin-Leo/snapshot-pyppeteer">
        <img src="https://ci.appveyor.com/api/projects/status/wpimbvko8d9fegjk/branch/master?svg=true" alt="Appveyor Build Status">
    </a>
    <a href="https://codecov.io/gh/pyecharts/snapshot-pyppeteer">
        <img src="https://codecov.io/gh/pyecharts/snapshot-pyppeteer/branch/master/graph/badge.svg" alt="Codecov">
    </a>
    <a href="https://badge.fury.io/py/snapshot-pyppeteer">
        <img src="https://badge.fury.io/py/snapshot-pyppeteer.svg" alt="PyPI version">
    </a>
    <a href="https://pypi.org/project/snapshot-pyppeteer/">
        <img src="https://img.shields.io/pypi/pyversions/snapshot-pyppeteer.svg?colorB=brightgreen" alt="PyPI - Python Version">
    </a>
</p>
<p align="center">
    <a href="https://pypi.org/project/snapshot-pyppeteer">
        <img src="https://img.shields.io/pypi/format/snapshot-pyppeteer.svg" alt="PyPI - Format">
    </a>
     <a href="https://github.com/pyecharts/snapshot-pyppeteer/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

## 🔰 安装

**pip 安装**
```shell
# 安装
$ pip install snapshot-pyppeteer

# 安装完后建议执行 chromium 安装命令
pyppeteer-install
```

## 📊 生成图片

* Pycharm 环境下
```python
from snapshot_pyppeteer import snapshot

from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.render import make_snapshot


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    make_snapshot(snapshot, c.render(), "bar.png")


if __name__ == '__main__':
    bar_base()
```
<p align="center">
    <img src="https://user-images.githubusercontent.com/17564655/66774139-704bf300-eef3-11e9-9cc2-6767d9650b38.png" width="85%">
</p>

* Notebook 环境下
```jupyterpython
#%%

from snapshot_pyppeteer import snapshot

from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.render import make_snapshot

#%%

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
)
make_snapshot(snapshot, c.render(), "bar.png", notebook=True)

#%%
```
<p align="center">
    <img src="https://user-images.githubusercontent.com/17564655/68744231-1859f680-062f-11ea-8385-fe677ee6b370.png" width="85%">
</p>

## ☁️ 扩展参数
* 在 `pyecharts` 的 `make_snapshot` 中允许传递 `kwargs` 类型的参数：
参数名称 | 参数类型 | 参数默认值  
-|-|-
notebook | bool | False |
remoteAddress | str | 空字符串 |

## 📃 License

MIT [©sunhailin-Leo](https://github.com/sunhailin-Leo)
## Description

Tavern のテスト

## Usage

環境の準備

```bash
pipenv install && pipenv shell
```

サーバを起動しておく

```bash
$ python sample-server.py
serving at port= 3000
```

テスト実行

```bash
$ PYTHONPATH=$PYTHONPATH:${PWD}/tests/integration pytest
================================================= test session starts ==================================================
platform linux -- Python 3.8.3, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /path/to/tavern-sample
plugins: tavern-1.16.0
collected 1 item

tests/integration/test_this-is-sample-test.tavern.yaml .                                                         [100%]

================================================== 1 passed in 0.14s ===================================================
```


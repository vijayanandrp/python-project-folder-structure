#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

PROJECT_NAME = "MyNewProject"


def create_dir(path: str) -> None:
    if not os.path.isdir(path):
        os.mkdir(path)
    return

def create_file(path: str) -> None:
    exception = False
    try:
        if not os.path.isfile(path) and '.' in path:
            with open(path, 'w') as fp:
                fp.write('')
        elif not os.path.isdir(path):
            create_dir(path)
    except FileNotFoundError:
        exception = True
        create_file(os.path.dirname(path))
    except Exception as err:
        print(err)
    if exception:
        create_file(path)


x = """
.gitignore
LICENSE.txt
README.md
bin/clean.sh
bin/start.sh
bin/stop.sh
data/config/dev.json
data/config/prod.json
data/config/qa.json
data/docs/design.md
data/docs/functional.md
data/docs/index.rst
data/docs/requirements.md
data/logs/app.log
data/schema/sample.xml
data/testdata/sample.txt
requirements.txt
setup.py
src/__init__.py
src/app/__init__.py
src/app/app.py
src/app/module1/create.py
src/app/module2/update.py
src/app/module3/delete.py
src/lib/__init__.py
src/lib/commons.py
src/lib/core.py
src/lib/config.py
src/lib/helpers.py
tests/__init__.py
tests/app_test.py
tests/core_test.py
tests/test_advanced.py
tests/test_helpers.py
"""

root_dir = os.path.dirname(os.path.abspath(__file__))
print(root_dir)
project_dir = os.path.join(root_dir, PROJECT_NAME)

if os.path.isdir(project_dir):
    shutil.rmtree(project_dir)

create_dir(project_dir)

x = [_.strip() for _ in x.split() if _.strip()]
x = list(set(x))
x.sort()


for val in x:
    path = os.path.join(project_dir, val)
    create_file(path)

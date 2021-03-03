#!/usr/bin/python3

import json
from encClient import generate

from pathlib import Path

with open("template.html") as f:
    template = f.read()
with open("template_password.html") as f:
    template_password = f.read()


def writeFile(CODE, data):
    Path(f"public/{CODE}").mkdir(parents=True, exist_ok=True)
    with open(f"public/{CODE}/index.html", "w") as g:
        g.write(data)


with open("links.json", "r") as f:
    data = json.load(f)
    for CODE in data:
        entry = data[CODE]
        if type(entry) is dict:
            if "disabled" in entry and entry["disabled"]:
                # skip
                continue
            
            content = ""
            if "password" in entry:
                content = template_password
                content = content.replace("$ENC_STRING", generate(entry["link"], entry["password"]).decode('utf-8'), 1)
            else:
                content = template
                content = content.replace("$REDIRECT_URL", entry["link"])
            
            content = content.replace("$INFO_STRING", entry.get("info", ""))
            writeFile(CODE, content)
        else:
            writeFile(CODE, template.replace("$INFO_STRING", "").replace("$REDIRECT_URL", entry))

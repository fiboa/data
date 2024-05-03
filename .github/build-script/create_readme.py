from pathlib import Path
from datetime import datetime
from jinja2 import Template
import logging
import requests
import sys

logger = logging.getLogger(__name__)

def main() -> bool:
  logger.info(f"Reading list of repositories")
  with requests.get("https://fiboa.org/stac/catalog.json") as response:
    catalog = response.json()
    data = list(filter(lambda link: link["rel"] == "child", catalog["links"]))
  
  data.sort(key = lambda x: x["title"])
  count = len(data)
  now = datetime.utcnow().strftime("%b %d %Y, %H:%M %Z")
  template = Template(Path("./README.md.jinja").read_text())

  with Path("./README.md") as f:
    f.write_text(template.render(data=data, updated=now, count=count))

  sys.exit(0)


if __name__ == "__main__":
  main()

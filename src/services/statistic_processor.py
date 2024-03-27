from datetime import datetime

from models import LinkEntity
from schemas.link_schema import LinkUpdate


class StatisticProcessor:
    @classmethod
    def handle_link(cls, link: LinkEntity) -> LinkUpdate:
        return LinkUpdate(usages=link.usages + 1, last_usage=datetime.now())

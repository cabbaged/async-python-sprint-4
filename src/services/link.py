from models.link_entity import LinkEntity as LinkModel
from schemas.link_schema import LinkCreate, LinkUpdate

from .base import RepositoryDB


class RepositoryLink(RepositoryDB[LinkModel, LinkCreate, LinkUpdate]):
    pass


link_crud = RepositoryLink(LinkModel)

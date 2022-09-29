from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

ModelType = TypeVar("ModelType", bound=object)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A beanie model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, uuid: str) -> Optional[ModelType]:
        return self.model.objects(uuid=uuid).first()

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        raise NotImplementedError()

    def update(
        self,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        raise NotImplementedError()

    def remove(self, id: int) -> ModelType:
        raise NotImplementedError()

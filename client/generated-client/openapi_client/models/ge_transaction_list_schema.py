# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from openapi_client.models.character_schema import CharacterSchema
from openapi_client.models.cooldown_schema import CooldownSchema
from openapi_client.models.ge_transaction_schema import GETransactionSchema
from typing import Optional, Set
from typing_extensions import Self

class GETransactionListSchema(BaseModel):
    """
    GETransactionListSchema
    """ # noqa: E501
    cooldown: CooldownSchema = Field(description="Cooldown details.")
    transaction: GETransactionSchema = Field(description="Transaction details.")
    character: CharacterSchema = Field(description="Character details.")
    __properties: ClassVar[List[str]] = ["cooldown", "transaction", "character"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GETransactionListSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cooldown
        if self.cooldown:
            _dict['cooldown'] = self.cooldown.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of character
        if self.character:
            _dict['character'] = self.character.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GETransactionListSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cooldown": CooldownSchema.from_dict(obj["cooldown"]) if obj.get("cooldown") is not None else None,
            "transaction": GETransactionSchema.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None,
            "character": CharacterSchema.from_dict(obj["character"]) if obj.get("character") is not None else None
        })
        return _obj



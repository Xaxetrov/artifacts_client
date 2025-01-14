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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from openapi_client.models.blocked_hits_schema import BlockedHitsSchema
from openapi_client.models.drop_schema import DropSchema
from typing import Optional, Set
from typing_extensions import Self

class FightSchema(BaseModel):
    """
    FightSchema
    """ # noqa: E501
    xp: StrictInt = Field(description="The amount of xp gained by the fight.")
    gold: StrictInt = Field(description="The amount of gold gained by the fight.")
    drops: List[DropSchema] = Field(description="The items dropped by the fight.")
    turns: StrictInt = Field(description="Numbers of the turns of the combat.")
    monster_blocked_hits: BlockedHitsSchema = Field(description="The amount of blocked hits by the monster.")
    player_blocked_hits: BlockedHitsSchema = Field(description="The amount of blocked hits by the player.")
    logs: List[StrictStr] = Field(description="The fight logs.")
    result: StrictStr = Field(description="The result of the fight.")
    __properties: ClassVar[List[str]] = ["xp", "gold", "drops", "turns", "monster_blocked_hits", "player_blocked_hits", "logs", "result"]

    @field_validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['win', 'lose']):
            raise ValueError("must be one of enum values ('win', 'lose')")
        return value

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
        """Create an instance of FightSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in drops (list)
        _items = []
        if self.drops:
            for _item in self.drops:
                if _item:
                    _items.append(_item.to_dict())
            _dict['drops'] = _items
        # override the default output from pydantic by calling `to_dict()` of monster_blocked_hits
        if self.monster_blocked_hits:
            _dict['monster_blocked_hits'] = self.monster_blocked_hits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of player_blocked_hits
        if self.player_blocked_hits:
            _dict['player_blocked_hits'] = self.player_blocked_hits.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FightSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "xp": obj.get("xp"),
            "gold": obj.get("gold"),
            "drops": [DropSchema.from_dict(_item) for _item in obj["drops"]] if obj.get("drops") is not None else None,
            "turns": obj.get("turns"),
            "monster_blocked_hits": BlockedHitsSchema.from_dict(obj["monster_blocked_hits"]) if obj.get("monster_blocked_hits") is not None else None,
            "player_blocked_hits": BlockedHitsSchema.from_dict(obj["player_blocked_hits"]) if obj.get("player_blocked_hits") is not None else None,
            "logs": obj.get("logs"),
            "result": obj.get("result")
        })
        return _obj



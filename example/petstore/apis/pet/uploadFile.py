from __future__ import annotations

import pydantic
import datetime
import asyncio
import typing

from pydantic import BaseModel

from swagger_codegen.api.request import ApiRequest


class ApiResponse(BaseModel):
    code: typing.Optional[int] = None
    type: typing.Optional[str] = None
    message: typing.Optional[str] = None


def make_request(
    self, __request__: bytes, petid: int, additionalmetadata: str = ...,
) -> ApiResponse:
    """uploads an image"""
    m = ApiRequest(
        method="POST",
        path="/api/v3/pet/{petId}/uploadImage".format(petId=petid,),
        content_type="application/json",
        body=__request__.dict(),
        headers=self._only_provided({}, exclude_none=True),
        query_params=self._only_provided(
            {"additionalMetadata": additionalmetadata,}, exclude_none=True
        ),
        cookies=self._only_provided({}, exclude_none=True),
    )
    return self.make_request({"200": {"application/json": ApiResponse,},}, m)

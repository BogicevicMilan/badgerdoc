from assets.config import minio_client
from assets.converters.text.text_to_badgerdoc_converter import (
    TextToBadgerdocConverter,
)
from assets.models.text import TextRequest
from fastapi import APIRouter, status

router = APIRouter(prefix="/text", tags=["text"])


@router.post(
    "/import",
    status_code=status.HTTP_201_CREATED,
)
def import_text(request: TextRequest) -> None:
    text_to_bd_use_case = TextToBadgerdocConverter(
        s3_client=minio_client,
    )
    text_to_bd_use_case.execute(
        s3_input_text=request.input_text,
        s3_output_pdf=request.output_pdf,
        s3_output_tokens=request.output_tokens,
    )
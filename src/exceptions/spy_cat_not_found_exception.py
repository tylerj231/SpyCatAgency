from fastapi import HTTPException, status


class SpyCatNotFoundException(HTTPException):
    def __init__(self, cat_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Spy cat with id {cat_id} was not found.",
        )

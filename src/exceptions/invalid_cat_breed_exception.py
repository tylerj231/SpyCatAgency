from fastapi import HTTPException, status


class InvalidCatBreedException(HTTPException):
    def __init__(self, breed: str) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Breed {breed} is not a valid cat breed.",
        )

from fastapi import HTTPException, status


class TargetNotFoundException(HTTPException):
    def __init__(self, target_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Target by {target_id} is not found.",
        )

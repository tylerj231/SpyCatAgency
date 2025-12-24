from fastapi import HTTPException, status


class MissionCompleteException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot update notes as mission is already complete.",
        )


class MissionCompleteExceptionTarget(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot update notes the target is complete.",
        )

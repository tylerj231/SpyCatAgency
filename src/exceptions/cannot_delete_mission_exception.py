from fastapi import HTTPException, status


class CanNotDeleteMissionException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Can not delete a mission with assigned spy cat.",
        )

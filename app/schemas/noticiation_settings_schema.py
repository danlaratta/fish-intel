from pydantic import BaseModel


class NotificationSettingsBase(BaseModel):
    pass 


class NotificationSettingsCreate(NotificationSettingsBase):
    pass


class NotificationSettingsUpdate(NotificationSettingsBase):
    pass


class NotificationSettingsResponse(NotificationSettingsBase):
    id: int 

    class Config:
        from_attributes = True
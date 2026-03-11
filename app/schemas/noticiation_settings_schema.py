from pydantic import BaseModel


class NotificationSettingsBase(BaseModel):
    score_alert_threshold: float 
    email_notifications_enabled: bool = True


class NotificationSettingsCreate(NotificationSettingsBase):
    pass


class NotificationSettingsUpdate(NotificationSettingsBase):
    pass


class NotificationSettingsResponse(NotificationSettingsBase):
    id: int 
    user_id: int 

    class Config:
        from_attributes = True
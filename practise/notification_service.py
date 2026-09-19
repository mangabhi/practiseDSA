from abc import ABC ,abstractmethod
class NotificationService(ABC):

    @abstractmethod
    def send(self,recipient:str,message:str)->None:
        pass

class EmailNotification(NotificationService):
    def send(self,recipient:str,message:str)->None:
            print(f"[Email] to : {recipient} | {message}")

class SlackNotification(NotificationService):
    def send(self,recipient:str,message:str)->None:
            print(f"[Slack] to : {recipient} | {message}")

class WebhookNotification(NotificationService):
    def send(self,recipient:str,message:str)->None:
            print(f"[Webhook] to : {recipient} | {message}")

class AlertService:
    def __init__(self,notifier:NotificationService):
        self._notifier=notifier

    def trigger_alert(self,recipient:str,issue:str)->None:
        alert_message=f"Alert {issue}"
        self._notifier.send(recipient,alert_message)


email_alerts = AlertService(EmailNotification())
email_alerts.trigger_alert("ops@company.com", "CPU usage at 95%")

slack_alerts = AlertService(SlackNotification())
slack_alerts.trigger_alert("#incidents", "Database connection pool exhausted")

webhook_alerts = AlertService(WebhookNotification())
webhook_alerts.trigger_alert("https://hooks.example.com/alerts", "Disk usage at 90%")
           
      

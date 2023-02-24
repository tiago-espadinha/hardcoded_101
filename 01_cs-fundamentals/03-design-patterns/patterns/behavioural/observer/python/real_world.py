import asyncio
from pattern import EventEmitter

class UserManagementSystem:
    def __init__(self):
        self.events = EventEmitter[dict]()
        
    async def create_user(self, username: str, email: str):
        print(f"Creating user: {username}")
        # Logic to save user to DB would go here
        
        # Notify observers
        await self.events.emit("user_created", {"username": username, "email": email})

class EmailService:
    async def send_welcome_email(self, data: dict):
        print(f"EmailService: Sending welcome email to {data['email']}...")
        await asyncio.sleep(0.2)
        print("EmailService: Welcome email sent.")

class AnalyticsService:
    def log_user_signup(self, data: dict):
        print(f"AnalyticsService: Logging signup for {data['username']}")

async def main():
    ums = UserManagementSystem()
    email_service = EmailService()
    analytics_service = AnalyticsService()
    
    # Register observers
    ums.events.on("user_created", email_service.send_welcome_email)
    ums.events.on("user_created", analytics_service.log_user_signup)
    
    await ums.create_user("jane_doe", "jane@example.com")

if __name__ == "__main__":
    asyncio.run(main())

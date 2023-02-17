/**
 * Facade pattern implementation for a Notification System
 * ES2022 Node.js environment
 */

// Subsystem Classes
class EmailService {
  send(user, message) {
    console.log(`EmailService: sending email to ${user.email}: "${message}"`);
  }
}

class SMSService {
  send(user, message) {
    console.log(`SMSService: sending SMS to ${user.phone}: "${message}"`);
  }
}

class PushNotificationService {
  send(user, message) {
    console.log(`PushNotificationService: sending push notification to ${user.deviceId}: "${message}"`);
  }
}

// The Facade
class NotificationFacade {
  #emailService;
  #smsService;
  #pushService;

  constructor() {
    this.#emailService = new EmailService();
    this.#smsService = new SMSService();
    this.#pushService = new PushNotificationService();
  }

  /**
   * Simple interface to send notification across multiple channels.
   * @param {Object} user User data.
   * @param {string} message Message to send.
   */
  send(user, message) {
    console.log(`\n--- Dispatching Notifications for ${user.name} ---`);
    
    // Logic can be added here to choose only certain channels based on user preferences.
    this.#emailService.send(user, message);
    this.#smsService.send(user, message);
    this.#pushService.send(user, message);
    
    console.log("--- All notifications dispatched ---");
  }
}

// Client Code
const user = {
  name: "John Doe",
  email: "john@example.com",
  phone: "+1-555-010-999",
  deviceId: "DEVICE_ID_789"
};

const notificationFacade = new NotificationFacade();
notificationFacade.send(user, "Hello! Your package has been shipped.");

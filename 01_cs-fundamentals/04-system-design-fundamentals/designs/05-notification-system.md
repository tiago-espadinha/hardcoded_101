# Design 05: Notification System

## Requirements
- **Functional requirements**:
  - Send real-time notifications via Push (iOS/Android), Email, and SMS.
  - Support for bulk/fanout notifications (e.g., news alerts to millions of users).
  - User preference management (allow/disallow specific notification types).
  - Track delivery status (sent, delivered, failed).
- **Non-functional requirements**:
  - **High Throughput**: Capable of sending 100M notifications per day, with bursts of 10k/sec.
  - **Low Latency**: Notifications should be delivered within seconds of being triggered.
  - **Reliability**: No notification should be lost (at-least-once delivery).
  - **Scalability**: Support up to 1B users.

## Capacity Estimation
- **Users**: 1B users, 100M active.
- **Volume**: 100M notifications/day.
- **Average Payload**: 1KB per notification (text, metadata, URLs).
- **Storage**: 100M * 1KB = 100 GB/day. To keep 1 month of logs: 3 TB.
- **Throughput**:
  - Average: 100M / 86,400 ≈ 1,150 notifications/sec.
  - Peak: 1,150 * 10 = 11,500 notifications/sec.

## High-Level Architecture
```
[Notification API] -> [Validator] -> [Priority Queues (Kafka)]
        |                                    |
[Preference DB]                      [Notification Workers]
                                             |
                                  +----------+----------+
                                  |          |          |
                                [FCM]    [SendGrid] [Twilio]
                                (Push)     (Email)    (SMS)
```
- **Notification API**: Entry point for internal services to trigger notifications.
- **Priority Queues (Kafka)**: Decouples the API from the heavy work of sending. Allows for different priorities (e.g., OTP vs. marketing).
- **Workers**: Asynchronous processes that consume from Kafka, fetch user tokens/emails, and call 3rd-party providers.
- **FCM/SendGrid/Twilio**: External vendors that handle the actual delivery.

## Data Model
- **Table: `users`**
  - `user_id` (PK), `email`, `phone_number`, `device_tokens` (json).
- **Table: `notification_preferences`**
  - `user_id` (FK), `type` (email/push/sms), `enabled` (boolean).
- **Table: `notification_history`** (NoSQL for write throughput)
  - `notif_id` (PK), `user_id`, `status` (queued/sent/failed), `created_at`, `payload`.

## Key Design Decisions
1. **Push vs. Pull Workers**: Chose **Push-based workers** that consume from Kafka. This allows for high throughput and easy scaling by adding more worker instances.
2. **At-Least-Once Delivery**: Achieved by using Kafka's message persistence and workers acknowledging only *after* a successful response from the 3rd-party provider.
3. **Database Selection**: Chose **Cassandra/DynamoDB** for notification logs. With 100M writes per day, a relational database would struggle with write IOPS and table size.

## Bottlenecks & How to Scale
1. **Third-Party Provider Limits**: Providers like Twilio or FCM have rate limits. Implement **Rate Limiting & Backoff** in the workers to prevent being banned and to handle temporary provider outages.
2. **Fanout (Million Follower Problem)**: Sending a notification to 10M followers of a celebrity. Use **Batching & Segmenting** the fanout into multiple smaller Kafka topics or messages to avoid blocking other users.
3. **Queue Backlog**: During peak events (e.g., World Cup), the queue can grow indefinitely. Implement **Priority Queues** so critical notifications (OTPs) bypass marketing blasts.

## What I Would Do Differently at 10x Scale
- **Dedicated Worker Clusters**: Separate worker clusters for each notification type (Push, Email, SMS) to isolate failures.
- **Intelligent Routing**: Automatically switch between providers (e.g., from SendGrid to Mailgun) if one provider's latency increases or delivery rate drops.
- **Regional Deployment**: Deploy notification workers close to the provider's data centers or user's regions to minimize network latency.

from abc import ABC, abstractmethod
from typing import Dict


class PaymentGateway(ABC):
    """
    The Target interface our application uses for all payment processing.
    """

    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> bool:
        pass


class StripeSDK:
    """
    A third-party payment SDK (Adaptee) with an incompatible interface.
    """

    def make_charge(self, charge_data: Dict[str, any]) -> str:
        # Complex charge logic with different naming conventions
        print(f"Stripe: Processing ${charge_data['amount_cents']/100} "
              f"{charge_data['curr']}")
        return "charge_id_123"


class StripeAdapter(PaymentGateway):
    """
    The Adapter that bridges StripeSDK to our PaymentGateway interface.
    """

    def __init__(self, stripe_sdk: StripeSDK) -> None:
        self.stripe_sdk = stripe_sdk

    def process_payment(self, amount: float, currency: str) -> bool:
        # Translating internal call to third-party SDK format
        charge_data = {
            "amount_cents": int(amount * 100),
            "curr": currency.lower()
        }
        charge_id = self.stripe_sdk.make_charge(charge_data)
        return charge_id is not None


class PayPalSDK:
    """
    Another third-party payment SDK (Adaptee) with another interface.
    """

    def send_payment(self, amt: float, ccy: str) -> bool:
        print(f"PayPal: Sending {amt} {ccy}")
        return True


class PayPalAdapter(PaymentGateway):
    """
    The Adapter that bridges PayPalSDK to our PaymentGateway interface.
    """

    def __init__(self, paypal_sdk: PayPalSDK) -> None:
        self.paypal_sdk = paypal_sdk

    def process_payment(self, amount: float, currency: str) -> bool:
        return self.paypal_sdk.send_payment(amount, currency)


def process_order(gateway: PaymentGateway, amount: float):
    """
    Client code that works with any PaymentGateway.
    """
    if gateway.process_payment(amount, "USD"):
        print("Order: Payment successful!\n")
    else:
        print("Order: Payment failed!\n")


if __name__ == "__main__":
    # Our app can work with any provider via adapters
    print("Scenario 1: Using Stripe")
    stripe_adapter = StripeAdapter(StripeSDK())
    process_order(stripe_adapter, 99.99)

    print("Scenario 2: Using PayPal")
    paypal_adapter = PayPalAdapter(PayPalSDK())
    process_order(paypal_adapter, 49.50)

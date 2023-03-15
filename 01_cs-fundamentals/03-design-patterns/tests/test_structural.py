import pytest
import time
from unittest.mock import Mock, patch
from patterns.structural.adapter.python.pattern import PayPalPayment, StripeAdapter
from patterns.structural.decorator.python.pattern import retry
from patterns.structural.proxy.python.pattern import RealAPI, CachingProxy

def test_adapter_invariant():
    paypal = PayPalPayment()
    adapter = StripeAdapter(paypal)
    # The adapter should call make_payment on the adaptee
    assert adapter.pay(100) == "Payment of $100 processed via PayPal."

def test_proxy_caching_invariant():
    real_api = Mock(spec=RealAPI)
    real_api.get_data.return_value = "Mocked Data"
    
    proxy = CachingProxy(real_api, ttl=10)
    
    # First call: real API called
    proxy.get_data("/test")
    assert real_api.get_data.call_count == 1
    
    # Second call: cached, real API NOT called
    proxy.get_data("/test")
    assert real_api.get_data.call_count == 1

def test_decorator_retry_invariant():
    mock_func = Mock()
    mock_func.side_effect = [ValueError("Failed"), "Success"]
    
    @retry(retries=3, delay=0.1)
    def decorated_func():
        return mock_func()
        
    result = decorated_func()
    assert result == "Success"
    assert mock_func.call_count == 2

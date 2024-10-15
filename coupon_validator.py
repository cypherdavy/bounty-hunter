import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import argparse

class CouponValidator:
    def __init__(self, base_url, coupon_endpoint, browser_driver_path):
        self.base_url = base_url
        self.coupon_endpoint = coupon_endpoint
        self.driver = webdriver.Chrome(browser_driver_path)
    
    def brute_force_coupons(self, coupon_list):
        """Brute force coupon codes to see if any invalid ones are accepted."""
        for coupon in coupon_list:
            response = requests.post(
                self.base_url + self.coupon_endpoint,
                data={'coupon_code': coupon}
            )
            if self.is_valid_response(response):
                print(f"Coupon {coupon} is accepted! Possible vulnerability.")
            else:
                print(f"Coupon {coupon} is correctly rejected.")
    
    def is_valid_response(self, response):
        """Determine if the coupon application was incorrectly accepted."""
        if response.status_code == 200 and "discount_applied" in response.text:
            return True
        return False

    def parameter_manipulation(self, coupon_code):
        """Test if parameter manipulation can bypass restrictions."""
        manipulated_url = f"{self.base_url}/checkout?coupon={coupon_code}"
        self.driver.get(manipulated_url)
        # Add checks for changes in price or discounts applied
        if "discount" in self.driver.page_source:
            print(f"Parameter manipulation successful with coupon {coupon_code}.")
        else:
            print(f"Parameter manipulation failed with coupon {coupon_code}.")
        
    def test_rate_limiting(self, coupon_code):
        """Test if the system allows applying the same coupon multiple times."""
        for i in range(5):  # Test with multiple requests
            response = requests.post(
                self.base_url + self.coupon_endpoint,
                data={'coupon_code': coupon_code}
            )
            if self.is_valid_response(response):
                print(f"Rate limiting failed: Coupon applied {i+1} times.")
            else:
                print(f"Rate limiting is functioning correctly at attempt {i+1}.")
    
    def close(self):
        """Close the browser session."""
        self.driver.quit()

def main():
    parser = argparse.ArgumentParser(description="Advanced Coupon Validator Tool")
    parser.add_argument('--base-url', required=True, help='The base URL of the target website')
    parser.add_argument('--coupon-endpoint', required=True, help='The endpoint for applying coupons')
    parser.add_argument('--browser-driver-path', required=True, help='Path to the Chrome WebDriver')
    parser.add_argument('--coupon-list', nargs='+', required=True, help='List of coupon codes to test')

    args = parser.parse_args()

    validator = CouponValidator(args.base_url, args.coupon_endpoint, args.browser_driver_path)
    validator.brute_force_coupons(args.coupon_list)
    for coupon in args.coupon_list:
        validator.parameter_manipulation(coupon)
        validator.test_rate_limiting(coupon)
    validator.close()

if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod


class Middleware(ABC):
    def __init__(self,next=None):
        self.next:Middleware = next
        
    @abstractmethod
    def check(self,request):
        raise NotImplementedError
        
class TokenValidationMiddleware(Middleware):
    def check(self, request):
        if not request.get("token"):
            print("Access Denied: No token provided")
            return False
        return self.next.check(request) if self.next else True
    
class RateLimitingMiddleware(Middleware):
    
    def __init__(self, next=None,limit=4):
        super().__init__(next)
        self.request_count = {}
        self.limit = limit
        
    def check(self, request):
        user = request.get("user")
        if user not in self.request_count:
            self.request_count[user] = 0
        
        self.request_count[user] += 1
        
        if self.request_count[user] > self.limit:
            print("Access Denied: Rate limit exceeded.")
            return False
        
        return self.next.check(request) if self.next else True
    
class RoleBasedAccessMiddleware(Middleware):
    def __init__(self, next=None,role="admin"):
        super().__init__(next)
        self.role = role
    def check(self, request):
        if request.get("role") != self.role:
            print("Access Denied: Insufficient permissions")
            return False
        return self.next.check(request) if self.next else True

    
if __name__ == "__main__":
    role_check = RoleBasedAccessMiddleware(role="admin")
    rate_limiter = RateLimitingMiddleware(role_check,5)
    token_validator = TokenValidationMiddleware(rate_limiter)
    # Test cases
    request1 = {"user": "Alice", "token": "valid123", "role": "admin"}
    request2 = {"user": "Bob", "token": "valid456", "role": "user"}
    request3 = {"user": "Eve", "role": "admin"}
    request4 = {"user": "Alice", "token": "valid123", "role": "admin"}

    # Simulating multiple requests from the same user (rate limiting test)
    token_validator.check(request1)
    for _ in range(5):  
        token_validator.check(request1)
    token_validator.check(request2)
    token_validator.check(request3)
    token_validator.check(request4)


# defines the shape API accepts and returns
from pydantic import BaseModel

# information returned after login
class Token(BaseModel):
  access_token: str # token user uses to prove they're authenticated
  token_type: str # tells client what type of token to use

# information extracted from a token
class TokenData(BaseModel):
  username: str | None = None # username can be str or None & if no username is provided it defaults to None

# information used to register a user
class UserCreate(BaseModel):
  username: str
  email: str
  password: str

# information API return (no passwords/hashed passwords here!)
class UserResponse(BaseModel):
  username: str
  email: str | None = None # email is optional

# inherits from UserResponse so contains the above + hashed_password
class UserInDB(UserResponse):
  hashed_password: str
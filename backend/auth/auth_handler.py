import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from database import get_db
from schemas import TokenData
from models import User

SECRET_KEY= 'qqwertyuuiopp'
ALGORITHM= 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES= 30 # expires after 30 minutes

password_hash= PasswordHash.recommended()
# looks for token in request header. the url is where the token is obtained
oauth2_scheme= OAuth2PasswordBearer(tokenUrl='auth/token')

app= APIRouter()

# comppare whether the password and hashed ver are similar
def verify_password(plain_password, hashed_password):
  return password_hash.verify(plain_password, hashed_password)

# hash password
def get_password_hash(password):
  return password_hash.hash(password)

# get user
def get_user(db: Session, username: str):
  db_user= db.query(User).filter(User.username == username).first()
  return db_user

# authenticate user
def authenticate_user(db: Session, username: str, password: str):
  user= get_user(db, username)
  if not user:
    return False
  if not verify_password(password, user.hashed_password):
    return False

  return user

# creates token user receives after successful login
def create_access_token(data: dict, expires_delta: timedelta | None = None): # timedelta == duration
  # data = token data 
  to_encode= data.copy()
  # calculate expiration time
  if expires_delta:
    expire= datetime.now(timezone.utc) + expires_delta
  else:
    expire= datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # if no duration was given default is 30

  # add the expiration to the token data
  to_encode.update({'exp': expire})

  # sign the token
  encoded_jwt= jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

  return encoded_jwt

# identify who is making a request
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db) # Depends tells FastAPI where to get the values
):
  # 401 unauthorized error if token cannot be validated/ user not found
  credentials_exception= HTTPException(
    status_code=401, 
    detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'}
  )
  try:
    # decode token
    payload= jwt.encode(token, SECRET_KEY, algorithms=[ALGORITHM])
    # extract username
    username: str = payload.get('sub')
    if username is None:
      raise credentials_exception
    token_data= TokenData(username=username)

  except InvalidTokenError:
    raise credentials_exception

  user= db.query(User).filter(User.username == token_data.username).first()
  if user is None:
    raise credentials_exception
  
  return user

# getting the authenticated user
async def get_current_active_user(
    current_user: User= Depends(get_current_user)
):
  return current_user
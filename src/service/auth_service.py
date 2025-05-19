# import src.repository.auth_repository as AuthRepository

# from src.middleware.custom_error import CustomError
# from src.utils import hashing, jwt_utils

# async def register(name, email, password):
#     user = await AuthRepository.findAccountByEmail(email)

#     if user is not None:
#         raise CustomError(400, 'email already used')
    
#     hashedpass = await hashing.hash_pass(password)

#     account = await AuthRepository.registerAccount(name, email, hashedpass.decode('utf-8'))

#     payload = {
#         'user_id': account.id,
#         'email': account.email,
#         'role': account.role
#     }

#     token = jwt_utils.jwt_encode(payload)

#     return token
    
# async def login(email, password):
#     user = await AuthRepository.findAccountByEmail(email)

#     if user is None:
#         raise CustomError(403, 'user not found')
    
#     isPasswdTrue = await hashing.compare(password, user.password)

#     if not isPasswdTrue:
#         raise CustomError(403, 'invalid cred')
    
#     payload = {
#         'user_id': user.id,
#         'email': user.email,
#         'role': user.role
#     }

#     token = jwt_utils.jwt_encode(payload)

#     return token

# async def me(token):
#     data_decode = jwt_utils.jwt_verify(token)

#     if data_decode is None:
#         raise CustomError(403, 'invalid token')
    
#     user = await AuthRepository.findAccountByEmail(data_decode['data']['email'])

#     if not user:
#         raise CustomError(400, 'user not found')
    
#     detail = await AuthRepository.getMe(user.id)
    
#     list_dict = [{'box_id': box.id} for box in detail.boxes]

#     return {
#         'user_id': user.id,
#         'name': user.name,
#         'email': user.email,
#         'boxes': list_dict
#     }
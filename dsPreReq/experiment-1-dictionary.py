# Author: Prasad Chavan 19UME305
# Write a python program to demonstrate dictionaries & related functions using python.

# create a dictionary named profile
profile = {
  'age' : 20 ,
  'username' : 'Cobra',
  'weapon' : 'Sword',
  'is_active' : True,
  'clan' : 'TP'
}

print(profile.keys()) # print all key and value pairs

profile.update({'weapon' : 'Gun'})
print(profile['weapon']) # print updated value for key weapon

profile.update({'is_banned' : False})
print(profile['is_banned']) # update is_banned key

profile['is_banned'] = True # update is_banned key by assignment
print(profile['is_banned']) 

profile2 = profile.copy() # copy data from profile into profile2
profile2.update({
  'age' : 18,
  'username' : 'Kai'
}) # update profile2 with other players info
print(profile2)
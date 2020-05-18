# Short Circuiting 4_62

# is_friend = True
# is_user = False

# if is_friend or is_user:
#   print('best friends forever')

# Logical operator 4_63

# print('<' > ';')
# print(1 < 2 < 3 <= 3)
# print( 'a' != 'b' )

# # < > <= >= !=

# # and or next not
# print(not(False))

# print(not( 1==2 ))

# 4_64

is_magician = False
is_expert = True

# check if magician AND expert : "you are a master magician"
# check if magician but not expert : "at least you're getting there"
# if you're not a magician : "You need magic powers"

if is_magician and is_expert:
  print("you are a master magician")
elif is_magician and not is_expert:
  print("at least you're getting there")
elif not is_magician:
  print("You need magic powers")


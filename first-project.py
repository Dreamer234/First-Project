import sys
import time

def undertale(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  print()

undertale("I love Undertale!")

def silk(text, waiting_time):
  undertale(text)
  time.sleep(waiting_time)
  print()

silk("... and I love Silksong!", 2.0)

def hollow(text):
  undertale(text)
  return input()

silk("and I love Hollow Knight too!", 1.0)
answer = hollow(" do you like Hollow Knight?")
if answer == "yes":
  silk("sounds good!", 1.0)
elif answer == "no":
  silk("OMG! Hollow Knight is the best game in the world (in my opinion)", 1.0)
silk("that's all...", 1.0)
undertale("thank you for reading these :)")

print("Here you are going to generate your own story by giving answers to just few questions.")
while True:
   adjective_1=input("Enter any adjective you like: ")
   place=input("Enter a place you like: ")
   animal=input("Enter any animal: ")
   emotion=input("Enter an emotion(you might want it to be sad): ")
   object=input("Enter any object: ")
   character=input("Enter the name of a character: ")
   print("Few more question to go")
   terrain=input("Enter any terrain like piece of land: ")
   weather_condition=input("Enter any weather condition: ")
   place2=input("Enter another place you like:")
   emotion2=input("Enter another emotion(you might want it to be happy): ")
   print("Last question comeon you can do this")
   adverb=input("Enter an adverb:")
   print(f"""In the {adjective_1} land of {place}, a {animal} was feeling {emotion}. The {animal} had lost its {object}.
Suddenly, a {character} appeared. 'I will help you find your {object},' they said.
Together, they journeyed through {terrain} and faced the {weather_condition}.
Finally, they found the {object} in a {place2}. The {animal} was so {emotion2} and thanked the {character}.
They lived {adverb} ever after.""")
   i=input("Wanna play again(y/n)? ")
   if i.lower()!="y":
      break
    
      


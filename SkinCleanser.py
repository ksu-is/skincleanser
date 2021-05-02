#first we will be giving the consumer a basic understanding of what this program will do
print("Thank you for choosing Skin Cleanser Finder to figure out the best skin care for you! We will start off with giving some basic insight on the different skin types.")
#now we are going to start by giving them information
print("There's 3 main types of skin, oily, dry and combonation. To start off we will explain and then from there you could get an idea and hopefully that will help you find which sounds like you. Dry skin type is usually described and dehydrated, flaky and cracked. Oily skin is usually described as greasy, shiny, and clogged pores.Finally combonation skin is usually described as a little bit of both, meaning you could be dry around your chin and oily in your t-zone.")
#now I will ask the consumer for their input to start getting an idea
consumer_answer=input("After reading through the top what kind of skin do you think you lean towards?(dry, oily, combo): ")
#next we will use the if method to help them find the best cleanser
if consumer_answer.lower() == "dry":
    print("We recommend the CerVa hydrating for 11.99")
elif consumer_answer.lower() == "oily":
    print("We recommend a cleanser that is more for Dermalogica Dermal Clay Cleanser for 22")
elif consumer_answer.lower() == "combo":
    print("We recommend the philosophy Purity Made simpe one-step paraben free facial cleanser")
else:
    print("Please start the program over and read through the instructions to find your best fit! (:")

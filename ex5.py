name = 'Sabrina Tee'
age = 25
height_inches = 65
height_cm = height_inches * 2.54
weight_lbs = 170
weight_kg = weight_lbs / 2.2
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print 'Weight in kg -', round(weight_kg), 'kg'
print 'Height in cm -', height_cm, 'cm'

print "Let's talk about %s." % name
print "She's %d inches tall." % height_inches
print "She's %d pounds heavy." % weight_lbs
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print 'Her teeth are usually %s depending on the coffee.' % teeth

print "If I add %d, %d, and %d I get %d." % (age, height_inches, weight_lbs, age + height_inches + weight_lbs) #260

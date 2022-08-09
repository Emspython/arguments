# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Define function greet with 2 arguments in following order
# A name
# a greeting template (str) templ parameter "hello, <name>!"

def greet(name, greeting = 'Hello, <name>!'):

    return greeting.replace('<name>', name)   

# write function force with 2 arguments mass(float), body(str)
# earth is the default

def force(mass, body = 'earth'):

    gravity = {
        "sun": 274.0,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    force = mass * gravity [body]
    return force

# Write a function pull that takes three arguments:
# m1 An object's mass in kg (float)
# m2 Another object's mass in kg (float)
# d Their distance in meters (float)

def pull(m1, m2, d):
    pull = (6.674 * 10 ** -11) * ((m1 * m2) / d ** 2)

    return pull

if __name__ == "__main__":
    print(greet("Michiel"))
    print(force(2))
    print(pull(1, 2, 10))
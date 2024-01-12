
train_mass = 22680
train_acceleration = 10
bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp*(9/5) + 32

c0_in_fahrenheit= c_to_f(0)

def get_force(mass, accceleration):
  return mass*accceleration

train_force = get_force(train_mass,train_acceleration)
print(train_force)
x = train_force
print("The GE train supplies", x ," Newtons of force.")
c= 3*10**8
def get_energy(mass,c):
  return mass*(c*c)

bomb_energy = get_energy(bomb_mass,c)
x = bomb_energy
print("A 1kg bomb supplies", x ,"Joules")

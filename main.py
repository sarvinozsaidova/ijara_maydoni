from manager import Manager

manager = Manager()

flat1 = manager.newFlat(23, 'yunusabot')

tariffs = [100, 150, 200]
manager.setTariffs(flat1, tariffs)

print(flat1.getCode()) 
print(flat1.getDimention()) 
print(flat1.getTariffs()) 

client1 = manager.newClient('Sarvinoz', 'Saidova', 24)

print(client1.getName()) 
print(client1.getSurname()) 
print(client1.getID())  

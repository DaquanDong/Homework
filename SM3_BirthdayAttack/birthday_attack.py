from pysmx.SM3 import SM3, hash_msg
import math
import os

def getRandomList(n, m):
	numbers = []
	while len(numbers) < n:
		i = os.urandom(m)
		if i not in numbers:
			numbers.append(i)
	return numbers

def brithAttack(m):
	sm3 = SM3()
	sqrt_m = int(math.sqrt(2**(m * 8)))
	list_k_value = {}
	list_l_value = {}
	list_k = getRandomList(sqrt_m, m)
	list_l = getRandomList(sqrt_m, m)
	for i in range(sqrt_m):
		sm3.update(list_k[i])
		item_k = sm3.hexdigest()
		list_k_value.update({item_k: list_k[i]})

		sm3.update(list_l[i])
		item_l = sm3.hexdigest()
		list_l_value.update({item_l: list_l[i]})

	print(list_k_value)
	print(list_l_value)
	coincide = set(list_k_value.keys()) & set(list_l_value.keys())
	#print(coincide)
	if not coincide:
		return False
	else:
		for same in coincide:
			print(same)
			print(list_k_value.get(same))
			print(list_l_value.get(same))
			print("-----------next-----------")
		return True

def birth_attack(n):
	hash_dict = {}
	for i in range(0, int(math.sqrt(pow(2, n*8)))):
		mes = os.urandom(n)
		print(mes)
		hash_m = hash_msg(mes)# [0:n*8]
		if hash_m in hash_dict.keys():
			print('Succeed')
			print("{} and {} have same hash mes:{}".format(hash_dict.get(hash_m), mes, hash_m))
			# print(hash_dict)
			return True
		hash_dict[hash_m] = mes
	print("Failed")


if __name__ == '__main__':
	while True:
		if birth_attack(4):
			break

#Отримати мій номер гри
#Written by: you!
puts "Ласкаво просимо до 'Отримати мій номер гри'"
puts "Яке ваше ім'я?"
input = gets
name = input.chomp
puts "Привіт, #{name}!".inspect

#Сохранение случайного числа
puts "У мене є випадкове число від 1 до 100."
puts "Чи можете ви вгадати його"
target = rand(100) + 1

#Количество попиток
num_quesses = 0

#Цикл на продолжение игри
quessed_it = false

until num_quesses == 10 || quessed_it 
	puts "Ви отримали #{10 - num_quesses} що залишилося"
	print "Ввелить своє число: "
	quess = gets.to_i
	
	num_quesses += 1

#Порівнювання числа
	if quess < target
		puts "На жаль. Ваша цифра замала."
	elsif quess > target
		puts "На жаль. Ваша цифра завелика"
	elsif quess == target
		puts "Хороша робота, #{name}!"
		puts "Ви вгадали мій номер #{target}!"
		quessed_it = true
	end
end

#Если попыток неосталось
unless quessed_it
	puts "Вибачте. Ви не вгадали мій номер, (Це було #{target}.)"
end
	
	
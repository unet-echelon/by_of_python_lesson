def say_hello(name)
	puts "Hello #{name}"
end
name = ARGV[0].to_s
say_hello(name)
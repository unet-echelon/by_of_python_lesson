def accelerate
	puts "Stepping on the gas"
	puts "Speeding up"
end
def sound_horn
	puts "Pressing the horn button"
	puts "Beep beep"
end
def use_headlights (brightness = "low-beam")
	puts "Turning on #{brightness} headlights"
	puts "Watch out for deep!"
end
sound_horn
sleep 2
accelerate
sleep 2
use_headlights
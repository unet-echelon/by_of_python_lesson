def mileage(miles_drive, gas_used)
	if gas_used == 0
		return 0.0		
	end
	miles_drive / gas_used
end

trip_mileaget = mileage(400, 0)
puts "You got #{trip_mileaget} MPG on this trip"
lifetime_mileage = mileage(11432, 366)
puts "This car averages #{lifetime_mileage} MPG"
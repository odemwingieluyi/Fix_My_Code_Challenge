###
#
#  Sorts integer arguments in ascending order
#
###

result = []

# Iterate over each argument provided in the command line
ARGV.each do |arg|
    # Ignore the argument if it is not a valid integer
    next if arg !~ /^-?[0-9]+$/

    # Convert the valid integer argument from string to integer type
    i_arg = arg.to_i

    # Initialize variables to track if the integer has been inserted
    # and to keep track of the current position in the result array
    is_inserted = false
    i = 0
    l = result.size

    # Loop through the current result array to find the correct position
    # for the new integer
    while !is_inserted && i < l do
        # If the current element in result is less than the new integer,
        # move to the next position
        if result[i] < i_arg
            i += 1
        else
            # Insert the new integer at the correct position
            result.insert(i, i_arg)
            is_inserted = true
            break
        end
    end

    # If the integer was not inserted (it is larger than all current elements),
    # append it to the end of the result array
    result << i_arg if !is_inserted
end

# Output the sorted list of integers
puts result


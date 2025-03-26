import streamlit as st
import math

# Coin distribution function
def divide_up_coins(num_people, num_coins):
    # Check that inputs are integers greater than 0:
    if num_people <= 0 or not isinstance(num_people, int):
        return "Error: Number of party members must be an integer greater than 0"
    if num_coins <= 0 or not isinstance(num_coins, int):
        return "Error: Number of coins must be an integer greater than 0"
    
    # Calculate coin distribution:
    division = math.ceil(num_coins / num_people)
    remainder = num_coins % num_people
    # Even distribution:
    if remainder == 0: 
        result = [division] * num_people
    # Uneven distribution:
    else:
        result = [division] * remainder
        result += [division - 1] * (num_people - remainder) 
    
    # Return an array of integers containing the correct distribution
    return result

#####################################################################################

# Title using default streamlit UI:
st.title('Prestigious Coin Distribution App')

# User inputs:
num_people = st.number_input("Number of Party Members:", min_value = 1, step = 1)
num_coins = st.number_input("Number of Coins:", min_value = 1, step = 1)

# Button to calculate distribution
if st.button("Calculate Distribution"):
    # Call coin distribution function:
    coin_dist = divide_up_coins(num_people, num_coins)

    # Format the result as a string with commas between the values
    if isinstance(coin_dist, list):
        formatted_result = ', '.join(map(str, coin_dist))
        st.write(f"Coin Distribution: {formatted_result}")
    else:
        st.write(coin_dist)  # Return error message
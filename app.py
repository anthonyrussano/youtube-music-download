# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "browser-cookie3",
# ]
# ///

import browser_cookie3
import time

# Define the path for the output cookies.txt file
output_file = 'cookies.txt'

# Get the current time as a UNIX timestamp
current_time = int(time.time())

# Fetch cookies for youtube.com specifically from the Brave browser
cookies = browser_cookie3.brave(domain_name='youtube.com')

# Function to format cookies in Netscape format
def format_cookie(cookie):
    domain = cookie.domain
    flag = 'TRUE' if cookie.domain.startswith('.') else 'FALSE'
    path = cookie.path
    secure = 'TRUE' if cookie.secure else 'FALSE'
    expiration = str(cookie.expires) if cookie.expires else str(current_time + 31536000)  # 1 year expiration if not set
    name = cookie.name
    value = cookie.value
    
    return f"{domain}\t{flag}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n"

# Write the cookies to the file in the Netscape format
with open(output_file, 'w') as f:
    # Write the header for the Netscape format
    f.write("# Netscape HTTP Cookie File\n")
    f.write("# This is a generated file! Do not edit.\n\n")
    
    # Write each cookie in the correct format
    for cookie in cookies:
        f.write(format_cookie(cookie))

print(f"Cookies saved to {output_file}")


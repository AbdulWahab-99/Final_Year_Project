import pandas as pd

# Sample DataFrame with a column named "city"
data = {'city': ['Swat', 'Nowshera', 'Muzaffarabad', 'Mansehra', 'Dera Ghazi Khan', 'Gilgit', 'Mirpur', 'Gujrat', 'Hyderabad', 'Bhit Shah', 'Chitral', 'Khairpur', 'Muzzaffarabad', 'Sargodha', 'Bunnu', 'Wah Cantt', 'Jazan', 'Larkana', 'Lasbela', 'Skardu', 'Taxila', 'Rawalakot', 'Upper Dir', 'Gujranwala', 'Peshawar', 'Lakki Marwat', 'Rawalpindi', 'Kohat', 'Haripur', 'Quetta', 'Bahawalpur', 'Multan', 'Faisalabad', 'Sialkot', 'Rahim Yar Khan', 'Dera Ismail Khan', 'Jamshoro', 'Lahore', 'Amilcar', 'Swabi', 'Khuzdar', 'Sukkur', 'Khyber Pukhtunkhwa', 'testcity', 'Karachi', 'Islamabad', 'Buner', 'Abbottabad', 'Nawabshah', 'Mirpur (AK)', 'Mardan']}

df = pd.DataFrame(data)

# Function to map city to province
def get_province(city):
    province_mapping = {
        'Swat': 'Khyber Pakhtunkhwa',
        'Nowshera': 'Khyber Pakhtunkhwa',
        'Muzaffarabad': 'Azad Kashmir',
        'Mansehra': 'Khyber Pakhtunkhwa',
        'Dera Ghazi Khan': 'Punjab',
        'Gilgit': 'Gilgit-Baltistan',
        'Mirpur': 'Azad Kashmir',
        'Gujrat': 'Punjab',
        'Hyderabad': 'Sindh',
        'Bhit Shah': 'Sindh',
        'Chitral': 'Khyber Pakhtunkhwa',
        'Khairpur': 'Sindh',
        'Muzzaffarabad': 'Azad Kashmir',
        'Sargodha': 'Punjab',
        'Bunnu': 'Khyber Pakhtunkhwa',
        'Wah Cantt': 'Punjab',
        'Jazan': 'Punjab',  # Assuming this is Jhang, Punjab, not Jazan, Saudi Arabia
        'Larkana': 'Sindh',
        'Lasbela': 'Balochistan',
        'Skardu': 'Gilgit-Baltistan',
        'Taxila': 'Punjab',
        'Rawalakot': 'Azad Kashmir',
        'Upper Dir': 'Khyber Pakhtunkhwa',
        'Gujranwala': 'Punjab',
        'Peshawar': 'Khyber Pakhtunkhwa',
        'Lakki Marwat': 'Khyber Pakhtunkhwa',
        'Rawalpindi': 'Punjab',
        'Kohat': 'Khyber Pakhtunkhwa',
        'Haripur': 'Khyber Pakhtunkhwa',
        'Quetta': 'Balochistan',
        'Bahawalpur': 'Punjab',
        'Multan': 'Punjab',
        'Faisalabad': 'Punjab',
        'Sialkot': 'Punjab',
        'Rahim Yar Khan': 'Punjab',
        'Dera Ismail Khan': 'Khyber Pakhtunkhwa',
        'Jamshoro': 'Sindh',
        'Lahore': 'Punjab',
        'Amilcar': 'Unknown',  # Assuming this is not a city in Pakistan
        'Swabi': 'Khyber Pakhtunkhwa',
        'Khuzdar': 'Balochistan',
        'Sukkur': 'Sindh',
        'Khyber Pukhtunkhwa': 'Khyber Pakhtunkhwa',  # Assuming this is not a city but a province
        'testcity': 'Unknown',  # Assuming this is not a city in Pakistan
        'Karachi': 'Sindh',
        'Islamabad': 'Islamabad Capital Territory',
        'Buner': 'Khyber Pakhtunkhwa',
        'Abbottabad': 'Khyber Pakhtunkhwa',
        'Nawabshah': 'Sindh',
        'Mirpur (AK)': 'Azad Kashmir',
        'Mardan': 'Khyber Pakhtunkhwa'
    }
    return province_mapping.get(city, 'Unknown')

# Apply the function to create the new "Province" column
df['Province'] = df['city'].apply(get_province)

print(df)

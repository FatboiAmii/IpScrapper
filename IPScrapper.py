import requests

def get_location_by_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = request.get(url)
    data = response.json()

    if data['status'] == 'success':
        country = data['country']
        city = data['city']
        lattitude = data['lat']
        longtitude = data['lon']
        print(f"Lokasi IP {ip_address}: {city}, {country} ({lattitude}, {longtitude})")
    else:
        print("Tidak dapat menemukan informasi lokasi untuk IP tersebut")

ip_address = input("Masukkan alamat ip yang ingin anda lacak: ")
get_location_by_ip(ip_address)
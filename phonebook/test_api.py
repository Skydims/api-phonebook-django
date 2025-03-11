import requests

BASE_URL = "http://127.0.0.1:8000/api/contacts/"

# GET: Mendapatkan semua kontak
def get_contacts():
    response = requests.get(BASE_URL)
    print("GET /contacts/")
    print(response.status_code)
    print(response.json())

# POST: Menambahkan kontak baru
def create_contact():
    data = {
        "name": "Dimas adi saputra",
        "phone_number": "081234567890"
    }
    response = requests.post(BASE_URL, json=data)
    print("POST /contacts/")
    print(response.status_code)
    print(response.json())

# PUT: Memperbarui kontak
def update_contact(contact_id):
    data = {
        "name": "Dimas Adi saputra",
        "phone_number": "081234567891"
    }
    response = requests.put(f"{BASE_URL}{contact_id}/", json=data)
    print(f"PUT /contacts/{contact_id}/")
    print(response.status_code)
    print(response.json())

# DELETE: Menghapus kontak
def delete_contact(contact_id):
    response = requests.delete(f"{BASE_URL}{contact_id}/")
    print(f"DELETE /contacts/{contact_id}/")
    print(response.status_code)

# Jalankan fungsi-fungsi di atas
if __name__ == "__main__":
    print("Testing API Buku Telepon")
    get_contacts()         # GET semua kontak
    create_contact()       # POST menambahkan kontak baru
    update_contact(1)      # PUT memperbarui kontak dengan ID 1
    delete_contact(1)      # DELETE kontak dengan ID 1

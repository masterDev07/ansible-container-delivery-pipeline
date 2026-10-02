import sys
from inventree.api import InvenTreeAPI

# --- KONFIGURASI ---
URL = "http://192.168.43.165:5234/api/"  # Ganti dengan IP server/VPS jika remote
USERNAME = "mint"        # Username Superuser kamu
PASSWORD = "moro"    # Password Superuser kamu

try:
    print("Menghubungkan ke API InvenTree...")
    # Pastikan variabel URL, USERNAME, dan PASSWORD sudah didefinisikan sebelumnya
    api = InvenTreeAPI(URL, username=USERNAME, password=PASSWORD)
    print("✅ Berhasil terhubung ke server.")
except Exception as e:
    print(f"❌ Gagal koneksi ke server: {e}")
    sys.exit(1)

# 1. AMBIL DAFTAR USER YANG SUDAH ADA DI DATABASE (VALIDASI)
print("\nMengambil daftar username yang sudah terdaftar...")
existing_users = []

try:
    # Endpoint resmi InvenTree untuk user list biasanya ada di 'user/'
    users_data = api.get("user/")

    # InvenTree API terkadang mengembalikan list langsung atau dict dengan key 'results'
    if isinstance(users_data, dict) and "results" in users_data:
        users_list = users_data["results"]
    elif isinstance(users_data, list):
        users_list = users_data
    else:
        users_list = []

    existing_users = [u.get("username") for u in users_list if u.get("username")]
    print(f"ℹ️ Ditemukan {len(existing_users)} user terdaftar di database.")
except Exception as e:
    print(f"❌ Gagal mengambil data user: {e}")

# 2. CARI ID GROUP TIM SPLICER


group_id=1

# 3. LOOPING DENGAN VALIDASI IF-ELSE
print("\nMemulai pemrosesan 10 akun teknisi...")

for i in range(1, 3):
    num_str = f"{i:02d}"
    username_target = f"teknisi.{num_str}"

    # VALIDASI: Jika username sudah ada di list, langsung skip ke angka berikutnya
    if username_target in existing_users:
        print(f"ℹ️ [SKIP] Akun {username_target} sudah ada di database. Tidak perlu dibuat lagi.")
        continue

    # REVISI: Tambahkan field 'email' di bawah ini untuk menghindari error 'This field is required'
    payload = {
        "username": username_target,
        "first_name": "Teknisi",
        "last_name": f"Lapangan {num_str}",
        "email": f"{username_target}@domainanda.com",  # 💡 Tambahan perbaikan wajib
        "password": "FO-Teknisi2026!",
        "is_active": True,
        "is_staff": False,
        "is_superuser": False,
        "groups": [group_id]
    }

    try:
        api.post("user/", payload)
        print(f"✅ [BARU] Sukses membuat akun: {username_target}")
    except Exception as e:
        print(f"❌ Gagal membuat akun {username_target}: {e}")

print("\n[SELESAI] Sinkronisasi akun selesai.")

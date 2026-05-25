"""
KELOMPOK 11: PENGECEKAN KEBOCORAN PIPA (for ... else)
Skenario: Sensor mendeteksi kebocoran di sepanjang jalur pipa
          yang dibagi menjadi 10 segmen.
          0 = Aman | 1 = Bocor
Pengembangan: Lab Case & Industri Kimia
"""

import time
import random
from datetime import datetime


# ─────────────────────────────────────────────────────────────
# FUNGSI UTILITAS
# ─────────────────────────────────────────────────────────────

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def cetak_header():
    print("=" * 60)
    print("   SISTEM PENGECEKAN KEBOCORAN PIPA - INDUSTRI KIMIA")
    print("   Kelompok 11 | Metode: for ... else")
    print(f"   Waktu Pengecekan : {timestamp()}")
    print("=" * 60)

def cetak_segmen(data_segmen):
    print("\n  [INFO] Data Sensor Per Segmen:")
    print("  " + "-" * 40)
    for i, nilai in enumerate(data_segmen, start=1):
        status = "🔴 BOCOR" if nilai == 1 else "🟢 Aman "
        print(f"    Segmen {i:02d}  :  [{nilai}]  →  {status}")
    print("  " + "-" * 40)

def laporan_akhir(bocor_list):
    print("\n" + "=" * 60)
    print("   LAPORAN AKHIR PENGECEKAN")
    print("=" * 60)
    if bocor_list:
        print(f"  ⚠️  Total Kebocoran Ditemukan : {len(bocor_list)} segmen")
        print(f"  📍 Segmen Bermasalah         : {bocor_list}")
        print(f"  🔧 Rekomendasi               : Lakukan perbaikan segera")
        print(f"                                 pada segmen di atas.")
    else:
        print("  ✅ Tidak ada kebocoran terdeteksi.")
        print("  👍 Rekomendasi: Jalur pipa dalam kondisi prima.")
    print("=" * 60)


# ─────────────────────────────────────────────────────────────
# FUNGSI UTAMA: PENGECEKAN DENGAN for ... else
# ─────────────────────────────────────────────────────────────

def cek_kebocoran_pertama(data_segmen):
    """
    Sesuai soal: cari kebocoran PERTAMA saja, lalu break.
    Gunakan else untuk mencetak 'Seluruh jalur pipa aman'.
    """
    print("\n  [MODE] Deteksi Kebocoran Pertama (for ... else)")
    print("  " + "-" * 40)

    for i, nilai in enumerate(data_segmen, start=1):
        print(f"    Memeriksa Segmen {i:02d}...", end=" ")
        time.sleep(0.3)  # simulasi waktu baca sensor
        if nilai == 1:
            print(f"⚠️  BOCOR!")
            print(f"\n  ❌ KEBOCORAN DI SEGMEN {i}!")
            print(f"     → Pengecekan dihentikan, segmen bocor ditemukan.")
            break
        else:
            print("✅ Aman")
    else:
        # Blok else hanya jalan jika for selesai TANPA break
        print("\n  ✅ SELURUH JALUR PIPA AMAN!")
        print("     → Tidak ada kebocoran pada semua segmen.")


def cek_kebocoran_lengkap(data_segmen):
    """
    Pengembangan industri: scan SEMUA segmen, catat semua yang bocor.
    """
    print("\n  [MODE] Scan Lengkap Semua Segmen (Industri Kimia)")
    print("  " + "-" * 40)

    bocor_list = []

    for i, nilai in enumerate(data_segmen, start=1):
        print(f"    Memeriksa Segmen {i:02d}...", end=" ")
        time.sleep(0.2)
        if nilai == 1:
            print(f"⚠️  BOCOR!")
            bocor_list.append(i)
        else:
            print("✅ Aman")

    laporan_akhir(bocor_list)
    return bocor_list


# ─────────────────────────────────────────────────────────────
# INPUT DATA SEGMEN
# ─────────────────────────────────────────────────────────────

def input_manual():
    print("\n  Masukkan status 10 segmen (0=Aman, 1=Bocor):")
    data = []
    for i in range(1, 11):
        while True:
            try:
                val = int(input(f"    Segmen {i:02d}: "))
                if val in (0, 1):
                    data.append(val)
                    break
                else:
                    print("    ⚠️  Masukkan 0 atau 1 saja!")
            except ValueError:
                print("    ⚠️  Input tidak valid!")
    return data

def input_otomatis():
    # Simulasi sensor acak: peluang bocor ~20%
    data = [random.choices([0, 1], weights=[80, 20])[0] for _ in range(10)]
    print(f"\n  [SENSOR OTOMATIS] Data dihasilkan: {data}")
    return data

def input_contoh_bocor():
    # Contoh hardcoded: segmen 4 dan 7 bocor
    data = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    print(f"\n  [CONTOH TETAP] Data: {data}")
    return data

def input_contoh_aman():
    # Semua aman
    data = [0] * 10
    print(f"\n  [CONTOH AMAN] Data: {data}")
    return data


# ─────────────────────────────────────────────────────────────
# MENU UTAMA
# ─────────────────────────────────────────────────────────────

def menu():
    print("\n┌─────────────────────────────────────────┐")
    print("│           PILIH SUMBER DATA SENSOR      │")
    print("├─────────────────────────────────────────┤")
    print("│  1. Input manual (10 segmen)            │")
    print("│  2. Sensor otomatis (acak)              │")
    print("│  3. Contoh: ada kebocoran (segmen 4 & 7)│")
    print("│  4. Contoh: semua segmen aman           │")
    print("│  5. Keluar                              │")
    print("└─────────────────────────────────────────┘")
    return input("  Pilih [1-5]: ").strip()

def menu_mode():
    print("\n┌─────────────────────────────────────────┐")
    print("│           PILIH MODE PENGECEKAN         │")
    print("├─────────────────────────────────────────┤")
    print("│  1. Deteksi kebocoran pertama (for-else)│")
    print("│  2. Scan lengkap semua segmen           │")
    print("│  3. Keduanya                            │")
    print("└─────────────────────────────────────────┘")
    return input("  Pilih [1-3]: ").strip()


# ─────────────────────────────────────────────────────────────
# PROGRAM UTAMA
# ─────────────────────────────────────────────────────────────

def main():
    cetak_header()

    # Pilih sumber data
    pilihan_data = menu()
    if pilihan_data == "1":
        data_segmen = input_manual()
    elif pilihan_data == "2":
        data_segmen = input_otomatis()
    elif pilihan_data == "3":
        data_segmen = input_contoh_bocor()
    elif pilihan_data == "4":
        data_segmen = input_contoh_aman()
    elif pilihan_data == "5":
        print("\n👋 Keluar dari sistem.")
        return
    else:
        print("⚠️  Pilihan tidak valid. Menggunakan sensor otomatis.")
        data_segmen = input_otomatis()

    # Tampilkan data segmen
    cetak_segmen(data_segmen)

    # Pilih mode pengecekan
    mode = menu_mode()
    print()

    if mode == "1":
        cek_kebocoran_pertama(data_segmen)
    elif mode == "2":
        cek_kebocoran_lengkap(data_segmen)
    elif mode == "3":
        cek_kebocoran_pertama(data_segmen)
        cek_kebocoran_lengkap(data_segmen)
    else:
        print("⚠️  Mode tidak valid. Menjalankan mode pertama.")
        cek_kebocoran_pertama(data_segmen)

    print(f"\n  [Selesai] Waktu: {timestamp()}\n")


if __name__ == "__main__":
    main()

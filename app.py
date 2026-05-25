"""
KELOMPOK 11: PENGECEKAN KEBOCORAN PIPA (for ... else)
Versi: Streamlit Web App
Skenario: Sensor mendeteksi kebocoran di sepanjang jalur pipa
          yang dibagi menjadi 10 segmen.
          0 = Aman | 1 = Bocor
"""

import streamlit as st
from datetime import datetime

# ─────────────────────────────────────────────────────────────
# KONFIGURASI HALAMAN
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Pengecekan Kebocoran Pipa",
    page_icon="🔧",
    layout="centered"
)

st.title("🔧 Sistem Pengecekan Kebocoran Pipa")
st.caption("Kelompok 11 | Metode: `for ... else` | Industri Kimia")
st.markdown("---")

# ─────────────────────────────────────────────────────────────
# PILIH SUMBER DATA
# ─────────────────────────────────────────────────────────────
st.subheader("📡 Sumber Data Sensor")

sumber = st.radio(
    "Pilih cara input data segmen:",
    ["Input Manual", "Acak Otomatis (Simulasi Sensor)", "Contoh: Ada Kebocoran (Segmen 4 & 7)", "Contoh: Semua Aman"],
    horizontal=False
)

data_segmen = []

if sumber == "Input Manual":
    st.markdown("**Masukkan status tiap segmen (0 = Aman, 1 = Bocor):**")
    cols = st.columns(5)
    for i in range(10):
        with cols[i % 5]:
            val = st.selectbox(f"Segmen {i+1:02d}", options=[0, 1], key=f"seg_{i}")
            data_segmen.append(val)

elif sumber == "Acak Otomatis (Simulasi Sensor)":
    import random
    if st.button("🔄 Generate Data Sensor"):
        data_segmen = [random.choices([0, 1], weights=[80, 20])[0] for _ in range(10)]
        st.session_state["data_acak"] = data_segmen
    data_segmen = st.session_state.get("data_acak", [0]*10)

elif sumber == "Contoh: Ada Kebocoran (Segmen 4 & 7)":
    data_segmen = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]

elif sumber == "Contoh: Semua Aman":
    data_segmen = [0] * 10

# ─────────────────────────────────────────────────────────────
# TAMPILKAN DATA SEGMEN
# ─────────────────────────────────────────────────────────────
if data_segmen:
    st.markdown("---")
    st.subheader("📊 Status Sensor Per Segmen")

    cols = st.columns(10)
    for i, val in enumerate(data_segmen):
        with cols[i]:
            if val == 1:
                st.error(f"**{i+1}**\n\n🔴")
                st.caption("Bocor")
            else:
                st.success(f"**{i+1}**\n\n🟢")
                st.caption("Aman")

    st.markdown(f"**Data mentah:** `{data_segmen}`")

# ─────────────────────────────────────────────────────────────
# PILIH MODE PENGECEKAN
# ─────────────────────────────────────────────────────────────
st.markdown("---")
st.subheader("⚙️ Mode Pengecekan")

mode = st.radio(
    "Pilih mode:",
    ["Deteksi Kebocoran Pertama (for-else)", "Scan Lengkap Semua Segmen", "Keduanya"],
    horizontal=False
)

# ─────────────────────────────────────────────────────────────
# TOMBOL CEK
# ─────────────────────────────────────────────────────────────
st.markdown("---")
if st.button("🚀 Mulai Pengecekan", use_container_width=True, type="primary"):

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"🕐 **Waktu Pengecekan:** `{waktu}`")
    st.markdown("---")

    # ── MODE 1: for ... else (kebocoran pertama) ──────────────
    def cek_pertama(data):
        st.markdown("### 🔍 Mode: Deteksi Kebocoran Pertama (`for ... else`)")
        log = []
        bocor_ditemukan = False

        for i, nilai in enumerate(data, start=1):
            if nilai == 1:
                log.append(f"🔴 Segmen {i:02d} → **BOCOR**")
                st.warning(f"❌ **KEBOCORAN DITEMUKAN DI SEGMEN {i}!**")
                st.info("ℹ️ Pengecekan dihentikan pada segmen pertama yang bocor (break).")
                bocor_ditemukan = True
                break
            else:
                log.append(f"🟢 Segmen {i:02d} → Aman")

        else:
            # else hanya jalan jika for selesai tanpa break
            st.success("✅ **SELURUH JALUR PIPA AMAN!**")
            st.info("ℹ️ Blok `else` dieksekusi karena tidak ada `break` terjadi.")

        with st.expander("📋 Log Pemeriksaan Segmen"):
            for baris in log:
                st.markdown(baris)

    # ── MODE 2: Scan Lengkap ──────────────────────────────────
    def cek_lengkap(data):
        st.markdown("### 🏭 Mode: Scan Lengkap Semua Segmen (Industri Kimia)")
        bocor_list = []
        log = []

        for i, nilai in enumerate(data, start=1):
            if nilai == 1:
                bocor_list.append(i)
                log.append(f"🔴 Segmen {i:02d} → **BOCOR**")
            else:
                log.append(f"🟢 Segmen {i:02d} → Aman")

        with st.expander("📋 Log Pemeriksaan Semua Segmen", expanded=True):
            for baris in log:
                st.markdown(baris)

        st.markdown("#### 📄 Laporan Akhir")
        if bocor_list:
            st.error(f"⚠️ **{len(bocor_list)} kebocoran ditemukan** di segmen: {bocor_list}")
            st.warning("🔧 **Rekomendasi:** Lakukan perbaikan segera pada segmen bermasalah.")
        else:
            st.success("✅ **Seluruh jalur pipa aman. Tidak ada kebocoran.**")
            st.info("👍 **Rekomendasi:** Jalur pipa dalam kondisi prima.")

    # ── JALANKAN SESUAI MODE ──────────────────────────────────
    if mode == "Deteksi Kebocoran Pertama (for-else)":
        cek_pertama(data_segmen)
    elif mode == "Scan Lengkap Semua Segmen":
        cek_lengkap(data_segmen)
    elif mode == "Keduanya":
        cek_pertama(data_segmen)
        st.markdown("---")
        cek_lengkap(data_segmen)

# ─────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("Kelompok 11 · Pengecekan Kebocoran Pipa · Python `for...else` · Industri Kimia")

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from datetime import time

# ==========================
# TOKEN BOT
# ==========================
TOKEN = "8895647105:AAF5kWGSb-xK7F5Ga1JZdHl1xhnBFirOsUM"

# ==========================
# CHAT ID
# ==========================
CHAT_ID = 5203687674

# ==========================
# PERINTAH /start
# ==========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Halo!\n\n"
        "Aku PowerSaver Bot.\n"
        "Aku akan mengingatkan untuk mematikan lampu kelas agar hemat energi. 💡"
    )

# ==========================
# PESAN PAGI
# ==========================
async def pagi(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="""
🌞 Selamat pagi!

Selamat belajar hari ini.

Sebelum pembelajaran dimulai, pastikan lampu kelas yang tidak digunakan sudah dimatikan.

Hemat energi dimulai dari kita! 💡
"""
    )

# ==========================
# PESAN SIANG
# ==========================
async def siang(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="""
🍽️ Waktu istirahat!

Jika kelas sudah terang, seterang masa depanmu, jangan lupa matikan lampu yang tidak digunakan ya. 💡

Setiap langkah kecil membantu menghemat energi. 🌱
"""
    )

# ==========================
# PESAN SORE
# ==========================
async def sore(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="""
🏫 Sebelum pulang

Pastikan:
✅ Lampu kelas sudah dimatikan
✅ Kipas angin sudah dimatikan
✅ AC, proyektor, atau peralatan listrik lainnya sudah dimatikan (jika digunakan)

Terima kasih telah menjadi Pahlawan Hemat Energi! 🌱💡
"""
    )

# ==========================
# MEMBUAT BOT
# ==========================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

# ==========================
# JADWAL OTOMATIS
# ==========================
job_queue = app.job_queue

job_queue.run_daily(pagi, time=time(7, 30))
job_queue.run_daily(siang, time=time(12, 0))
job_queue.run_daily(sore, time=time(15, 30))

# ==========================
print("PowerSaver Bot sedang berjalan...")
app.run_polling()

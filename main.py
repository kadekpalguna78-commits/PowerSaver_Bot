from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import time
from zoneinfo import ZoneInfo

# ==========================================
# KONFIGURASI
# ==========================================

TOKEN = "8895647105:AAF5kWGSb-xK7F5Ga1JZdHl1xhnBFirOsUM"
CHAT_ID = 5203687674

WITA = ZoneInfo("Asia/Makassar")

# ==========================================
# PERINTAH /start
# ==========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Halo!\n\n"
        "Selamat datang di *PowerSaver Bot* 💡\n\n"
        "Bot ini membantu mengingatkan warga sekolah untuk menghemat energi.\n\n"
        "Ketik /menu untuk melihat semua fitur.",
        parse_mode="Markdown"
    )

# ==========================================
# MENU
# ==========================================

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 *MENU POWERSAVER BOT*\n\n"
        "🏠 /start\n"
        "📋 /menu\n"
        "💡 /hemat\n"
        "📝 /lapor\n"
        "🧪 /test\n\n"
        "Bot juga akan mengirim pengingat otomatis setiap hari.",
        parse_mode="Markdown"
    )

# ==========================================
# TIPS HEMAT
# ==========================================

async def hemat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 *Tips Hemat Energi*\n\n"
        "✅ Matikan lampu jika kelas kosong.\n"
        "✅ Gunakan cahaya matahari bila cukup terang.\n"
        "✅ Matikan kipas/AC jika tidak digunakan.\n"
        "✅ Cabut charger setelah dipakai.\n\n"
        "🌱 Mari menjadi pelopor hemat energi!",
        parse_mode="Markdown"
    )

# ==========================================
# LAPOR
# ==========================================

async def lapor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 Laporan diterima.\n\n"
        "Terima kasih telah melaporkan kondisi lampu kelas.\n"
        "Mari bersama menjaga budaya hemat energi. 💡"
    )

# ==========================================
# TEST
# ==========================================

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="✅ TEST BERHASIL!\nPowerSaver Bot aktif dan dapat mengirim pesan."
    )

# ==========================================
# NOTIFIKASI PAGI
# ==========================================

async def pagi(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="""
🌞 Selamat Pagi!

Selamat belajar hari ini.

Sebelum pelajaran dimulai,
pastikan lampu yang tidak digunakan sudah dimatikan.

💡 Hemat energi dimulai dari kita!
"""
    )

# ==========================================
# NOTIFIKASI SIANG
# ==========================================

async def siang(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="""
🍽️ Waktu Istirahat

Jika kelas sudah cukup terang,
jangan lupa matikan lampu yang tidak diperlukan.

🌱 Setiap langkah kecil membantu menghemat energi.
"""
    )

# ==========================================
# NOTIFIKASI SORE
# ==========================================

async def sore(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="""
🏫 Sebelum Pulang

Mohon pastikan:

✅ Lampu sudah dimatikan
✅ Kipas sudah dimatikan
✅ AC sudah dimatikan (jika ada)
✅ Proyektor sudah dimatikan

Terima kasih telah menjadi
💡 Pahlawan Hemat Energi 🌱
"""
    )

# ==========================================
# MEMBUAT BOT
# ==========================================

app = ApplicationBuilder().token(TOKEN).build()

# COMMAND
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("hemat", hemat))
app.add_handler(CommandHandler("lapor", lapor))
app.add_handler(CommandHandler("test", test))

# ==========================================
# JADWAL OTOMATIS
# ==========================================

job_queue = app.job_queue

job_queue.run_daily(
    pagi,
    time=time(hour=7, minute=30, tzinfo=WITA)
)

job_queue.run_daily(
    siang,
    time=time(hour=12, minute=0, tzinfo=WITA)
)

job_queue.run_daily(
    sore,
    time=time(hour=15, minute=30, tzinfo=WITA)
)

print("✅ PowerSaver Bot sedang berjalan...")

app.run_polling()